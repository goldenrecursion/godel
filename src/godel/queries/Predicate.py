from godel.fragments.PredicateDetails import fragment_predicate_details
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_predicate():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='Predicate', variables=dict(name=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String))))
    _op_predicate_by_name = _op.predicate_by_name(name=sgqlc.types.Variable('name'))
    _op_predicate_by_name.__fragment__(fragment_predicate_details())
    return _op


class Query:
    predicate = query_predicate()


class Operations:
    query = Query
