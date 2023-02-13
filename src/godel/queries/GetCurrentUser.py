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
    _op_current_user.ens_name()
    _op_current_user.balance()
    _op_current_user.token_balance()
    _op_current_user.stake_balance()
    _op_current_user_user_flags = _op_current_user.user_flags()
    _op_current_user_user_flags_nodes = _op_current_user_user_flags.nodes()
    _op_current_user_user_flags_nodes.flag()
    return _op


class Query:
    get_current_user = query_get_current_user()


class Operations:
    query = Query
