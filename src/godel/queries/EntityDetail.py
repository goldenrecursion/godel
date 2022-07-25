from godel.fragments.PredicateDetails import fragment_predicate_details
from godel.fragments.EntityDetail import fragment_entity_detail
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_detail():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityDetail', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID))))
    _op_entity = _op.entity(id=sgqlc.types.Variable('id'))
    _op_entity.__fragment__(fragment_entity_detail())
    _op_templates = _op.templates(order_by='RANK_ASC')
    _op_templates_nodes = _op_templates.nodes()
    _op_templates_nodes.entity_id()
    _op_templates_nodes_template_predicates = _op_templates_nodes.template_predicates(order_by='RANK_ASC')
    _op_templates_nodes_template_predicates_nodes = _op_templates_nodes_template_predicates.nodes()
    _op_templates_nodes_template_predicates_nodes_predicate = _op_templates_nodes_template_predicates_nodes.predicate()
    _op_templates_nodes_template_predicates_nodes_predicate.__fragment__(fragment_predicate_details())
    return _op


class Query:
    entity_detail = query_entity_detail()


class Operations:
    query = Query
