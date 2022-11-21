import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_type():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityType', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID))))
    _op_entity = _op.entity(id=sgqlc.types.Variable('id'))
    _op_entity.id()
    _op_entity.name()
    _op_entity.is_entity_type()
    return _op


class Query:
    entity_type = query_entity_type()


class Operations:
    query = Query
