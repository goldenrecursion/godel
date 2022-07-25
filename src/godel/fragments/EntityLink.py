import sgqlc.types
import sgqlc.operation
import godel.schema

_schema = godel.schema
_schema_root = _schema.schema

__all__ = ('Operations',)


def fragment_entity_link():
    _frag = sgqlc.operation.Fragment(_schema.Entity, 'EntityLink')
    _frag.id()
    _frag.pathname()
    _frag.name()
    _frag.thumbnail()
    return _frag


class Fragment:
    entity_link = fragment_entity_link()


class Operations:
    fragment = Fragment
