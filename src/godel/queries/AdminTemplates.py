import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def fragment_predicate_fields():
    _frag = sgqlc.operation.Fragment(_schema.Predicate, 'predicateFields')
    _frag.id()
    _frag.name()
    _frag.description()
    _frag.label()
    _frag.object_type()
    _frag.show_in_infobox()
    return _frag


class Fragment:
    predicate_fields = fragment_predicate_fields()


def query_admin_templates():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='AdminTemplates')
    _op_templates = _op.templates()
    _op_templates_nodes = _op_templates.nodes()
    _op_templates_nodes.id()
    _op_templates_nodes_entity = _op_templates_nodes.entity()
    _op_templates_nodes_entity.id()
    _op_templates_nodes_entity.name()
    _op_templates_nodes_entity.pathname()
    _op_templates_nodes_template_predicates = _op_templates_nodes.template_predicates(order_by='RANK_ASC')
    _op_templates_nodes_template_predicates_nodes = _op_templates_nodes_template_predicates.nodes()
    _op_templates_nodes_template_predicates_nodes_predicate = _op_templates_nodes_template_predicates_nodes.predicate()
    _op_templates_nodes_template_predicates_nodes_predicate.__fragment__(fragment_predicate_fields())
    _op_predicates = _op.predicates(order_by='NAME_ASC')
    _op_predicates_nodes = _op_predicates.nodes()
    _op_predicates_nodes.__fragment__(fragment_predicate_fields())
    return _op


class Query:
    admin_templates = query_admin_templates()


class Operations:
    fragment = Fragment
    query = Query
