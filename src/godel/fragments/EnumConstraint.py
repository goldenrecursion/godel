import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def fragment_enum_constraint():
    _frag = sgqlc.operation.Fragment(_schema.EnumPredicateConstraintElement, 'EnumConstraint')
    _frag.id()
    _frag.object_value()
    _frag_object_entity = _frag.object_entity()
    _frag_object_entity.__fragment__(fragment_entity_link())
    return _frag


class Fragment:
    enum_constraint = fragment_enum_constraint()


class Operations:
    fragment = Fragment
