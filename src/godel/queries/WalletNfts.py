import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_wallet_nfts():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='WalletNfts', variables=dict(after=sgqlc.types.Arg(_schema.Cursor, default=None)))
    _op_eligible_nfts = _op.current_user_nft_requests(first=20, after=sgqlc.types.Variable('after'), order_by='LEDGER_RECORD_AMOUNT_SUM_DESC', __alias__='eligible_nfts')
    _op_eligible_nfts.total_count()
    _op_eligible_nfts_page_info = _op_eligible_nfts.page_info()
    _op_eligible_nfts_page_info.has_next_page()
    _op_eligible_nfts_page_info.end_cursor()
    _op_eligible_nfts_nodes = _op_eligible_nfts.nodes()
    _op_eligible_nfts_nodes_entity = _op_eligible_nfts_nodes.entity()
    _op_eligible_nfts_nodes_entity.__fragment__(fragment_entity_link())
    _op_eligible_nfts_nodes.ledger_record_amount_sum()
    _op_eligible_nfts_nodes.entity_ledger_record_amount_sum()
    _op_eligible_nfts_nodes.ownership_percent()
    return _op


class Query:
    wallet_nfts = query_wallet_nfts()


class Operations:
    query = Query
