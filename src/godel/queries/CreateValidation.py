import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_create_validation():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='CreateValidation', variables=dict(tripleId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), validationType=sgqlc.types.Arg(sgqlc.types.non_null(_schema.ValidationType))))
    _op_create_validation = _op.create_validation(input={'tripleId': sgqlc.types.Variable('tripleId'), 'validationType': sgqlc.types.Variable('validationType')})
    _op_create_validation_validation = _op_create_validation.validation()
    _op_create_validation_validation.ground_truth_violation_reason()
    return _op


class Mutation:
    create_validation = mutation_create_validation()


class Operations:
    mutation = Mutation
