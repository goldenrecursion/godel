import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_create_user_report():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='CreateUserReport', variables=dict(userId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), flag=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UserReportFlagType)), comment=sgqlc.types.Arg(_schema.String)))
    _op_create_user_report = _op.create_user_report(input={'userId': sgqlc.types.Variable('userId'), 'flag': sgqlc.types.Variable('flag'), 'comment': sgqlc.types.Variable('comment')})
    _op_create_user_report.client_mutation_id()
    return _op


class Mutation:
    create_user_report = mutation_create_user_report()


class Operations:
    mutation = Mutation
