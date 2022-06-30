import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_predicates_from_ipfs():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='PredicatesFromIPFS')
    _op_predicates_from_ipfs = _op.predicates_from_ipfs()
    _op_predicates_from_ipfs_predicates = _op_predicates_from_ipfs.predicates()
    _op_predicates_from_ipfs_predicates.name()
    return _op


class Query:
    predicates_from_ipfs = query_predicates_from_ipfs()


class Operations:
    query = Query
