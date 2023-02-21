import logging
import uuid
import json
import time
from importlib_metadata import version
from typing import Optional, Literal
from platform import platform

import requests
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from godel import schema

from godel.fragments.EntityLink import fragment_entity_link
from godel.fragments.EntityDetail import fragment_entity_detail
from godel.fragments.EntitySummary import fragment_entity_summary
from godel.fragments.PredicateDetails import fragment_predicate_details
from godel.fragments.TripleWidget import fragment_triple_widget

from godel.queries.AddTripleToEntityById import (
    Operations as AddTripleToEntityByIdOperations,
)
from godel.queries.Authenticate import Operations as AuthenticateOperations
from godel.queries.CreateEntity import Operations as CreateEntityOperations
from godel.queries.CreateValidation import Operations as CreateValidationOperations
from godel.queries.CreateStatement import Operations as CreateStatementOperations
from godel.queries.CreateTripleFlag import Operations as CreateTripleFlagOperations

# from godel.queries.CurrentUserBlockchainData import Operations as CurrentUserBlockchainDataOperations
# from godel.queries.CurrentUserValidations import (
# Operations as CurrentUserValidationsOperations,
# )
from godel.queries.EntityByName import Operations as EntityByNameOperations
from godel.queries.EntityGolden import Operations as EntityGoldenOperations
from godel.queries.EntitySearch import Operations as EntitySearchOperations
from godel.queries.GetAuthenticationMessage import (
    Operations as GetAuthenticationMessageOperations,
)
from godel.queries.GetCurrentUser import Operations as GetCurrentUserOperations
from godel.queries.GetEntities import Operations as GetEntitiesOperations
from godel.queries.GetTripleForValidation import (
    Operations as GetTripleForValidationOperations,
)
from godel.queries.LiveView import Operations as LiveViewOperations
from godel.queries.Predicate import Operations as PredicateOperations
from godel.queries.Templates import Operations as TemplatesOperations
from godel.queries.EntityDetail import Operations as EntityDetailOperations
from godel.queries.AssignValidation import Operations as AssignValidationOperations

from .models import (
    DisambiguationTripleDict,
    PredicateWeightDict,
    DisambiguationValidationStatus,
)

logger = logging.getLogger(__name__)


class GoldenAPI:
    def __init__(
        self,
        url: str = "https://dapp.golden.xyz/graphql",
        jwt_token: str = "",
        headers: dict = {},
        timeout: float = None,
        load_test: bool = False,
    ):
        self.load_test = load_test
        self.url = url
        self.jwt_token = jwt_token
        self.headers = headers
        self.headers[
            "User-Agent"
        ] = f"golden sdk v-{get_godel_version()}_{platform().lower()}"
        self.headers["X-Device-Id"] = str(uuid.UUID(int=uuid.getnode()))
        self.headers["X-metrics"] = "{}"
        self.headers.update(
            {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}
        )
        self.timeout = timeout
        self.endpoint = HTTPEndpoint(self.url, self.headers, timeout=self.timeout)

    #####################
    ## Utility Methods ##
    #####################

    def set_jwt_token(self, jwt_token: str = "") -> None:
        """Set your token to start accessing the API with your wallet/role

        Args:
            jwt_token (str): JWT Token. Defaults to "".
        """
        self.jwt_token = jwt_token
        self.headers.update(
            {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}
        )
        self.endpoint = HTTPEndpoint(self.url, self.headers, timeout=self.timeout)

    def query(self, query: str = "", variables: dict = {}) -> dict:
        """Generic method to query graphql endpoint"""
        data = self.endpoint(query, variables)
        return data

    @classmethod
    def generate_variables(cls, op: Operation, params: dict) -> dict:
        """Helper for retrieving variable names from operation
        and making variable object for endpoint

        Args:
            op (Operation): sgqlc operation
            params dict: variable values from methods

        Returns:
            dict: dict of variable names
        """
        var_args = op._Operation__args
        variables = {}
        for name in map(lambda x: x.strip("$"), var_args):
            variables[name] = None  # Set placeholder
        for p, v in params.items():
            p = cls.to_camel_case(p)
            if p in variables:
                variables[p] = v
        return variables

    @staticmethod
    def to_camel_case(snake_str: str) -> str:
        """Convert snake str to camel case since all params
        should eventually adhere to graphql camel case

        Args:
            snake_str (str): snake string

        Returns:
            str: lower camel case
        """
        components = snake_str.split("_")
        return components[0] + "".join(x.title() for x in components[1:])

    ####################
    ## Authentication ##
    ####################

    # Retrieve JWT Token

    def get_authentication_message(self, user_id: str, **kwargs) -> dict:
        """Retrieve auth message to sign with your wallet to verify your role and account

        Args:
            user_id (str): Ether wallet address (Hex)

        Returns:
            dict: payload with string message
        """
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = GetAuthenticationMessageOperations.mutation.get_authentication_message
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    def authenticate(self, user_id: str, signature: str, **kwargs) -> dict:
        """Authenticate your signature with the GraphQL API

        Args:
            user_id(str): Ether wallet address (Hex)
            signature (str): Signed auth message (Hex)

        Returns:
            dict: payload with JWT bearer token
        """
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = AuthenticateOperations.mutation.authenticate
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    def get_authentication_token(
        self, user_id: str, wallet_private_key: str, **kwargs
    ) -> str:
        """Convenience method for calling `getAuthenticationMessage` and `authenticate`
        given a user's wallet address and private key to obtain a JWT bearer token.
        Private key param is never sent to the API. This package only uses it to generate
        your signature using web3.py

        Calling this method will automatically set self.jwt_token which will be used in
        your graphql request headers.

        Args:
            user_id(str): Wallet address (Hex)
            sign (str): Wallet private key

        Returns:
            str: your JWT bearer token
        """
        try:
            from web3.auto import w3
            from eth_account.messages import encode_defunct
        except ModuleNotFoundError:
            logger.info("Need to install web3.py package")
            return
        message_response = self.get_authentication_message(user_id=user_id)
        try:
            message_string = message_response["data"]["getAuthenticationMessage"][
                "string"
            ]
        except:
            return message_response
        message = encode_defunct(text=message_string)
        signed_message = w3.eth.account.sign_message(
            message, private_key=wallet_private_key
        )
        signature = signed_message.signature.hex()
        auth_token = self.authenticate(user_id=user_id, signature=signature)
        try:
            self.set_jwt_token(jwt_token=auth_token["data"]["authenticate"]["jwtToken"])
        except:
            return auth_token
        return auth_token

    #############
    ## Queries ##
    #############

    # Entities and Disambiguation

    def entity_by_name(self, name: str, first: int = 10, **kwargs) -> dict:
        """Retrieve entity by name

        Args:
            name (str): name of entity
            first (int, optional): number of results. Defaults to 20.

        Returns:
            dict: search results
        """
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = EntityByNameOperations.query.entity_by_name
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    def entity_by_golden_id(self, golden_id: str, **kwargs) -> dict:
        """Retrieve entity by golden.com entity ID

        Args:
            golden_id (str): must be an integer

        Returns:
            dict: _description_
        """
        try:
            int(golden_id)
        except:
            ValueError(f"golden_id param must be integer not {golden_id}")
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = EntityGoldenOperations.query.entity_golden
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    def entity_search(self, name: str, first: int = 20, **kwargs) -> dict:
        """Base entity search with SQL

        Args:
            name (str): name of entity searched
            first (int, Optional): number of results. Defaults to 20.

        Returns:
            dict: search results
        """
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = EntitySearchOperations.query.entity_search
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    def entity_detail(self, id: str, **kwargs) -> dict:
        """Retrieve entity details, includes rich template and statement values

        Args:
            id (str): id of entity to retrieve

        Returns:
            dict: Entity with details
        """
        query = """query EntityDetail($id: UUID!) {
            entity(id: $id) {
              ...EntityDetail
              isEntityType
            }
            templates(orderBy: RANK_ASC) {
              nodes {
                entityId
                templatePredicates(orderBy: RANK_ASC) {
                  nodes {
                    predicate {
                      ...PredicateDetails
                    }
                  }
                }
              }
            }
        }
              %s
              %s
              %s
            """ % (
            str(fragment_entity_detail()),
            str(fragment_predicate_details()),
            str(fragment_triple_widget()),
        )
        variables = {"id": id}
        if self.load_test:
            json_body = {"query": query, "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(query, variables)
        return data

    def entity_with_triples(self, id: str) -> dict:
        """Retrieve entity with both entity to value triples and entity to entity triples

        Args:
            entity_id (str): id of entity to retrieve

        Returns:
            dict: Entity with triples
        """

        query = """query entityWithTriples(
            $id: UUID!
            ){
              entity(id: $id) {
              id
                statementsBySubjectId {
                  nodes {
                    id
                    objectEntityId
                    objectValue
                    predicate {
                      name
                    }
                    objectEntity {
                      name
                    }
                  }
                }
              }
            }"""
        variables = {"id": id}
        if self.load_test:
            json_body = {"query": query, "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(query, variables)
        return data

    def disambiguate_triples(
        self,
        triples: DisambiguationTripleDict,
        predicate_weights: Optional[PredicateWeightDict] = None,
        validation_status: Optional[DisambiguationValidationStatus] = None,
        distance_threshold: float = 0.3,
        with_diff: bool = False,
        source: Literal["PROTOCOL", "GOLDENCOM"] = "PROTOCOL",
        **kwargs,
    ) -> dict:
        """Disambiguate entities given the predicate and object value or entity ID

        Args:
            triples (DisambiguationTripleDict): dict with <predicate, object> pairs. i.e: {"Name": "Twitter Inc.", "Website": "https://twitter.com"}
            predicate_weights: None or a dictionary indicating the specific weight of the predicates when calculating the distance metric.
                               The default predicate weight is 1.0. A higher value will have more weight when calculating the overall entity distance
                               while a lower one will be less important. Use only if your workload doesn't work well with the system's defaults.
                               As a special case, predicates wight a weight of 0 will not be considered for distance calculations, nor for searching
                               entity candidates that might match.
            validation_status: None or ["ACCEPTED", "REJECTED", "PENDING", "INVALID", "PAUSED"]. If specified, will only search on submitted triples
                               with the given status
            distance_threshold: (float). Cutoff distance value for the resulting disambiguation candidates. 0.3 by default. 0 indicates a perfect
                                match (more stringent), while 1 indicates total disparity (more relaxed)
            with_diff: (bool). Indicates whether the response should include a full diff, indicating which of the submitted triples have already been
                        added onto the graph, and which haven't.
            source: "PROTOCOL" or "GOLDENCOM". Indicates the source to execute disambiguation against. By default, disambiguation is performed against
                    data submitted to the protocol but, if you want, you can also run it against data submitted against GOLDEN.COM. The predicate format
                    is exactly the same. The only difference being that the id from the entity response will match the slug of the entity on Golden.com,
                    instead of being a UUID.

        Returns:
            dict: Entities with details
        """
        predicate_object_pairs = []
        for k, v in triples.items():
            if isinstance(v, dict):
                # Nested object. Need to disambiguate it first
                r = self.disambiguate_triples(
                    v,
                    predicate_weights=predicate_weights,
                    validation_status=validation_status,
                    distance_threshold=distance_threshold,
                    with_diff=False,
                    source=source,
                    **kwargs,
                )
                candidate_entities = sorted(
                    [e for e in r["data"]["disambiguateTriples"]["entities"]],
                    key=lambda e: -e["reputation"],
                )
                if candidate_entities:
                    v = candidate_entities[0]["id"]
                else:
                    continue
            predicate_object = {
                "predicate": k,
                "object": v,
            }
            predicate_object_pairs.append(predicate_object)
        predicate_weight_pairs = (
            [{"predicate": k, "weight": v} for k, v in predicate_weights.items()]
            if predicate_weights
            else None
        )

        query = """query DisambiguateTriple(
            $triples: [DisambiguationInputTripleModel!]!,
            $predicateWeights: [PredicateWeightInput!],
            $source: DisambiguationSource,
            $validationStatus: ValidationStatus,
            $withDiff: Boolean! = false
            ){
                disambiguateTriples(
                payload: {
                    triples: $triples
                    validationStatus: $validationStatus
                    predicateWeights: $predicateWeights
                    source: $source
                }
              ) {
                errors
                entities {
                  name
                  distance
                  id
                  reputation
                  diff @include(if: $withDiff) {
                    matches {
                        id
                        validation_status
                        predicate
                        object
                    }
                    inserts {
                        object
                        predicate
                    }
                    updates {
                        source {
                            id
                            object
                            predicate
                            validation_status
                        }
                        update {
                            object
                            predicate
                        }
                    }
                  }
                }
              }
            }"""
        variables = {
            "triples": predicate_object_pairs,
            "validationStatus": validation_status,
            "withDiff": with_diff,
            "predicateWeights": predicate_weight_pairs,
            "source": source,
        }
        if self.load_test:
            json_body = {"query": query, "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(query, variables)
        if (
            ("data" in data)
            and ("disambiguateTriples" in data["data"])
            and ("entities" in data["data"]["disambiguateTriples"])
        ):
            data["data"]["disambiguateTriples"]["entities"] = [
                e
                for e in data["data"]["disambiguateTriples"]["entities"]
                if e["distance"] <= distance_threshold
            ]
        return data

    # Predicates

    def predicate_by_name(self, name: str, **kwargs) -> dict:
        """Get predicate given name

        Args:
            name (str): name of prediate

        Returns:
            dict: predicate object returned
        """
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = PredicateOperations.query.predicate
        variables = self.generate_variables(op, params)
        data = self.endpoint(op, variables)
        return data

    def predicate_by_id(self, id: str) -> dict:
        """Get all predicates

        Returns:
            dict: List of available predicates
        """
        query = f"""query MyQuery {{
            predicate(id: "{id}") {{
              id
              name
              objectType
            }}
        }}"""
        variables = {}
        if self.load_test:
            json_body = {"query": query, "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(query, variables)
        return data

    def predicates(self) -> dict:
        """Get all predicates

        Returns:
            dict: List of available predicates
        """
        query = """query MyQuery {
            predicates {
              edges {
                node {
                  id
                  name
                  objectType
                  label
                  description
                  citationRequirement
                  objectType
                }
              }
            }
        }"""
        variables = {}
        if self.load_test:
            json_body = {"query": query, "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(query, variables)
        return data

    # Templates
    def templates(self) -> dict:
        """Get all templates

        Returns:
            dict: List of available templates
        """
        query = """query MyQuery {
            templates {
              edges {
                node {
                  id
                  entityId 
                  entity {
                    name
                    description
                  }
                }
              }
            }
        }"""
        variables = {}
        if self.load_test:
            json_body = {"query": query, "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(query, variables)
        return data

    # Validation

    def get_triple_for_validation(self, **kwargs) -> dict:
        """Get triple for validation

        Returns:
            dict: data contain triple to validate
        """
        op = GetTripleForValidationOperations.query.get_triple_for_validation
        data = self.endpoint(op)
        return data

    def assign_validation(self, force: bool = False, **kwargs) -> dict:
        """Get unvalidated triple id from queue

        Returns:
            dict: Unvalidated triple id
        """
        op = AssignValidationOperations.mutation.assign_validation
        data = self.endpoint(op)
        if self.load_test and not force:
            json_body = {
                "query": bytes(op).decode("utf-8"),
            }
            return json_body, self.url, self.headers
        return data

    def unvalidated_triple(self) -> dict:
        """Get unvalidated triple from queue

        Returns:
            dict: Unvalidated triple
        """
        assign_validation = self.assign_validation(force=True)
        try:
            triple_id = (
                assign_validation.get("data")
                .get("assignValidation")
                .get("assignedValidation")
                .get("tripleId")
            )
        except:
            logger.warning(
                f"Could not retrieve assigned validation: {assign_validation}"
            )
            return assign_validation

        # TODO: Replace once sgqlc supports GetTripleForValidation nested fragment
        query = """query GetTripleForValidation($id: UUID!) {
            triple(id: $id) {
              ... on Statement {
                id
                dateCreated
                dateRejected
                dateAccepted
                dateSlashed
                objectValue
                objectEntityId
                subjectId
                userId
                predicateId
                citationsByTripleId {
                  nodes {
                    url
                  }
                }
              }
            }
        }
        """

        variables = {"id": triple_id}
        if self.load_test:
            json_body = {"query": query, "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(query, variables)

        x_metrics = json.loads(self.headers.get("X-metrics"))
        if x_metrics.get("cv"):
            x_metrics.pop("cv")
        x_metrics.update({"uv": time.time()})
        self.headers["X-metrics"] = json.dumps(x_metrics)

        return data

    ###############
    ## Mutations ##
    ###############

    # Entity Submissions
    def create_entity(self, create_entity_input: schema.CreateEntityInput, **kwargs):
        """Create an entity given the MDTs/statement inputs required for entity creation.

        Args:
            input (CreateEntityInput): Create Entity input

        Returns:
            dict: created entity
        """
        # TODO: Debug why entity link fragment isn't registered...for now use query
        # data = self.query(query=f"""
        # mutation MyMutation {{
        #   createEntity(input: {{name: "{name}"}}) {{
        #     entity {{
        #       id
        #     }}
        #   }}
        # }}
        # """,
        # headers=self.headers,
        # )
        # return data
        x_metrics = json.loads(self.headers.get("X-metrics"))
        ce_metrics = time.time()
        if x_metrics.get("ce"):
            x_metrics.update({"ced": ce_metrics - x_metrics.get("ce")})
        x_metrics.update({"ce": ce_metrics})
        self.headers["X-metrics"] = json.dumps(x_metrics)

        input = create_entity_input.__to_json_value__()
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = CreateEntityOperations.mutation.create_entity
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    # Triples Submissions

    def create_statement(
        self, create_statement_input: schema.CreateStatementInput, **kwargs
    ):
        """Create statement triple given the statement input combinations of subject entity id, predicate id, object id/value, and citation url

        Args:
            input (CreateStatementInput): Create statement record input

        Returns:
            dict: created statement
        """
        x_metrics = json.loads(self.headers.get("X-metrics"))
        ce_metrics = time.time()
        if x_metrics.get("cs"):
            x_metrics.update({"csd": ce_metrics - x_metrics.get("cs")})
        x_metrics.update({"cs": ce_metrics})
        self.headers["X-metrics"] = json.dumps(x_metrics)

        input = create_statement_input.__to_json_value__()
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = CreateStatementOperations.mutation.create_statement
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    # Validation Submissions

    def create_validation(self, triple_id: str, validation_type: str, **kwargs) -> dict:
        """Create verification vote

        Args:
            triple_id (str): Your triple id
            validation_type (str): Verfication type "ACCEPTED", "REJECTED", "SKIPPED"

        Returns:
            dict: created verification task
        """
        x_metrics = json.loads(self.headers.get("X-metrics"))
        x_metrics.update({"cv": time.time()})
        if x_metrics.get("uv"):
            x_metrics.update({"vd": x_metrics.get("cv") - x_metrics.get("uv")})
        self.headers["X-metrics"] = json.dumps(x_metrics)

        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = CreateValidationOperations.mutation.create_validation
        variables = self.generate_variables(op, params)
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    # Create Triple Flag

    def create_triple_flag(
        self, create_triple_flag_input: schema.CreateTripleFlagInput, **kwargs
    ) -> dict:
        """Create triple flag given the triple flag inputs consisting of triple_id and your flag

        Args:
            create_triple_flag_input (schema.CreateTripleFlagInput): Triple flag input

        Returns:
            dict: created triple flag
        """
        # Special case for parsing input
        variables = create_triple_flag_input.__to_json_value__()
        for p, v in variables.items():
            p = self.to_camel_case(p)
            if p in variables:
                variables[p] = v

        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = CreateTripleFlagOperations.mutation.create_triple_flag
        if self.load_test:
            json_body = {"query": bytes(op).decode("utf-8"), "variables": variables}
            return json_body, self.url, self.headers
        data = self.endpoint(op, variables)
        return data

    def add_triple_to_entity(
        self,
        entity_id: str,
        predicate_id: str,
        citation_url: str,
        object_entity_id: str = None,
        object_value: str = None,
        **kwargs,
    ) -> dict:
        """*WARNING: To be deprecated in near future version*

        Add a triple given the subject enity id, predicate id, object id/value, and citation url

        Args:
            entity_id (str): UID of the subject entity
            predicate_id (str): UID of the predicate
            object_entity_id (str): UID of the object entity
            citation_url (str): citation URL

        Returns:
            dict: created triple
        """
        logger.warning("This method will be deprecated")
        pred_object_type = (
            self.predicate_by_id(id=predicate_id)
            .get("data", {})
            .get("predicate", {})
            .get("objectType", "")
        )
        if pred_object_type == "ENTITY":
            assert object_entity_id and not object_value
        elif pred_object_type in ["ANY_URI", "STRING", "INTEGER"]:
            assert object_value and not object_entity_id
        else:
            assert object_value and not object_entity_id
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = AddTripleToEntityByIdOperations.mutation.add_triple_to_entity_by_id
        variables = self.generate_variables(op, params)
        data = self.endpoint(op, variables)
        return data


def get_godel_version() -> str:
    """Grabs the version of Godel from builtin importlib library

    Returns:
        str: version name, unknown if fails to dynamically pull
    """
    try:
        return version("godel")
    except:
        return "unknown"
