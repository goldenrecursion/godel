import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_get_citations():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='GetCitations', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=None), after=sgqlc.types.Arg(_schema.Cursor, default=None), orderBy=sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(_schema.CitationsOrderBy))), condition=sgqlc.types.Arg(sgqlc.types.non_null(_schema.CitationCondition))))
    _op_citations = _op.citations(order_by=sgqlc.types.Variable('orderBy'), after=sgqlc.types.Variable('after'), first=sgqlc.types.Variable('first'), condition=sgqlc.types.Variable('condition'))
    _op_citations.total_count()
    _op_citations_nodes = _op_citations.nodes()
    _op_citations_nodes.id()
    _op_citations_nodes.url()
    return _op


class Query:
    get_citations = query_get_citations()


class Operations:
    query = Query
