import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_profile_index():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='ProfileIndex')
    _op_current_user = _op.current_user()
    _op_current_user.ens_name()
    _op_current_user_user_flags = _op_current_user.user_flags()
    _op_current_user_user_flags_nodes = _op_current_user_user_flags.nodes()
    _op_current_user_user_flags_nodes.flag()
    return _op


class Query:
    profile_index = query_profile_index()


class Operations:
    query = Query
