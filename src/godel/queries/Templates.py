import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_templates():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='Templates')
    _op_templates = _op.templates()
    _op_templates_nodes = _op_templates.nodes()
    _op_templates_nodes.id()
    _op_templates_nodes_entity = _op_templates_nodes.entity()
    _op_templates_nodes_entity.id()
    _op_templates_nodes_entity.name()
    _op_templates_nodes_template_predicates = _op_templates_nodes.template_predicates()
    _op_templates_nodes_template_predicates_nodes = _op_templates_nodes_template_predicates.nodes()
    _op_templates_nodes_template_predicates_nodes_predicate = _op_templates_nodes_template_predicates_nodes.predicate()
    _op_templates_nodes_template_predicates_nodes_predicate.id()
    _op_templates_nodes_template_predicates_nodes_predicate.name()
    _op_templates_nodes_template_predicates_nodes_predicate.object_type()
    return _op


class Query:
    templates = query_templates()


class Operations:
    query = Query
