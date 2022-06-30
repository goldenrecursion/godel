from dapp_api.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import dapp_api.schema

_schema = dapp_api.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_triple_for_validation():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetTripleForValidation')
    _op_unvalidated_triple = _op.unvalidated_triple()
    _op_unvalidated_triple__as__Statement = _op_unvalidated_triple.__as__(_schema.Statement)
    _op_unvalidated_triple__as__Statement.__fragment__(fragment_triple_widget())
    _op_unvalidated_triple__as__Statement_subject = _op_unvalidated_triple__as__Statement.subject()
    _op_unvalidated_triple__as__Statement_subject.description()
    _op_unvalidated_triple__as__Statement_subject.thumbnail()
    _op_unvalidated_triple__as__Statement_subject.website()
    _op_unvalidated_triple__as__Statement_subject.golden_id()
    _op_unvalidated_triple__as__Statement_object_entity = _op_unvalidated_triple__as__Statement.object_entity()
    _op_unvalidated_triple__as__Statement_object_entity.description()
    _op_unvalidated_triple__as__Statement_object_entity.thumbnail()
    _op_unvalidated_triple__as__Statement_object_entity.website()
    _op_unvalidated_triple__as__Statement_object_entity.golden_id()
    return _op


class Query:
    get_triple_for_validation = query_get_triple_for_validation()


class Operations:
    query = Query
