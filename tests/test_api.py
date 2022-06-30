import pytest

from godel import GoldenAPI

_GAPI = GoldenAPI()

# TODO: Use test wallet
@ pytest.mark.skip(reason="Need test wallet to sign")
def test_authenticate():
    _GAPI.authenticate()

@ pytest.mark.skip(reason="Requires connection to api")
def test_predicate():
    _GAPI.predicate(name="CEO")

