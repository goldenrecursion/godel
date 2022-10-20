from godel.fragments.TripleWidget import fragment_triple_widget
from godel.fragments.EntitySummary import fragment_entity_summary
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_triple_for_validation():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetTripleForValidation', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID))))
    _op_triple = _op.triple(id=sgqlc.types.Variable('id'))
    _op_triple__as__Statement = _op_triple.__as__(_schema.Statement)
    _op_triple__as__Statement.__fragment__(fragment_triple_widget())
    _op_triple__as__Statement_subject = _op_triple__as__Statement.subject()
    _op_triple__as__Statement_subject.__fragment__(fragment_entity_summary())
    _op_triple__as__Statement_object_entity = _op_triple__as__Statement.object_entity()
    _op_triple__as__Statement_object_entity.__fragment__(fragment_entity_summary())
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
