import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_leaderboard():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='Leaderboard', variables=dict(orderBy=sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(_schema.TopUsersOrderBy))), sortKey=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String))))
    _op_top_users = _op.top_users(order_by=sgqlc.types.Variable('orderBy'), first=100)
    _op_top_users_nodes = _op_top_users.nodes()
    _op_top_users_nodes.user_id()
    _op_top_users_nodes.submitted_statement_count()
    _op_top_users_nodes.accepted_statement_count()
    _op_get_user_ranking = _op.get_user_ranking(sort_key=sgqlc.types.Variable('sortKey'))
    _op_get_user_ranking_nodes = _op_get_user_ranking.nodes()
    _op_get_user_ranking_nodes.user_id()
    _op_get_user_ranking_nodes.submitted_statement_count()
    _op_get_user_ranking_nodes.accepted_statement_count()
    _op_get_user_ranking_nodes.ranking()
    return _op


class Query:
    leaderboard = query_leaderboard()


class Operations:
    query = Query
