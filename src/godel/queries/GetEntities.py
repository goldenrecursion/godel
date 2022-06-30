from godel.fragments.EntityLink import fragment_entity_link
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_entities():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetEntities')
    _op_entities = _op.entities(first=100)
    _op_entities_nodes = _op_entities.nodes()
    _op_entities_nodes.__fragment__(fragment_entity_link())
    return _op


class Query:
    get_entities = query_get_entities()


class Operations:
    query = Query
