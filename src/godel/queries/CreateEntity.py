from godel.fragments.EntityDetail import fragment_entity_detail
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_create_entity():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='CreateEntity', variables=dict(input=sgqlc.types.Arg(sgqlc.types.non_null(_schema.CreateEntityInput))))
    _op_create_entity = _op.create_entity(input=sgqlc.types.Variable('input'))
    _op_create_entity_entity = _op_create_entity.entity()
    _op_create_entity_entity.__fragment__(fragment_entity_detail())
    return _op


class Mutation:
    create_entity = mutation_create_entity()


class Operations:
    mutation = Mutation
