import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_current_user_contributions():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='CurrentUserContributions', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None), condition=sgqlc.types.Arg(sgqlc.types.non_null(_schema.StatementCondition))))
    _op_current_user = _op.current_user()
    _op_current_user_contributions_stats = _op_current_user.contributions_stats()
    _op_current_user_contributions_stats.accuracy()
    _op_current_user_contributions_stats.agreed_with_consensus_count()
    _op_current_user_contributions_stats.disagreed_with_consensus_count()
    _op_current_user_contributions_stats.pending_count()
    _op_statements = _op.statements(order_by='DATE_CREATED_DESC', after=sgqlc.types.Variable('after'), first=sgqlc.types.Variable('first'), condition=sgqlc.types.Variable('condition'))
    _op_statements.total_count()
    _op_statements_page_info = _op_statements.page_info()
    _op_statements_page_info.end_cursor()
    _op_statements_page_info.has_previous_page()
    _op_statements_page_info.has_next_page()
    _op_statements_edges = _op_statements.edges()
    _op_statements_edges.cursor()
    _op_statements_edges_node = _op_statements_edges.node()
    _op_statements_edges_node.__fragment__(fragment_triple_widget())
    _op_statements_edges_node_ledger_records_by_user_id_and_triple_id = _op_statements_edges_node.ledger_records_by_user_id_and_triple_id()
    _op_statements_edges_node_ledger_records_by_user_id_and_triple_id_nodes = _op_statements_edges_node_ledger_records_by_user_id_and_triple_id.nodes()
    _op_statements_edges_node_ledger_records_by_user_id_and_triple_id_nodes.amount()
    _op_statements_edges_node_ledger_records_by_user_id_and_triple_id_nodes.type_id()
    return _op


class Query:
    current_user_contributions = query_current_user_contributions()


class Operations:
    query = Query
