import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_user_nft_requests():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='UserNftRequests', variables=dict(userId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String)), after=sgqlc.types.Arg(_schema.Cursor, default=None)))
    _op_user = _op.user(id=sgqlc.types.Variable('userId'))
    _op_user_nft_requests = _op_user.nft_requests(first=20, after=sgqlc.types.Variable('after'))
    _op_user_nft_requests.total_count()
    _op_user_nft_requests_page_info = _op_user_nft_requests.page_info()
    _op_user_nft_requests_page_info.has_next_page()
    _op_user_nft_requests_page_info.end_cursor()
    _op_user_nft_requests_nodes = _op_user_nft_requests.nodes()
    _op_user_nft_requests_nodes_entity = _op_user_nft_requests_nodes.entity()
    _op_user_nft_requests_nodes_entity.__fragment__(fragment_entity_link())
    _op_user_nft_requests_nodes.ledger_record_amount_sum()
    _op_user_nft_requests_nodes.entity_ledger_record_amount_sum()
    _op_user_nft_requests_nodes.ownership_percent()
    return _op


class Query:
    user_nft_requests = query_user_nft_requests()


class Operations:
    query = Query
