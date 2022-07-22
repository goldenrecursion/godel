import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_predicate_detail():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='PredicateDetail', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID))))
    _op_predicate = _op.predicate(id=sgqlc.types.Variable('id'))
    _op_predicate.__fragment__(fragment_predicate_details())
    return _op


class Query:
    predicate_detail = query_predicate_detail()


class Operations:
    query = Query
