# v0.5.1

## What's Changed
* Update disamb call with args and multi-pred params by @aychang95 in https://github.com/goldenrecursion/godel/pull/33


**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.5.0...v0.5.1

# v0.5.0

## What's Changed
* Variable + wording changes by @katkaypettitt in https://github.com/goldenrecursion/godel/pull/28
* Api changes demo fix by @katkaypettitt in https://github.com/goldenrecursion/godel/pull/29
* Add disambiguate triple query by @aychang95 in https://github.com/goldenrecursion/godel/pull/30
* Add headers metric by @aychang95 in https://github.com/goldenrecursion/godel/pull/31
* Sc 18593 by @aychang95 in https://github.com/goldenrecursion/godel/pull/32

## New Contributors
* @katkaypettitt made their first contribution in https://github.com/goldenrecursion/godel/pull/28

**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.4.3...v0.5.0

# v0.4.3

## What's Changed
* Sc 18483/name delete by @aychang95 in https://github.com/goldenrecursion/godel/pull/25
* Update changelog to v0.4.2 by @aychang95 in https://github.com/goldenrecursion/godel/pull/26
* Query/assignvalidation by @aychang95 in https://github.com/goldenrecursion/godel/pull/27

## Breaking Changes
Previous versions <v0.4.3 will no longer be able to use the `unvalidated_triple()` method.

**Full Changelog**: https://github.com/goldenrecursion/godel/compare/v0.4.2...v0.4.3

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