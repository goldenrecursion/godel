import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_index():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityIndex', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID))))
    _op_entity = _op.entity(id=sgqlc.types.Variable('id'))
    _op_entity.id()
    _op_entity.pathname()
    _op_entity.name()
    _op_entity.description()
    _op_entity.thumbnail()
    _op_entity.golden_id()
    _op_entity_is_a = _op_entity.is_a()
    _op_entity_is_a_nodes = _op_entity_is_a.nodes()
    _op_entity_is_a_nodes.id()
    _op_entity_is_a_nodes.name()
    _op_entity.is_entity_type()
    return _op


class Query:
    entity_index = query_entity_index()


class Operations:
    query = Query
