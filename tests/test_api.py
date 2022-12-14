import pytest
import os
import random

import pandas as pd
from godel import GoldenAPI
from godel.schema import (
    CreateEntityInput,
    StatementInputRecordInput,
    CreateStatementInput,
    StatementInputRecordInput,
    ValidationType,
)

_GOLDAPI = GoldenAPI(url="https://sandbox.dapp.golden.xyz/graphql")
_WALLET_A = os.getenv("WALLET_A")
_WALLET_PK = os.getenv("WALLET_PK")


def test_predicates():
    _GOLDAPI.predicates()


def test_templates():
    _GOLDAPI.templates()

@pytest.mark.skip(reason="Needs config")
def test_auntheticate():
    # Retrieve one-off nonce from GraphQL API
    message_response = _GOLDAPI.get_authentication_message(user_id=_WALLET_A)
    message_response

    # Sign and verify nonce with your wallet's private key (KEEP THIS SECURE)
    from web3.auto import w3
    from eth_account.messages import encode_defunct

    message_string = message_response["data"]["getAuthenticationMessage"]["string"]
    message = encode_defunct(text=message_string)
    signed_message = w3.eth.account.sign_message(message, private_key=_WALLET_PK)
    signature = signed_message.signature.hex()

    # Authenticate with Golden's API and you'll recieve a jwt bearer token
    auth_response = _GOLDAPI.authenticate(user_id=_WALLET_A, signature=signature)

    jwt_token = auth_response["data"]["authenticate"]["jwtToken"]

    # Set JWT token to verify your wallet/role and unlock permissions to the rest of the API
    _GOLDAPI.set_jwt_token(jwt_token=jwt_token)

    global _JWT_TOKEN
    _JWT_TOKEN = jwt_token

@pytest.mark.skip(reason="Needs config")
def test_create_entity():
    # Test connection with search
    search_results = _GOLDAPI.entity_search(name="Miles")
    search_results_df = pd.DataFrame(search_results["data"]["entityByName"]["nodes"])

    predicates = {}
    for p in _GOLDAPI.predicates()["data"]["predicates"]["edges"]:
        p = p["node"]
        predicates[p["name"]] = {"id": p["id"], "objectType": p["objectType"]}
    predicates_df = pd.DataFrame(predicates).transpose()

    templates = {}
    for t in _GOLDAPI.templates()["data"]["templates"]["edges"]:
        t = t["node"]
        templates[t["entity"]["name"]] = {
            "id": t["id"],
            "entityId": t["entityId"],
            "entityDescription": t["entity"]["description"],
        }
    templates_df = pd.DataFrame(templates).transpose()

    templates = {}
    for t in _GOLDAPI.templates()["data"]["templates"]["edges"]:
        t = t["node"]
        templates[t["entity"]["name"]] = {
            "id": t["id"],
            "entityId": t["entityId"],
            "entityDescription": t["entity"]["description"],
        }
    templates_df = pd.DataFrame(templates).transpose()

    name = "John Doe"
    is_a = "0c4e6054-5fd8-48a8-817c-f6611278f755"  # Person Template Entity Id
    citation_urls = ["https://golden.com/wiki/johndoe"]

    # Create triples inputs
    statements = []

    # Add Template
    statements.append(
        StatementInputRecordInput(
            predicate_id=predicates["Is a"]["id"],
            object_entity_id=is_a,
            citation_urls=citation_urls,
            qualifiers=[],
        )
    )

    # Add Name
    statements.append(
        StatementInputRecordInput(
            predicate_id=predicates["Name"]["id"],
            object_value=name,
            citation_urls=citation_urls,
            qualifiers=[],
        )
    )

    # Add Website
    statements.append(
        StatementInputRecordInput(
            predicate_id=predicates["Website"]["id"],
            object_value="https://johndoe.com",
            citation_urls=citation_urls,
            qualifiers=[],
        )
    )

    # Create Entity Input
    create_entity_input = CreateEntityInput(statements=statements)
    create_entity_input.__to_json_value__()

    data = _GOLDAPI.create_entity(create_entity_input=create_entity_input)
    data["data"]["createEntity"]
    assert "errors" not in data


@pytest.mark.skip(reason="Needs config")
def test_create_triple():
    # Test with search
    search_results = _GOLDAPI.entity_search(name="Miles")
    search_results_df = pd.DataFrame(search_results["data"]["entityByName"]["nodes"])
    search_results_df

    predicates = {}
    for p in _GOLDAPI.predicates()["data"]["predicates"]["edges"]:
        p = p["node"]
        predicates[p["name"]] = {"id": p["id"], "objectType": p["objectType"]}
    predicates_df = pd.DataFrame(predicates).transpose()

    # Triple data
    subject_id = search_results_df["id"][0]  # Miles Wolff
    predicate_id = "0efd0441-1ffc-4e30-8806-e58c434770c8"  # Email Address
    # Randomized, very small chance of collision within 24 hour sandbox period
    object_value = f"{random.randint(0,1000000000)}@example.com"

    # Create statement input API
    create_statement_input = CreateStatementInput(
        subject_id=subject_id,
        predicate_id=predicate_id,
        object_value=object_value,
        citation_urls=["https://golden.com"],
    )

    data = _GOLDAPI.create_statement(create_statement_input=create_statement_input)
    assert "errors" not in data

@pytest.mark.skip(reason="Needs config")
def test_create_verification():
    # Get an unvalidated triple
    data = _GOLDAPI.unvalidated_triple()["data"]
    unvalidated_triple = data["triple"]
    # Create validation with the triple id and your validation type
    triple_id = unvalidated_triple["id"]
    validation_type = "REJECTED"
    # Create Validation
    data = _GOLDAPI.create_validation(
        triple_id=triple_id, validation_type=validation_type
    )
    assert "errors" not in data
