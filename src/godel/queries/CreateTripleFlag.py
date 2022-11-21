import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_create_triple_flag():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='CreateTripleFlag', variables=dict(tripleId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), flag=sgqlc.types.Arg(sgqlc.types.non_null(_schema.TripleFlagType))))
    _op_create_triple_flag = _op.create_triple_flag(input={'tripleId': sgqlc.types.Variable('tripleId'), 'flag': sgqlc.types.Variable('flag')})
    _op_create_triple_flag.client_mutation_id()
    return _op


class Mutation:
    create_triple_flag = mutation_create_triple_flag()


class Operations:
    mutation = Mutation
