import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_search():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntitySearch', variables=dict(name=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), first=sgqlc.types.Arg(_schema.Int, default=20)))
    _op_entity_by_name = _op.entity_by_name(entity_name=sgqlc.types.Variable('name'), first=sgqlc.types.Variable('first'))
    _op_entity_by_name_nodes = _op_entity_by_name.nodes()
    _op_entity_by_name_nodes.id()
    _op_entity_by_name_nodes.name()
    _op_entity_by_name_nodes.description()
    _op_entity_by_name_nodes.thumbnail()
    _op_entity_by_name_nodes.golden_id()
    _op_entity_by_name_nodes.pathname()
    return _op


class Query:
    entity_search = query_entity_search()


class Operations:
    query = Query
