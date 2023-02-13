import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_current_user_validation_activity():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='CurrentUserValidationActivity', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None), condition=sgqlc.types.Arg(sgqlc.types.non_null(_schema.ValidationActivityCondition))))
    _op_current_user_validation_activity = _op.current_user_validation_activity(order_by=('CREATED_AT_DESC', 'PRIMARY_KEY_ASC'), after=sgqlc.types.Variable('after'), first=sgqlc.types.Variable('first'), condition=sgqlc.types.Variable('condition'))
    _op_current_user_validation_activity.total_count()
    _op_current_user_validation_activity_page_info = _op_current_user_validation_activity.page_info()
    _op_current_user_validation_activity_page_info.end_cursor()
    _op_current_user_validation_activity_page_info.has_previous_page()
    _op_current_user_validation_activity_page_info.has_next_page()
    _op_current_user_validation_activity_nodes = _op_current_user_validation_activity.nodes()
    _op_current_user_validation_activity_nodes.id()
    _op_current_user_validation_activity_nodes.created_at()
    _op_current_user_validation_activity_nodes.reason()
    _op_current_user_validation_activity_nodes_triple = _op_current_user_validation_activity_nodes.triple()
    _op_current_user_validation_activity_nodes_triple.__fragment__(fragment_triple_widget())
    _op_current_user_validation_activity_nodes.validation_status()
    _op_current_user_validation_activity_nodes.validation_type()
    _op_current_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id = _op_current_user_validation_activity_nodes.ledger_records_by_user_id_and_triple_id()
    _op_current_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes = _op_current_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id.nodes()
    _op_current_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes.user_id()
    _op_current_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes.amount()
    _op_current_user_validation_activity_nodes_ledger_records_by_user_id_and_triple_id_nodes.type_id()
    _op_current_user = _op.current_user()
    _op_current_user_stats = _op_current_user.stats()
    _op_current_user_stats.accuracy()
    _op_current_user_stats.agreed_with_consensus_count()
    _op_current_user_stats.disagreed_with_consensus_count()
    _op_current_user_stats.pending_count()
    return _op


class Query:
    current_user_validation_activity = query_current_user_validation_activity()


class Operations:
    query = Query
