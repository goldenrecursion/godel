from godel.fragments.EntityLink import fragment_entity_link
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def fragment_triple_widget():
    _frag = sgqlc.operation.Fragment(_schema.Triple, 'TripleWidget')
    _frag__as__Statement = _frag.__as__(_schema.Statement)
    _frag__as__Statement.id()
    _frag__as__Statement.date_accepted()
    _frag__as__Statement.date_rejected()
    _frag__as__Statement.user_id()
    _frag__as__Statement.validation_status()
    _frag__as__Statement_subject = _frag__as__Statement.subject()
    _frag__as__Statement_subject.id()
    _frag__as__Statement_subject.pathname()
    _frag__as__Statement_subject.name()
    _frag__as__Statement_subject.thumbnail()
    _frag__as__Statement_predicate = _frag__as__Statement.predicate()
    _frag__as__Statement_predicate.id()
    _frag__as__Statement_predicate.name()
    _frag__as__Statement_predicate.description()
    _frag__as__Statement_predicate.label()
    _frag__as__Statement_predicate.object_type()
    _frag__as__Statement_predicate.show_in_infobox()
    _frag__as__Statement.object_value()
    _frag__as__Statement_object_entity = _frag__as__Statement.object_entity()
    _frag__as__Statement_object_entity.id()
    _frag__as__Statement_object_entity.pathname()
    _frag__as__Statement_object_entity.name()
    _frag__as__Statement_object_entity.thumbnail()
    _frag__as__Statement_citations_by_triple_id = _frag__as__Statement.citations_by_triple_id()
    _frag__as__Statement_citations_by_triple_id_nodes = _frag__as__Statement_citations_by_triple_id.nodes()
    _frag__as__Statement_citations_by_triple_id_nodes.url()
    _frag__as__Statement_qualifiers_by_subject_id = _frag__as__Statement.qualifiers_by_subject_id()
    _frag__as__Statement_qualifiers_by_subject_id_nodes = _frag__as__Statement_qualifiers_by_subject_id.nodes()
    _frag__as__Statement_qualifiers_by_subject_id_nodes.id()
    _frag__as__Statement_qualifiers_by_subject_id_nodes_predicate = _frag__as__Statement_qualifiers_by_subject_id_nodes.predicate()
    _frag__as__Statement_qualifiers_by_subject_id_nodes_predicate.name()
    _frag__as__Statement_qualifiers_by_subject_id_nodes.object_value()
    return _frag


class Fragment:
    triple_widget = fragment_triple_widget()


class Operations:
    fragment = Fragment
