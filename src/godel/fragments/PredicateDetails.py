import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def fragment_predicate_details():
    _frag = sgqlc.operation.Fragment(_schema.Predicate, 'PredicateDetails')
    _frag.id()
    _frag.name()
    _frag.description()
    _frag.object_type()
    _frag.label()
    return _frag


class Fragment:
    predicate_details = fragment_predicate_details()


class Operations:
    fragment = Fragment
