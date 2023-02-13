import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_bounties():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='Bounties', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None)))
    _op_bounties = _op.bounties(after=sgqlc.types.Variable('after'), first=sgqlc.types.Variable('first'), order_by=('VIEWER_ASC',), condition={'dateCompleted': None})
    _op_bounties.total_count()
    _op_bounties_page_info = _op_bounties.page_info()
    _op_bounties_page_info.end_cursor()
    _op_bounties_page_info.has_previous_page()
    _op_bounties_page_info.has_next_page()
    _op_bounties_nodes = _op_bounties.nodes()
    _op_bounties_nodes.id()
    _op_bounties_nodes.date_created()
    _op_bounties_nodes.triple_reward()
    _op_bounties_nodes_subject_entity = _op_bounties_nodes.subject_entity()
    _op_bounties_nodes_subject_entity.__fragment__(fragment_entity_link())
    _op_bounties_nodes_predicate = _op_bounties_nodes.predicate()
    _op_bounties_nodes_predicate.id()
    _op_bounties_nodes_predicate.name()
    _op_bounties_nodes_predicate.description()
    _op_bounties_nodes_predicate.label()
    _op_bounties_nodes_predicate.object_type()
    _op_bounties_nodes_predicate.show_in_infobox()
    return _op


class Query:
    bounties = query_bounties()


class Operations:
    query = Query
