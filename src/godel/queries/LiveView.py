from godel.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_live_view():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='LiveView', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None), condition=sgqlc.types.Arg(_schema.TripleCondition), orderBy=sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(_schema.TriplesOrderBy)), default=('DATE_ACCEPTED_DESC',))))
    _op_triples = _op.triples(first=sgqlc.types.Variable('first'), after=sgqlc.types.Variable('after'), condition=sgqlc.types.Variable('condition'), order_by=sgqlc.types.Variable('orderBy'))
    _op_triples_page_info = _op_triples.page_info()
    _op_triples_page_info.end_cursor()
    _op_triples_page_info.has_previous_page()
    _op_triples_page_info.has_next_page()
    _op_triples_edges = _op_triples.edges()
    _op_triples_edges_node = _op_triples_edges.node()
    _op_triples_edges_node.__fragment__(fragment_triple_widget())
    return _op


class Query:
    live_view = query_live_view()


class Operations:
    query = Query
