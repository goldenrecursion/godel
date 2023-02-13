import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_statement_validations():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='StatementValidations', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None), orderBy=sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(_schema.ValidationsOrderBy)), default=('CREATED_AT_DESC', 'PRIMARY_KEY_ASC')), condition=sgqlc.types.Arg(sgqlc.types.non_null(_schema.ValidationCondition))))
    _op_statement = _op.statement(id=sgqlc.types.Variable('id'))
    _op_statement_validations = _op_statement.validations(order_by=sgqlc.types.Variable('orderBy'), after=sgqlc.types.Variable('after'), first=sgqlc.types.Variable('first'), condition=sgqlc.types.Variable('condition'))
    _op_statement_validations.total_count()
    _op_statement_validations_page_info = _op_statement_validations.page_info()
    _op_statement_validations_page_info.has_previous_page()
    _op_statement_validations_page_info.has_next_page()
    _op_statement_validations_page_info.end_cursor()
    _op_statement_validations_nodes = _op_statement_validations.nodes()
    _op_statement_validations_nodes.id()
    _op_statement_validations_nodes.created_at()
    _op_statement_validations_nodes.validation_type()
    _op_statement_validations_nodes_user = _op_statement_validations_nodes.user()
    _op_statement_validations_nodes_user.id()
    _op_statement_validations_nodes_user.ens_name()
    _op_statement_validations_nodes.triple_id()
    return _op


class Query:
    statement_validations = query_statement_validations()


class Operations:
    query = Query
