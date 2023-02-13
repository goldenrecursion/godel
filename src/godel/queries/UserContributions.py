import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_user_contributions():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='UserContributions', variables=dict(userId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None)))
    _op_user = _op.user(id=sgqlc.types.Variable('userId'))
    _op_user_contributions_stats = _op_user.contributions_stats()
    _op_user_contributions_stats.accuracy()
    _op_user_contributions_stats.agreed_with_consensus_count()
    _op_user_contributions_stats.disagreed_with_consensus_count()
    _op_user_contributions_stats.pending_count()
    _op_user_statements = _op_user.statements(first=sgqlc.types.Variable('first'), after=sgqlc.types.Variable('after'), order_by='DATE_CREATED_DESC')
    _op_user_statements.total_count()
    _op_user_statements_page_info = _op_user_statements.page_info()
    _op_user_statements_page_info.has_next_page()
    _op_user_statements_page_info.end_cursor()
    _op_user_statements_edges = _op_user_statements.edges()
    _op_user_statements_edges.cursor()
    _op_user_statements_edges_node = _op_user_statements_edges.node()
    _op_user_statements_edges_node.__fragment__(fragment_triple_widget())
    _op_user_statements_edges_node_ledger_records_by_user_id_and_triple_id = _op_user_statements_edges_node.ledger_records_by_user_id_and_triple_id()
    _op_user_statements_edges_node_ledger_records_by_user_id_and_triple_id_nodes = _op_user_statements_edges_node_ledger_records_by_user_id_and_triple_id.nodes()
    _op_user_statements_edges_node_ledger_records_by_user_id_and_triple_id_nodes.amount()
    _op_user_statements_edges_node_ledger_records_by_user_id_and_triple_id_nodes.type_id()
    return _op


class Query:
    user_contributions = query_user_contributions()


class Operations:
    query = Query
