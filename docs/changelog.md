# v0.4.2

## What's Changed
* Sc 18483/name delete by @aychang95 in https://github.com/goldenrecursion/godel/pull/23
* Update version and dependencies by @aychang95 in https://github.com/goldenrecursion/godel/pull/24

## Breaking Changes
The name statement will have to be added as statement instead of a GraphQL query param from now on.
```
StatementInputRecordInput(
    predicate_id = <NAME-predicate-id>,
    object_value = <name>,
    citation_urls = [],
    qualifiers = [],
)
```

**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.4.1...v0.4.2

# v0.4.1

## What's Changed
* Update generated modules by @aychang95 in https://github.com/goldenrecursion/godel/pull/21

New `create_triple_flag()` mutation.

**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.4.0...v0.4.1


# v0.4.0

## What's Changed
* Create inputs by @aychang95 in https://github.com/goldenrecursion/godel/pull/18
* Update guides for docs and notebook tutorials by @aychang95 in https://github.com/goldenrecursion/godel/pull/20
* Update/v0.4.0 by @aychang95 in https://github.com/goldenrecursion/godel/pull/19

## Deprecation
* Deprecating `add_triple_to_entity` in favor of `create_entity`

**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.3.5...v0.4.0


# v0.3.5

## What's Changed
* Fix importlib for 37 and update readme by @aychang95 in https://github.com/goldenrecursion/godel/pull/17


**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.3.4...v0.3.5


# v0.3.4

## What's Changed
* Update triple widget and clean repo by @aychang95 in https://github.com/goldenrecursion/godel/pull/15
* Fix version retrieval and simplify by removing toml by @aychang95 in https://github.com/goldenrecursion/godel/pull/16


**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.3.3...v0.3.4