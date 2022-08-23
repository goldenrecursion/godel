import logging
import os
from importlib_metadata import version

import sys
from typing import List, Union
from platform import platform

import requests
from sgqlc.endpoint.http import HTTPEndpoint
from sgqlc.operation import Operation

from godel import schema
from godel.queries.AddTripleToEntityById import (
    Operations as AddTripleToEntityByIdOperations,
)
from godel.queries.Authenticate import Operations as AuthenticateOperations
from godel.queries.CreateEntity import Operations as CreateEntityOperations
from godel.queries.CreateValidation import Operations as CreateValidationOperations
from godel.queries.CreateStatement import Operations as CreateStatementOperations

# from godel.queries.CurrentUserBlockchainData import Operations as CurrentUserBlockchainDataOperations
from godel.queries.CurrentUserValidations import (
    Operations as CurrentUserValidationsOperations,
)
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

logger = logging.getLogger(__name__)


class GoldenAPI:
    def __init__(
        self, url: str = "https://dapp.golden.xyz/graphql", jwt_token: str = ""
    ):
        self.url = url
        self.jwt_token = jwt_token
        self.headers = {}
        self.headers[
            "User-Agent"
        ] = f"golden sdk v-{get_godel_version()}_{platform().lower()}"
        self.headers.update(
            {"Authorization": f"Bearer {jwt_token}"} if jwt_token else {}
        )
        self.endpoint = HTTPEndpoint(self.url, self.headers)
        self.predicates_cache = self.predicates()
        self.templates_cache = self.templates()

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
        self.endpoint = HTTPEndpoint(self.url, self.headers)

    def query(self, query: str = "", headers: dict = {}):
        """Generic method to query graphql endpoint"""
        r = requests.post(self.url, json={"query": query}, headers=headers)
        print(r.status_code)
        if r.status_code == 400:
            logger.warning(r)
        return r.json()

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

    # Entities

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
        data = self.endpoint(op, variables)
        return data

    def entity_detail(self, id: str, **kwargs) -> dict:
        """Retrieve entity details, includes rich template and statement values

        Args:
            id (str): id of entity to retrieve

        Returns:
            dict: Entity with details
        """
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = EntityDetailOperations.query.entity_detail
        variables = self.generate_variables(op, params)
        data = self.endpoint(op, variables)
        return data

    def entity_with_triples(self, id: str) -> dict:
        """Retrieve entity with both entity to value triples and entity to entity triples

        Args:
            entity_id (str): id of entity to retrieve

        Returns:
            dict: Entity with triples
        """

        query = f"""query MyQuery {{
              entity(id: "{id}") {{
              id
                statementsBySubjectId {{
                  nodes {{
                    id
                    objectEntityId
                    objectValue
                    predicate {{
                      name
                    }}
                    objectEntity {{
                      name
                    }}
                  }}
                }}
              }}
            }}"""
        variables = {}
        data = self.endpoint(query, variables)
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
                }
              }
            }
        }"""
        variables = {}
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

    def unvalidated_triple(self) -> dict:
        """Get all templates

        Returns:
            dict: List of available templates
        """
        query = """query MyQuery {
            unvalidatedTriple {
              ... on Statement {
                id
                citationsByTripleId {
                     nodes {
                         url
                     }
                 }
                dateCreated
                objectEntityId
                objectValue
                subjectId
                userId
                predicateId
              }
            }
        }"""
        variables = {}
        data = self.endpoint(query, variables)
        return data

    ###############
    ## Mutations ##
    ###############

    # Entity Submissions
    def create_entity(self, create_entity_input: schema.CreateEntityInput, **kwargs):
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

        input = create_entity_input.__to_json_value__()
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = CreateEntityOperations.mutation.create_entity
        variables = self.generate_variables(op, params)
        data = self.endpoint(op, variables)
        return data

    # Triples Submissions

    def create_statement(
        self, create_statement_input: schema.CreateStatementInput, **kwargs
    ):
        """Create statement triple given the statement input combinations of subject entity id, predicate id, object id/value, and citation url

        Args:
            input (str): Create statement record input

        Returns:
            dict: created statement
        """
        input = create_statement_input.__to_json_value__()
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = CreateStatementOperations.mutation.create_statement
        variables = self.generate_variables(op, params)
        data = self.endpoint(op, variables)
        return data

    # Validation Submissions

    def create_validation(self, triple_id: str, validation_type: str, **kwargs) -> dict:
        params = locals()
        params.pop("kwargs")
        params.pop("self")
        params.update(kwargs)
        op = CreateValidationOperations.mutation.create_validation
        variables = self.generate_variables(op, params)
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
        """ *WARNING: To be deprecated in near future version*
        
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
