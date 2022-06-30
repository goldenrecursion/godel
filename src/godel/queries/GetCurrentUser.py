import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_current_user():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetCurrentUser')
    _op_current_user = _op.current_user()
    _op_current_user.id()
    _op_current_user.short_address()
    _op_current_user.nonce()
    _op_current_user.balance()
    _op_current_user.token_balance()
    _op_current_user.stake_balance()
    return _op


class Query:
    get_current_user = query_get_current_user()


class Operations:
    query = Query
