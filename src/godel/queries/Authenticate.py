import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_authenticate():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='Authenticate', variables=dict(userId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), signature=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String))))
    _op_authenticate = _op.authenticate(input={'userId': sgqlc.types.Variable('userId'), 'signature': sgqlc.types.Variable('signature')})
    _op_authenticate.jwt_token()
    return _op


class Mutation:
    authenticate = mutation_authenticate()


class Operations:
    mutation = Mutation
