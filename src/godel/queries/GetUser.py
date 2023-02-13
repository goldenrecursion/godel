import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_user():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetUser', variables=dict(userId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String))))
    _op_user = _op.user(id=sgqlc.types.Variable('userId'))
    _op_user.id()
    return _op


class Query:
    get_user = query_get_user()


class Operations:
    query = Query
