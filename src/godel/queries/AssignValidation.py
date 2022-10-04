import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_assign_validation():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='AssignValidation')
    _op_assign_validation = _op.assign_validation(input={})
    _op_assign_validation_assigned_validation = _op_assign_validation.assigned_validation()
    _op_assign_validation_assigned_validation.triple_id()
    return _op


class Mutation:
    assign_validation = mutation_assign_validation()


class Operations:
    mutation = Mutation
