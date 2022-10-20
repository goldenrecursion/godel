import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_contributors():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityContributors', variables=dict(id=sgqlc.types.Arg(sgqlc.types.non_null(_schema.UUID)), after=sgqlc.types.Arg(_schema.Cursor, default=None)))
    _op_entity = _op.entity(id=sgqlc.types.Variable('id'))
    _op_entity.id()
    _op_entity_nft_requests = _op_entity.nft_requests(first=5, after=sgqlc.types.Variable('after'))
    _op_entity_nft_requests_page_info = _op_entity_nft_requests.page_info()
    _op_entity_nft_requests_page_info.has_next_page()
    _op_entity_nft_requests_page_info.end_cursor()
    _op_entity_nft_requests_nodes = _op_entity_nft_requests.nodes()
    _op_entity_nft_requests_nodes.user_id()
    _op_entity_nft_requests_nodes.ledger_record_amount_sum()
    _op_entity_nft_requests_nodes.ownership_percent()
    return _op


class Query:
    entity_contributors = query_entity_contributors()


class Operations:
    query = Query
