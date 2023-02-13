from godel.fragments.TripleWidget import fragment_triple_widget
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_triple_event():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='TripleEvent', variables=dict(first=sgqlc.types.Arg(_schema.Int, default=20), after=sgqlc.types.Arg(_schema.Cursor, default=None), condition=sgqlc.types.Arg(_schema.LedgerRecordCondition)))
    _op_ledger_records = _op.ledger_records(first=sgqlc.types.Variable('first'), after=sgqlc.types.Variable('after'), condition=sgqlc.types.Variable('condition'), order_by='CREATED_AT_DESC')
    _op_ledger_records_page_info = _op_ledger_records.page_info()
    _op_ledger_records_page_info.end_cursor()
    _op_ledger_records_page_info.has_previous_page()
    _op_ledger_records_page_info.has_next_page()
    _op_ledger_records_edges = _op_ledger_records.edges()
    _op_ledger_records_edges_node = _op_ledger_records_edges.node()
    _op_ledger_records_edges_node.amount()
    _op_ledger_records_edges_node.created_at()
    _op_ledger_records_edges_node_user = _op_ledger_records_edges_node.user()
    _op_ledger_records_edges_node_user.id()
    _op_ledger_records_edges_node_user.ens_name()
    _op_ledger_records_edges_node_triple = _op_ledger_records_edges_node.triple()
    _op_ledger_records_edges_node_triple__as__Statement = _op_ledger_records_edges_node_triple.__as__(_schema.Statement)
    _op_ledger_records_edges_node_triple__as__Statement.__fragment__(fragment_triple_widget())
    return _op


class Query:
    triple_event = query_triple_event()


class Operations:
    query = Query
