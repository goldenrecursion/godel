import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_triple_count():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='TripleCount')
    _op_statements = _op.statements()
    _op_statements.total_count()
    return _op


class Query:
    triple_count = query_triple_count()


class Operations:
    query = Query
