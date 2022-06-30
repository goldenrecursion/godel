from godel.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_add_triple_to_entity_by_id():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='AddTripleToEntityById', variables=dict(entityId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), predicateId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), objectValue=sgqlc.types.Arg(_schema.String), objectEntityId=sgqlc.types.Arg(_schema.UUID), citationUrl=sgqlc.types.Arg(_schema.String)))
    _op_create_statement = _op.create_statement(input={'subjectId': sgqlc.types.Variable('entityId'), 'predicateId': sgqlc.types.Variable('predicateId'), 'objectValue': sgqlc.types.Variable('objectValue'), 'objectEntityId': sgqlc.types.Variable('objectEntityId'), 'citationUrl': sgqlc.types.Variable('citationUrl')})
    _op_create_statement_statement = _op_create_statement.statement()
    _op_create_statement_statement.__fragment__(fragment_triple_widget())
    return _op


class Mutation:
    add_triple_to_entity_by_id = mutation_add_triple_to_entity_by_id()


class Operations:
    mutation = Mutation
