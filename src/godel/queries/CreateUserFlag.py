import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_create_user_flag():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='CreateUserFlag', variables=dict(flag=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UserFlagType))))
    _op_create_user_flag = _op.create_user_flag(input={'flag': sgqlc.types.Variable('flag')})
    _op_create_user_flag_user_flag = _op_create_user_flag.user_flag()
    _op_create_user_flag_user_flag.user_id()
    _op_create_user_flag_user_flag.flag()
    _op_create_user_flag_user_flag.created_at()
    return _op


class Mutation:
    create_user_flag = mutation_create_user_flag()


class Operations:
    mutation = Mutation
