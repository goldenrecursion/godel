import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_user_verifications():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='UserVerifications', variables=dict(userId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None)))
    _op_user = _op.user(id=sgqlc.types.Variable('userId'))
    _op_user_stats = _op_user.stats()
    _op_user_stats.accuracy()
    _op_user_stats.agreed_with_consensus_count()
    _op_user_stats.disagreed_with_consensus_count()
    _op_user_stats.pending_count()
    _op_user_validation_activity = _op_user.validation_activity(first=sgqlc.types.Variable('first'), after=sgqlc.types.Variable('after'), order_by=('CREATED_AT_DESC', 'PRIMARY_KEY_ASC'))
    _op_user_validation_activity.total_count()
    _op_user_validation_activity_page_info = _op_user_validation_activity.page_info()
    _op_user_validation_activity_page_info.has_next_page()
    _op_user_validation_activity_page_info.end_cursor()
    _op_user_validation_activity_page_info.has_previous_page()
    _op_user_validation_activity_nodes = _op_user_validation_activity.nodes()
    _op_user_validation_activity_nodes.id()
    _op_user_validation_activity_nodes.created_at()
    _op_user_validation_activity_nodes.reason()
    _op_user_validation_activity_nodes_triple = _op_user_validation_activity_nodes.triple()
    _op_user_validation_activity_nodes_triple.__fragment__(fragment_triple_widget())
    _op_user_validation_activity_nodes.validation_status()
    _op_user_validation_activity_nodes.validation_type()
    _op_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id = _op_user_validation_activity_nodes.ledger_records_by_user_id_and_triple_id()
    _op_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes = _op_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id.nodes()
    _op_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes.user_id()
    _op_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes.amount()
    _op_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes.type_id()
    return _op


class Query:
    user_verifications = query_user_verifications()


class Operations:
    query = Query
