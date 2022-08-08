from godel.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_create_statement():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='CreateStatement', variables=dict(input=sgqlc.types.Arg(sgqlc.types.non_null(_schema.CreateStatementInput))))
    _op_create_statement = _op.create_statement(input=sgqlc.types.Variable('input'))
    _op_create_statement_statement = _op_create_statement.statement()
    _op_create_statement_statement.__fragment__(fragment_triple_widget())
    return _op


class Mutation:
    create_statement = mutation_create_statement()


class Operations:
    mutation = Mutation
