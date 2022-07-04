from dapp_api.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import dapp_api.schema

_schema = dapp_api.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def fragment_entity_detail():
    _frag = sgqlc.operation.Fragment(_schema.Entity, 'EntityDetail')
    _frag.id()
    _frag.name()
    _frag.description()
    _frag.thumbnail()
    _frag_is_a = _frag.is_a()
    _frag_is_a_nodes = _frag_is_a.nodes()
    _frag_is_a_nodes.name()
    _frag_statements_by_subject_id = _frag.statements_by_subject_id()
    _frag_statements_by_subject_id_nodes = _frag_statements_by_subject_id.nodes()
    _frag_statements_by_subject_id_nodes.__fragment__(fragment_triple_widget())
    _frag_statements_by_subject_id_nodes.date_rejected()
    return _frag


class Fragment:
    entity_detail = fragment_entity_detail()


class Operations:
    fragment = Fragment
