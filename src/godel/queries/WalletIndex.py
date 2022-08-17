import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_wallet_index():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='WalletIndex')
    _op_current_user = _op.current_user()
    _op_current_user.id()
    _op_current_user_ledger_records = _op_current_user.ledger_records(first=20, order_by='CREATED_AT_DESC')
    _op_current_user_ledger_records_nodes = _op_current_user_ledger_records.nodes()
    _op_current_user_ledger_records_nodes.id()
    _op_current_user_ledger_records_nodes.created_at()
    _op_current_user_ledger_records_nodes.amount()
    _op_current_user_ledger_records_nodes.reason()
    _op_current_user_ledger_records_nodes_triple = _op_current_user_ledger_records_nodes.triple()
    _op_current_user_ledger_records_nodes_triple__as__Statement = _op_current_user_ledger_records_nodes_triple.__as__(_schema.Statement)
    _op_current_user_ledger_records_nodes_triple__as__Statement.__fragment__(fragment_triple_widget())
    return _op


class Query:
    wallet_index = query_wallet_index()


class Operations:
    query = Query
