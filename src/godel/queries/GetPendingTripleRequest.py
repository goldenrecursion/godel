import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_pending_triple_request():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetPendingTripleRequest')
    _op_pending_triple_request = _op.pending_triple_request()
    _op_pending_triple_request.id()
    _op_pending_triple_request_subject_entity = _op_pending_triple_request.subject_entity()
    _op_pending_triple_request_subject_entity.__fragment__(fragment_entity_detail())
    _op_pending_triple_request_predicate = _op_pending_triple_request.predicate()
    _op_pending_triple_request_predicate.__fragment__(fragment_predicate_details())
    return _op


class Query:
    get_pending_triple_request = query_get_pending_triple_request()


class Operations:
    query = Query
