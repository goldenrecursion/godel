import pytest

from godel import GoldenAPI

_GOLDAPI = GoldenAPI(url="https://sandbox.dapp.golden.xyz/graphql")

def test_predicates():
    _GOLDAPI.predicates()

def test_templates():
    _GOLDAPI.templates()