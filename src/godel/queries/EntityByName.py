from godel.fragments.EntityDetail import fragment_entity_detail
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_by_name():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityByName', variables=dict(name=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), first=sgqlc.types.Arg(_schema.Int, default=10)))
    _op_entity_by_name = _op.entity_by_name(entity_name=sgqlc.types.Variable('name'), first=sgqlc.types.Variable('first'))
    _op_entity_by_name_edges = _op_entity_by_name.edges()
    _op_entity_by_name_edges_node = _op_entity_by_name_edges.node()
    _op_entity_by_name_edges_node.id()
    _op_entity_by_name_edges_node.__fragment__(fragment_entity_detail())
    return _op


class Query:
    entity_by_name = query_entity_by_name()


class Operations:
    query = Query
