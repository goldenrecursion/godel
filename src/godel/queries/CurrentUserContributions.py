import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_current_user_contributions():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='CurrentUserContributions', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None), condition=sgqlc.types.Arg(sgqlc.types.non_null(_schema.TripleCondition))))
    _op_current_user = _op.current_user()
    _op_current_user_contributions_stats = _op_current_user.contributions_stats()
    _op_current_user_contributions_stats.accuracy()
    _op_current_user_contributions_stats.agreed_with_consensus_count()
    _op_current_user_contributions_stats.disagreed_with_consensus_count()
    _op_current_user_contributions_stats.pending_count()
    _op_triples = _op.triples(order_by='DATE_CREATED_DESC', after=sgqlc.types.Variable('after'), first=sgqlc.types.Variable('first'), condition=sgqlc.types.Variable('condition'))
    _op_triples.total_count()
    _op_triples_page_info = _op_triples.page_info()
    _op_triples_page_info.end_cursor()
    _op_triples_page_info.has_previous_page()
    _op_triples_page_info.has_next_page()
    _op_triples_edges = _op_triples.edges()
    _op_triples_edges.cursor()
    _op_triples_edges_node = _op_triples_edges.node()
    _op_triples_edges_node.__fragment__(fragment_triple_widget())
    return _op


class Query:
    current_user_contributions = query_current_user_contributions()


class Operations:
    query = Query
