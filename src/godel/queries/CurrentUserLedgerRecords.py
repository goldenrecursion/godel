import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_current_user_ledger_records():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='CurrentUserLedgerRecords', variables=dict(after=sgqlc.types.Arg(_schema.Cursor, default=None), condition=sgqlc.types.Arg(sgqlc.types.non_null(_schema.LedgerRecordCondition))))
    _op_current_user = _op.current_user()
    _op_current_user_ledger_records = _op_current_user.ledger_records(first=20, after=sgqlc.types.Variable('after'), order_by='CREATED_AT_DESC', condition=sgqlc.types.Variable('condition'))
    _op_current_user_ledger_records.total_count()
    _op_current_user_ledger_records_page_info = _op_current_user_ledger_records.page_info()
    _op_current_user_ledger_records_page_info.has_next_page()
    _op_current_user_ledger_records_page_info.end_cursor()
    _op_current_user_ledger_records_nodes = _op_current_user_ledger_records.nodes()
    _op_current_user_ledger_records_nodes.id()
    _op_current_user_ledger_records_nodes.created_at()
    _op_current_user_ledger_records_nodes.amount()
    _op_current_user_ledger_records_nodes_triple = _op_current_user_ledger_records_nodes.triple()
    _op_current_user_ledger_records_nodes_triple__as__Statement = _op_current_user_ledger_records_nodes_triple.__as__(_schema.Statement)
    _op_current_user_ledger_records_nodes_triple__as__Statement.__fragment__(fragment_triple_widget())
    _op_current_user_ledger_records_nodes_type = _op_current_user_ledger_records_nodes.type()
    _op_current_user_ledger_records_nodes_type.title()
    _op_current_user_ledger_records_nodes_type.details()
    return _op


class Query:
    current_user_ledger_records = query_current_user_ledger_records()


class Operations:
    query = Query
