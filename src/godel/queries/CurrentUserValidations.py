from godel.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_current_user_validations():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='CurrentUserValidations', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None), condition=sgqlc.types.Arg(sgqlc.types.non_null(_schema.ValidationCondition))))
    _op_current_user = _op.current_user()
    _op_current_user_stats = _op_current_user.stats()
    _op_current_user_stats.accuracy()
    _op_current_user_stats.agreed_with_consensus_count()
    _op_current_user_stats.disagreed_with_consensus_count()
    _op_current_user_stats.pending_count()
    _op_current_user_validations = _op_current_user.validations(order_by='CREATED_AT_DESC', after=sgqlc.types.Variable('after'), first=sgqlc.types.Variable('first'), condition=sgqlc.types.Variable('condition'))
    _op_current_user_validations.total_count()
    _op_current_user_validations_page_info = _op_current_user_validations.page_info()
    _op_current_user_validations_page_info.end_cursor()
    _op_current_user_validations_page_info.has_previous_page()
    _op_current_user_validations_page_info.has_next_page()
    _op_current_user_validations_edges = _op_current_user_validations.edges()
    _op_current_user_validations_edges.cursor()
    _op_current_user_validations_edges_node = _op_current_user_validations_edges.node()
    _op_current_user_validations_edges_node.id()
    _op_current_user_validations_edges_node.created_at()
    _op_current_user_validations_edges_node.validation_type()
    _op_current_user_validations_edges_node_triple = _op_current_user_validations_edges_node.triple()
    _op_current_user_validations_edges_node_triple.__fragment__(fragment_triple_widget())
    return _op


class Query:
    current_user_validations = query_current_user_validations()


class Operations:
    query = Query
