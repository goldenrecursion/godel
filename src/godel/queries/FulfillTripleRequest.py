import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def mutation_fulfill_triple_request():
    _op = sgqlc.operation.Operation(_schema_root.mutation_type, name='FulfillTripleRequest', variables=dict(tripleRequestId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), objectValue=sgqlc.types.Arg(_schema.String), objectEntityId=sgqlc.types.Arg(_schema.UUID), citationUrls=sgqlc.types.Arg(sgqlc.types.list_of(_schema.String))))
    _op_fulfill_triple_request = _op.fulfill_triple_request(input={'inputTripleRequestId': sgqlc.types.Variable('tripleRequestId'), 'inputObjectValue': sgqlc.types.Variable('objectValue'), 'inputObjectEntityId': sgqlc.types.Variable('objectEntityId'), 'inputCitationUrls': sgqlc.types.Variable('citationUrls')})
    _op_fulfill_triple_request_statement = _op_fulfill_triple_request.statement()
    _op_fulfill_triple_request_statement.__fragment__(fragment_triple_widget())
    return _op


class Mutation:
    fulfill_triple_request = mutation_fulfill_triple_request()


class Operations:
    mutation = Mutation
