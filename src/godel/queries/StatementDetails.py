import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_statement_details():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='StatementDetails', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID))))
    _op_statement = _op.statement(id=sgqlc.types.Variable('id'))
    _op_statement.__fragment__(fragment_triple_widget())
    _op_statement_user = _op_statement.user()
    _op_statement_user.id()
    _op_statement_user.ens_name()
    _op_statement_user.short_address()
    _op_statement.date_created()
    _op_statement_validation_metrics = _op_statement.validation_metrics()
    _op_statement_validation_metrics.accepted()
    _op_statement_validation_metrics.rejected()
    _op_statement_validation_metrics.total()
    return _op


class Query:
    statement_details = query_statement_details()


class Operations:
    query = Query
