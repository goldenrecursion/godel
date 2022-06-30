from godel.fragments.EntityDetail import fragment_entity_detail
import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def query_entity_golden():
    _op = sgqlc.operation.Operation(_schema_root.query_type, name='EntityGolden', variables=dict(goldenId=sgqlc.types.Arg(sgqlc.types.non_null(_schema.String))))
    _op_entity_by_golden_id = _op.entity_by_golden_id(golden_id=sgqlc.types.Variable('goldenId'))
    _op_entity_by_golden_id.__fragment__(fragment_entity_detail())
    return _op


class Query:
    entity_golden = query_entity_golden()


class Operations:
    query = Query
