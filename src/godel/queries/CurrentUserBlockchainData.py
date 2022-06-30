import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_current_user_blockchain_data():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='CurrentUserBlockchainData')
    _op_current_user_blockchain_data = _op.current_user_blockchain_data()
    _op_current_user_blockchain_data.user_id()
    _op_current_user_blockchain_data.staked_tokens()
    _op_current_user_blockchain_data.tokens_balance()
    _op_current_user_blockchain_data.contract_owner()
    return _op


class Query:
    current_user_blockchain_data = query_current_user_blockchain_data()


class Operations:
    query = Query
