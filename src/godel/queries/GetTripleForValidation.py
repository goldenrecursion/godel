from godel.fragments.TripleWidget import fragment_triple_widget
from godel.fragments.EntityDetail import fragment_entity_detail
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_triple_for_validation():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetTripleForValidation')
    _op_unvalidated_triple = _op.unvalidated_triple()
    _op_unvalidated_triple__as__Statement = _op_unvalidated_triple.__as__(_schema.Statement)
    _op_unvalidated_triple__as__Statement.__fragment__(fragment_triple_widget())
    _op_unvalidated_triple__as__Statement_subject = _op_unvalidated_triple__as__Statement.subject()
    _op_unvalidated_triple__as__Statement_subject.__fragment__(fragment_entity_detail())
    _op_unvalidated_triple__as__Statement_object_entity = _op_unvalidated_triple__as__Statement.object_entity()
    _op_unvalidated_triple__as__Statement_object_entity.__fragment__(fragment_entity_detail())
    _op_current_user = _op.current_user()
    _op_current_user.remaining_skips()
    _op_current_user_user_flags = _op_current_user.user_flags()
    _op_current_user_user_flags_nodes = _op_current_user_user_flags.nodes()
    _op_current_user_user_flags_nodes.flag()
    return _op


class Query:
    get_triple_for_validation = query_get_triple_for_validation()


class Operations:
    query = Query
