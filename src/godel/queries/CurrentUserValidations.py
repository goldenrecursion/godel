from dapp_api.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import dapp_api.schema

_schema = dapp_api.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_current_user_validations():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='CurrentUserValidations')
    _op_current_user = _op.current_user()
    _op_current_user_validations = _op_current_user.validations()
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
