from godel.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_live_view():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='LiveView')
    _op_triples = _op.triples(first=20, condition={'validationStatus': 'ACCEPTED'}, order_by='DATE_ACCEPTED_DESC')
    _op_triples_nodes = _op_triples.nodes()
    _op_triples_nodes.__fragment__(fragment_triple_widget())
    return _op


class Query:
    live_view = query_live_view()


class Operations:
    query = Query
