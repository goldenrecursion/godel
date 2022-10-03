import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_golden_redirect():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityGoldenRedirect', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID))))
    _op_entity = _op.entity(id=sgqlc.types.Variable('id'))
    _op_entity.golden_id()
    return _op


class Query:
    entity_golden_redirect = query_entity_golden_redirect()


class Operations:
    query = Query
