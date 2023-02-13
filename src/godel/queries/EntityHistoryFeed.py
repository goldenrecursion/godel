import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_history_feed():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityHistoryFeed', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), first=sgqlc.types.Arg(_schema.Int, default=20), offset=sgqlc.types.Arg(_schema.Int), orderBy=sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(_schema.EntityHistoriesOrderBy)), default=('TIMESTAMP_DESC', 'TRIPLE_ID_ASC'))))
    _op_entity = _op.entity(id=sgqlc.types.Variable('id'))
    _op_entity.id()
    _op_entity_history = _op_entity.history(order_by=sgqlc.types.Variable('orderBy'), offset=sgqlc.types.Variable('offset'), first=sgqlc.types.Variable('first'))
    _op_entity_history.total_count()
    _op_entity_history_page_info = _op_entity_history.page_info()
    _op_entity_history_page_info.has_previous_page()
    _op_entity_history_page_info.has_next_page()
    _op_entity_history_nodes = _op_entity_history.nodes()
    _op_entity_history_nodes.event()
    _op_entity_history_nodes.timestamp()
    _op_entity_history_nodes_triple = _op_entity_history_nodes.triple()
    _op_entity_history_nodes_triple__as__Statement = _op_entity_history_nodes_triple.__as__(_schema.Statement)
    _op_entity_history_nodes_triple__as__Statement.id()
    _op_entity_history_nodes_triple__as__Statement.date_accepted()
    _op_entity_history_nodes_triple__as__Statement.date_rejected()
    _op_entity_history_nodes_triple__as__Statement.user_id()
    _op_entity_history_nodes_triple__as__Statement.validation_status()
    _op_entity_history_nodes_triple__as__Statement_subject = _op_entity_history_nodes_triple__as__Statement.subject()
    _op_entity_history_nodes_triple__as__Statement_subject.__fragment__(fragment_entity_link())
    _op_entity_history_nodes_triple__as__Statement_predicate = _op_entity_history_nodes_triple__as__Statement.predicate()
    _op_entity_history_nodes_triple__as__Statement_predicate.id()
    _op_entity_history_nodes_triple__as__Statement_predicate.name()
    _op_entity_history_nodes_triple__as__Statement_predicate.description()
    _op_entity_history_nodes_triple__as__Statement_predicate.label()
    _op_entity_history_nodes_triple__as__Statement_predicate.object_type()
    _op_entity_history_nodes_triple__as__Statement_predicate.show_in_infobox()
    _op_entity_history_nodes_triple__as__Statement.object_value()
    _op_entity_history_nodes_triple__as__Statement_object_entity = _op_entity_history_nodes_triple__as__Statement.object_entity()
    _op_entity_history_nodes_triple__as__Statement_object_entity.__fragment__(fragment_entity_link())
    return _op


class Query:
    entity_history_feed = query_entity_history_feed()


class Operations:
    query = Query
