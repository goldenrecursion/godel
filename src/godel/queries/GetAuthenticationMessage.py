import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_get_authentication_message():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='GetAuthenticationMessage', variables=dict(userId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String))))
    _op_get_authentication_message = _op.get_authentication_message(input={'userId': sgqlc.types.Variable('userId')})
    _op_get_authentication_message.string()
    return _op


class Mutation:
    get_authentication_message = mutation_get_authentication_message()


class Operations:
    mutation = Mutation
