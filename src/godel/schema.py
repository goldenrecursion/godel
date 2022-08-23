import sgqlc.types
import sgqlc.types.relay


schema = sgqlc.types.Schema()


# Unexport Node/PageInfo, let schema re-declare them
schema -= sgqlc.types.relay.Node
schema -= sgqlc.types.relay.PageInfo



########################################################################
# Scalars and Enumerations
########################################################################
class BigInt(sgqlc.types.Scalar):
    __schema__ = schema


Boolean = sgqlc.types.Boolean

class CitationsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'TRIPLE_ID_ASC', 'TRIPLE_ID_DESC', 'URL_ASC', 'URL_DESC')


class Cursor(sgqlc.types.Scalar):
    __schema__ = schema


class Datetime(sgqlc.types.Scalar):
    __schema__ = schema


class EntitiesOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class EnumPredicateConstraintTargetType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('OBJECT', 'SUBJECT')


Float = sgqlc.types.Float

ID = sgqlc.types.ID

Int = sgqlc.types.Int

class JwtToken(sgqlc.types.Scalar):
    __schema__ = schema


class LedgerRecordReason(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ADMIN', 'GROUND_TRUTH_TRIPLE_VOTE', 'INITIAL_AWARD', 'SUBMITTED_TRIPLE', 'VOTE_CONCLUDED')


class LedgerRecordsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AMOUNT_ASC', 'AMOUNT_DESC', 'CREATED_AT_ASC', 'CREATED_AT_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'REASON_ASC', 'REASON_DESC', 'TRIPLE_ID_ASC', 'TRIPLE_ID_DESC', 'USER_ID_ASC', 'USER_ID_DESC')


class PoPredicateObjectConstraintTargetType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('OBJECT', 'SUBJECT')


class PredicateConstraintType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ENUM', 'FORMAT', 'PREDICATE_OBJECT')


class PredicatesOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CID_ASC', 'CID_DESC', 'DESCRIPTION_ASC', 'DESCRIPTION_DESC', 'ID_ASC', 'ID_DESC', 'LABEL_ASC', 'LABEL_DESC', 'NAME_ASC', 'NAME_DESC', 'NATURAL', 'OBJECT_TYPE_ASC', 'OBJECT_TYPE_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class QualifiersOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATE_ACCEPTED_ASC', 'DATE_ACCEPTED_DESC', 'DATE_CONSTRAINTS_VIOLATED_ASC', 'DATE_CONSTRAINTS_VIOLATED_DESC', 'DATE_CREATED_ASC', 'DATE_CREATED_DESC', 'DATE_REJECTED_ASC', 'DATE_REJECTED_DESC', 'DATE_SLASHED_ASC', 'DATE_SLASHED_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'OBJECT_ENTITY_ID_ASC', 'OBJECT_ENTITY_ID_DESC', 'OBJECT_VALUE_ASC', 'OBJECT_VALUE_DESC', 'PREDICATE_ID_ASC', 'PREDICATE_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SUBJECT_ID_ASC', 'SUBJECT_ID_DESC', 'USER_ID_ASC', 'USER_ID_DESC', 'VALIDATION_STATUS_ASC', 'VALIDATION_STATUS_DESC')


class StatementsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATE_ACCEPTED_ASC', 'DATE_ACCEPTED_DESC', 'DATE_CONSTRAINTS_VIOLATED_ASC', 'DATE_CONSTRAINTS_VIOLATED_DESC', 'DATE_CREATED_ASC', 'DATE_CREATED_DESC', 'DATE_REJECTED_ASC', 'DATE_REJECTED_DESC', 'DATE_SLASHED_ASC', 'DATE_SLASHED_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'OBJECT_ENTITY_ID_ASC', 'OBJECT_ENTITY_ID_DESC', 'OBJECT_VALUE_ASC', 'OBJECT_VALUE_DESC', 'PREDICATE_ID_ASC', 'PREDICATE_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SUBJECT_ID_ASC', 'SUBJECT_ID_DESC', 'USER_ID_ASC', 'USER_ID_DESC', 'VALIDATION_STATUS_ASC', 'VALIDATION_STATUS_DESC')


String = sgqlc.types.String

class TemplatePredicatesOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ID_ASC', 'ID_DESC', 'NATURAL', 'PREDICATE_ID_ASC', 'PREDICATE_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'RANK_ASC', 'RANK_DESC', 'TEMPLATE_ID_ASC', 'TEMPLATE_ID_DESC')


class TemplatesOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ENTITY_ID_ASC', 'ENTITY_ID_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'RANK_ASC', 'RANK_DESC')


class TopUserSubmittersOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACCEPTED_STATEMENT_COUNT_ASC', 'ACCEPTED_STATEMENT_COUNT_DESC', 'NATURAL', 'SUBMITTED_STATEMENT_COUNT_ASC', 'SUBMITTED_STATEMENT_COUNT_DESC', 'USER_ID_ASC', 'USER_ID_DESC')


class TopUserValidatorsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('NATURAL', 'USER_ID_ASC', 'USER_ID_DESC', 'VALIDATION_CONSENSUS_COUNT_ASC', 'VALIDATION_CONSENSUS_COUNT_DESC', 'VALIDATION_COUNT_ASC', 'VALIDATION_COUNT_DESC')


class TripleRequestsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATE_CREATED_ASC', 'DATE_CREATED_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PREDICATE_ID_ASC', 'PREDICATE_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'SUBJECT_ENTITY_ID_ASC', 'SUBJECT_ENTITY_ID_DESC')


class TriplesOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('DATE_ACCEPTED_ASC', 'DATE_ACCEPTED_DESC', 'DATE_CREATED_ASC', 'DATE_CREATED_DESC', 'DATE_REJECTED_ASC', 'DATE_REJECTED_DESC', 'DATE_SLASHED_ASC', 'DATE_SLASHED_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'OBJECT_VALUE_ASC', 'OBJECT_VALUE_DESC', 'PREDICATE_ID_ASC', 'PREDICATE_ID_DESC', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'USER_ID_ASC', 'USER_ID_DESC', 'VALIDATION_STATUS_ASC', 'VALIDATION_STATUS_DESC')


class UUID(sgqlc.types.Scalar):
    __schema__ = schema


class UserFlagType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('WELCOME_MODAL',)


class UserFlagsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'FLAG_ASC', 'FLAG_DESC', 'ID_ASC', 'ID_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC', 'USER_ID_ASC', 'USER_ID_DESC')


class ValidationConsensusStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('AGREED', 'DISAGREED', 'PENDING')


class ValidationStatus(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACCEPTED', 'INVALID', 'PAUSED', 'PENDING', 'REJECTED')


class ValidationType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ACCEPTED', 'REJECTED', 'SKIPPED')


class ValidationsOrderBy(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('CREATED_AT_ASC', 'CREATED_AT_DESC', 'NATURAL', 'PRIMARY_KEY_ASC', 'PRIMARY_KEY_DESC')


class ValueType(sgqlc.types.Enum):
    __schema__ = schema
    __choices__ = ('ANY_URI', 'DATE_TIME', 'DECIMAL', 'ENTITY', 'FLOAT', 'INTEGER', 'STRING')



########################################################################
# Input Objects
########################################################################
class AuthenticateInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id', 'signature')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    signature = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='signature')


class CitationCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'triple_id', 'url')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    triple_id = sgqlc.types.Field(UUID, graphql_name='tripleId')
    url = sgqlc.types.Field(String, graphql_name='url')


class CreateEntityInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'name', 'statements')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    statements = sgqlc.types.Field(sgqlc.types.list_of('StatementInputRecordInput'), graphql_name='statements')


class CreateQualifierInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id', 'predicate_id', 'object_value', 'object_entity_id', 'citation_urls')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='subjectId')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    citation_urls = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='citationUrls')


class CreateStatementInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'subject_id', 'predicate_id', 'object_value', 'object_entity_id', 'citation_urls', 'qualifiers')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='subjectId')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    citation_urls = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='citationUrls')
    qualifiers = sgqlc.types.Field(sgqlc.types.list_of('QualifierInputRecordInput'), graphql_name='qualifiers')


class CreateUserFlagInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'flag')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    flag = sgqlc.types.Field(sgqlc.types.non_null(UserFlagType), graphql_name='flag')


class CreateValidationInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'triple_id', 'validation_type')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    triple_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='tripleId')
    validation_type = sgqlc.types.Field(sgqlc.types.non_null(ValidationType), graphql_name='validationType')


class EntityCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id',)
    id = sgqlc.types.Field(UUID, graphql_name='id')


class FulfillTripleRequestInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'input_triple_request_id', 'input_object_value', 'input_object_entity_id', 'input_citation_urls')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    input_triple_request_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='inputTripleRequestId')
    input_object_value = sgqlc.types.Field(String, graphql_name='inputObjectValue')
    input_object_entity_id = sgqlc.types.Field(UUID, graphql_name='inputObjectEntityId')
    input_citation_urls = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='inputCitationUrls')


class GetAuthenticationMessageInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_id')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')


class LedgerRecordCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'user_id', 'created_at', 'amount', 'reason', 'triple_id')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    reason = sgqlc.types.Field(LedgerRecordReason, graphql_name='reason')
    triple_id = sgqlc.types.Field(UUID, graphql_name='tripleId')


class PredicateCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'object_type', 'cid', 'label')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    name = sgqlc.types.Field(String, graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    object_type = sgqlc.types.Field(ValueType, graphql_name='objectType')
    cid = sgqlc.types.Field(String, graphql_name='cid')
    label = sgqlc.types.Field(String, graphql_name='label')


class QualifierCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'subject_id', 'predicate_id', 'object_value', 'object_entity_id', 'user_id', 'date_created', 'date_accepted', 'date_rejected', 'date_constraints_violated', 'date_slashed', 'validation_status')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    subject_id = sgqlc.types.Field(UUID, graphql_name='subjectId')
    predicate_id = sgqlc.types.Field(UUID, graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    date_created = sgqlc.types.Field(Datetime, graphql_name='dateCreated')
    date_accepted = sgqlc.types.Field(Datetime, graphql_name='dateAccepted')
    date_rejected = sgqlc.types.Field(Datetime, graphql_name='dateRejected')
    date_constraints_violated = sgqlc.types.Field(Datetime, graphql_name='dateConstraintsViolated')
    date_slashed = sgqlc.types.Field(Datetime, graphql_name='dateSlashed')
    validation_status = sgqlc.types.Field(ValidationStatus, graphql_name='validationStatus')


class QualifierInputRecordInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('predicate_id', 'object_value', 'object_entity_id', 'citation_urls')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    citation_urls = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='citationUrls')


class StatementCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'subject_id', 'predicate_id', 'object_value', 'object_entity_id', 'user_id', 'date_created', 'date_accepted', 'date_rejected', 'date_constraints_violated', 'date_slashed', 'validation_status')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    subject_id = sgqlc.types.Field(UUID, graphql_name='subjectId')
    predicate_id = sgqlc.types.Field(UUID, graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    date_created = sgqlc.types.Field(Datetime, graphql_name='dateCreated')
    date_accepted = sgqlc.types.Field(Datetime, graphql_name='dateAccepted')
    date_rejected = sgqlc.types.Field(Datetime, graphql_name='dateRejected')
    date_constraints_violated = sgqlc.types.Field(Datetime, graphql_name='dateConstraintsViolated')
    date_slashed = sgqlc.types.Field(Datetime, graphql_name='dateSlashed')
    validation_status = sgqlc.types.Field(ValidationStatus, graphql_name='validationStatus')


class StatementInputRecordInput(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('predicate_id', 'object_value', 'object_entity_id', 'citation_urls', 'qualifiers')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    citation_urls = sgqlc.types.Field(sgqlc.types.list_of(String), graphql_name='citationUrls')
    qualifiers = sgqlc.types.Field(sgqlc.types.list_of(QualifierInputRecordInput), graphql_name='qualifiers')


class TemplateCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'entity_id', 'rank')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    entity_id = sgqlc.types.Field(UUID, graphql_name='entityId')
    rank = sgqlc.types.Field(Int, graphql_name='rank')


class TemplatePredicateCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'template_id', 'predicate_id', 'rank')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    template_id = sgqlc.types.Field(UUID, graphql_name='templateId')
    predicate_id = sgqlc.types.Field(UUID, graphql_name='predicateId')
    rank = sgqlc.types.Field(Int, graphql_name='rank')


class TopUserSubmitterCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('user_id', 'submitted_statement_count', 'accepted_statement_count')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    submitted_statement_count = sgqlc.types.Field(Int, graphql_name='submittedStatementCount')
    accepted_statement_count = sgqlc.types.Field(Int, graphql_name='acceptedStatementCount')


class TopUserValidatorCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('user_id', 'validation_count', 'validation_consensus_count')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    validation_count = sgqlc.types.Field(Int, graphql_name='validationCount')
    validation_consensus_count = sgqlc.types.Field(Int, graphql_name='validationConsensusCount')


class TripleCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'date_created', 'predicate_id', 'object_value', 'user_id', 'date_accepted', 'date_rejected', 'date_slashed', 'validation_status')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    date_created = sgqlc.types.Field(Datetime, graphql_name='dateCreated')
    predicate_id = sgqlc.types.Field(UUID, graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    date_accepted = sgqlc.types.Field(Datetime, graphql_name='dateAccepted')
    date_rejected = sgqlc.types.Field(Datetime, graphql_name='dateRejected')
    date_slashed = sgqlc.types.Field(Datetime, graphql_name='dateSlashed')
    validation_status = sgqlc.types.Field(ValidationStatus, graphql_name='validationStatus')


class TripleRequestCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'subject_entity_id', 'predicate_id', 'date_created')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    subject_entity_id = sgqlc.types.Field(UUID, graphql_name='subjectEntityId')
    predicate_id = sgqlc.types.Field(UUID, graphql_name='predicateId')
    date_created = sgqlc.types.Field(Datetime, graphql_name='dateCreated')


class UserFlagCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'user_id', 'flag', 'created_at')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    flag = sgqlc.types.Field(UserFlagType, graphql_name='flag')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')


class ValidationCondition(sgqlc.types.Input):
    __schema__ = schema
    __field_names__ = ('id', 'triple_id', 'user_id', 'validation_type', 'created_at', 'validation_consensus_status')
    id = sgqlc.types.Field(UUID, graphql_name='id')
    triple_id = sgqlc.types.Field(UUID, graphql_name='tripleId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    validation_type = sgqlc.types.Field(ValidationType, graphql_name='validationType')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    validation_consensus_status = sgqlc.types.Field(ValidationConsensusStatus, graphql_name='validationConsensusStatus')



########################################################################
# Output Objects and Interfaces
########################################################################
class AuthenticatePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'jwt_token', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    jwt_token = sgqlc.types.Field(JwtToken, graphql_name='jwtToken')
    query = sgqlc.types.Field('Query', graphql_name='query')


class BasePredicateConstraintsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BasePredicateConstraint'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('BasePredicateConstraintsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class BasePredicateConstraintsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('BasePredicateConstraint'), graphql_name='node')


class CitationsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Citation'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('CitationsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class CitationsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Citation'), graphql_name='node')


class CreateEntityPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'entity', 'query', 'entity_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    entity = sgqlc.types.Field('Entity', graphql_name='entity')
    query = sgqlc.types.Field('Query', graphql_name='query')
    entity_edge = sgqlc.types.Field('EntitiesEdge', graphql_name='entityEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EntitiesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class CreateQualifierPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'qualifier', 'query', 'subject', 'predicate', 'object_entity', 'qualifier_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    qualifier = sgqlc.types.Field('Qualifier', graphql_name='qualifier')
    query = sgqlc.types.Field('Query', graphql_name='query')
    subject = sgqlc.types.Field(sgqlc.types.non_null('Statement'), graphql_name='subject')
    predicate = sgqlc.types.Field(sgqlc.types.non_null('Predicate'), graphql_name='predicate')
    object_entity = sgqlc.types.Field('Entity', graphql_name='objectEntity')
    qualifier_edge = sgqlc.types.Field('QualifiersEdge', graphql_name='qualifierEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(QualifiersOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class CreateStatementPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'statement', 'query', 'subject', 'predicate', 'object_entity', 'statement_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    statement = sgqlc.types.Field('Statement', graphql_name='statement')
    query = sgqlc.types.Field('Query', graphql_name='query')
    subject = sgqlc.types.Field(sgqlc.types.non_null('Entity'), graphql_name='subject')
    predicate = sgqlc.types.Field(sgqlc.types.non_null('Predicate'), graphql_name='predicate')
    object_entity = sgqlc.types.Field('Entity', graphql_name='objectEntity')
    statement_edge = sgqlc.types.Field('StatementsEdge', graphql_name='statementEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StatementsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class CreateUserFlagPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'user_flag', 'query', 'user_flag_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    user_flag = sgqlc.types.Field('UserFlag', graphql_name='userFlag')
    query = sgqlc.types.Field('Query', graphql_name='query')
    user_flag_edge = sgqlc.types.Field('UserFlagsEdge', graphql_name='userFlagEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UserFlagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class CreateValidationPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'validation', 'query', 'triple', 'validation_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    validation = sgqlc.types.Field('Validation', graphql_name='validation')
    query = sgqlc.types.Field('Query', graphql_name='query')
    triple = sgqlc.types.Field(sgqlc.types.non_null('Triple'), graphql_name='triple')
    validation_edge = sgqlc.types.Field('ValidationsEdge', graphql_name='validationEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ValidationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class EntitiesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Entity'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EntitiesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EntitiesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Entity'), graphql_name='node')


class EnumPredicateConstraintElementsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EnumPredicateConstraintElement'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('EnumPredicateConstraintElementsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class EnumPredicateConstraintElementsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('EnumPredicateConstraintElement'), graphql_name='node')


class FulfillTripleRequestPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'statement', 'query', 'subject', 'predicate', 'object_entity', 'statement_edge')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    statement = sgqlc.types.Field('Statement', graphql_name='statement')
    query = sgqlc.types.Field('Query', graphql_name='query')
    subject = sgqlc.types.Field(sgqlc.types.non_null('Entity'), graphql_name='subject')
    predicate = sgqlc.types.Field(sgqlc.types.non_null('Predicate'), graphql_name='predicate')
    object_entity = sgqlc.types.Field('Entity', graphql_name='objectEntity')
    statement_edge = sgqlc.types.Field('StatementsEdge', graphql_name='statementEdge', args=sgqlc.types.ArgDict((
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StatementsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
))
    )


class GetAuthenticationMessagePayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('client_mutation_id', 'string', 'query')
    client_mutation_id = sgqlc.types.Field(String, graphql_name='clientMutationId')
    string = sgqlc.types.Field(String, graphql_name='string')
    query = sgqlc.types.Field('Query', graphql_name='query')


class LedgerRecordChangedPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('event', 'amount', 'balance')
    event = sgqlc.types.Field(String, graphql_name='event')
    amount = sgqlc.types.Field(BigInt, graphql_name='amount')
    balance = sgqlc.types.Field(BigInt, graphql_name='balance')


class LedgerRecordsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LedgerRecord'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('LedgerRecordsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null('PageInfo'), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class LedgerRecordsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('LedgerRecord'), graphql_name='node')


class Mutation(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('authenticate', 'create_entity', 'create_qualifier', 'create_statement', 'create_user_flag', 'create_validation', 'fulfill_triple_request', 'get_authentication_message')
    authenticate = sgqlc.types.Field(AuthenticatePayload, graphql_name='authenticate', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(AuthenticateInput), graphql_name='input', default=None)),
))
    )
    create_entity = sgqlc.types.Field(CreateEntityPayload, graphql_name='createEntity', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateEntityInput), graphql_name='input', default=None)),
))
    )
    create_qualifier = sgqlc.types.Field(CreateQualifierPayload, graphql_name='createQualifier', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateQualifierInput), graphql_name='input', default=None)),
))
    )
    create_statement = sgqlc.types.Field(CreateStatementPayload, graphql_name='createStatement', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateStatementInput), graphql_name='input', default=None)),
))
    )
    create_user_flag = sgqlc.types.Field(CreateUserFlagPayload, graphql_name='createUserFlag', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateUserFlagInput), graphql_name='input', default=None)),
))
    )
    create_validation = sgqlc.types.Field(CreateValidationPayload, graphql_name='createValidation', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(CreateValidationInput), graphql_name='input', default=None)),
))
    )
    fulfill_triple_request = sgqlc.types.Field(FulfillTripleRequestPayload, graphql_name='fulfillTripleRequest', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(FulfillTripleRequestInput), graphql_name='input', default=None)),
))
    )
    get_authentication_message = sgqlc.types.Field(GetAuthenticationMessagePayload, graphql_name='getAuthenticationMessage', args=sgqlc.types.ArgDict((
        ('input', sgqlc.types.Arg(sgqlc.types.non_null(GetAuthenticationMessageInput), graphql_name='input', default=None)),
))
    )


class Node(sgqlc.types.Interface):
    __schema__ = schema
    __field_names__ = ('node_id',)
    node_id = sgqlc.types.Field(sgqlc.types.non_null(ID), graphql_name='nodeId')


class PageInfo(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('has_next_page', 'has_previous_page', 'start_cursor', 'end_cursor')
    has_next_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasNextPage')
    has_previous_page = sgqlc.types.Field(sgqlc.types.non_null(Boolean), graphql_name='hasPreviousPage')
    start_cursor = sgqlc.types.Field(Cursor, graphql_name='startCursor')
    end_cursor = sgqlc.types.Field(Cursor, graphql_name='endCursor')


class PoPredicateConstraintRulesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PoPredicateConstraintRule'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PoPredicateConstraintRulesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PoPredicateConstraintRulesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('PoPredicateConstraintRule'), graphql_name='node')


class PredicatesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Predicate'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('PredicatesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class PredicatesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Predicate'), graphql_name='node')


class QualifiersConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Qualifier'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('QualifiersEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class QualifiersEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Qualifier'), graphql_name='node')


class StatementsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Statement'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('StatementsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class StatementsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Statement'), graphql_name='node')


class SubmittersRanking(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user_id', 'submitted_statement_count', 'accepted_statement_count', 'ranking_submitted_statement_count', 'ranking_accepted_statement_count')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    submitted_statement_count = sgqlc.types.Field(Int, graphql_name='submittedStatementCount')
    accepted_statement_count = sgqlc.types.Field(Int, graphql_name='acceptedStatementCount')
    ranking_submitted_statement_count = sgqlc.types.Field(Int, graphql_name='rankingSubmittedStatementCount')
    ranking_accepted_statement_count = sgqlc.types.Field(Int, graphql_name='rankingAcceptedStatementCount')


class Subscription(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user_triple_validated', 'triple_validated', 'ledger_record_changed', 'user_balance_changed')
    user_triple_validated = sgqlc.types.Field('TripleValidatedSubscriptionPayload', graphql_name='userTripleValidated')
    triple_validated = sgqlc.types.Field('TripleValidatedSubscriptionPayload', graphql_name='tripleValidated', args=sgqlc.types.ArgDict((
        ('triple_id', sgqlc.types.Arg(String, graphql_name='tripleId', default=None)),
))
    )
    ledger_record_changed = sgqlc.types.Field(LedgerRecordChangedPayload, graphql_name='ledgerRecordChanged')
    user_balance_changed = sgqlc.types.Field('UserBalanceChangedPayload', graphql_name='userBalanceChanged')


class TemplatePredicatesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TemplatePredicate'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TemplatePredicatesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TemplatePredicatesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('TemplatePredicate'), graphql_name='node')


class TemplatesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Template'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TemplatesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TemplatesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Template'), graphql_name='node')


class TopUserSubmitter(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user_id', 'submitted_statement_count', 'accepted_statement_count')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    submitted_statement_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='submittedStatementCount')
    accepted_statement_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='acceptedStatementCount')


class TopUserSubmittersConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TopUserSubmitter))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TopUserSubmittersEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TopUserSubmittersEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(TopUserSubmitter), graphql_name='node')


class TopUserValidator(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user_id', 'validation_count', 'validation_consensus_count')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    validation_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='validationCount')
    validation_consensus_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='validationConsensusCount')


class TopUserValidatorsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null(TopUserValidator))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TopUserValidatorsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TopUserValidatorsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null(TopUserValidator), graphql_name='node')


class TripleRequestsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TripleRequest'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TripleRequestsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TripleRequestsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('TripleRequest'), graphql_name='node')


class TripleValidatedSubscriptionPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('triple', 'event', 'is_valid')
    triple = sgqlc.types.Field('Triple', graphql_name='triple')
    event = sgqlc.types.Field(String, graphql_name='event')
    is_valid = sgqlc.types.Field(Boolean, graphql_name='isValid')


class TriplesConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Triple'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('TriplesEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class TriplesEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field('Triple', graphql_name='node')


class UserBalanceChangedPayload(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('event', 'token_balance', 'stake_balance')
    event = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='event')
    token_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenBalance')
    stake_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='stakeBalance')


class UserFlagsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserFlag'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('UserFlagsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class UserFlagsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('UserFlag'), graphql_name='node')


class UserStat(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('accuracy', 'agreed_with_consensus_count', 'disagreed_with_consensus_count', 'pending_count')
    accuracy = sgqlc.types.Field(sgqlc.types.non_null(Float), graphql_name='accuracy')
    agreed_with_consensus_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='agreedWithConsensusCount')
    disagreed_with_consensus_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='disagreedWithConsensusCount')
    pending_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='pendingCount')


class ValidationsConnection(sgqlc.types.relay.Connection):
    __schema__ = schema
    __field_names__ = ('nodes', 'edges', 'page_info', 'total_count')
    nodes = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('Validation'))), graphql_name='nodes')
    edges = sgqlc.types.Field(sgqlc.types.non_null(sgqlc.types.list_of(sgqlc.types.non_null('ValidationsEdge'))), graphql_name='edges')
    page_info = sgqlc.types.Field(sgqlc.types.non_null(PageInfo), graphql_name='pageInfo')
    total_count = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='totalCount')


class ValidationsEdge(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('cursor', 'node')
    cursor = sgqlc.types.Field(Cursor, graphql_name='cursor')
    node = sgqlc.types.Field(sgqlc.types.non_null('Validation'), graphql_name='node')


class ValidatorsRanking(sgqlc.types.Type):
    __schema__ = schema
    __field_names__ = ('user_id', 'validation_count', 'validation_consensus_count', 'ranking_validation_count', 'ranking_validation_consensus_count')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    validation_count = sgqlc.types.Field(Int, graphql_name='validationCount')
    validation_consensus_count = sgqlc.types.Field(Int, graphql_name='validationConsensusCount')
    ranking_validation_count = sgqlc.types.Field(Int, graphql_name='rankingValidationCount')
    ranking_validation_consensus_count = sgqlc.types.Field(Int, graphql_name='rankingValidationConsensusCount')


class BasePredicateConstraint(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'predicate_id', 'type', 'allow', 'predicate', 'child_format_predicate_constraint', 'child_po_predicate_constraint', 'child_enum_predicate_constraint')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    type = sgqlc.types.Field(sgqlc.types.non_null(PredicateConstraintType), graphql_name='type')
    allow = sgqlc.types.Field(Boolean, graphql_name='allow')
    predicate = sgqlc.types.Field(sgqlc.types.non_null('Predicate'), graphql_name='predicate')
    child_format_predicate_constraint = sgqlc.types.Field('FormatPredicateConstraint', graphql_name='childFormatPredicateConstraint')
    child_po_predicate_constraint = sgqlc.types.Field('PoPredicateConstraint', graphql_name='childPoPredicateConstraint')
    child_enum_predicate_constraint = sgqlc.types.Field('EnumPredicateConstraint', graphql_name='childEnumPredicateConstraint')


class Citation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'triple_id', 'url', 'citation', 'triple')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    triple_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='tripleId')
    url = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='url')
    citation = sgqlc.types.Field(sgqlc.types.non_null('Triple'), graphql_name='citation')
    triple = sgqlc.types.Field(sgqlc.types.non_null('Statement'), graphql_name='triple')


class Entity(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'template', 'triple_requests_by_subject_entity_id', 'po_predicate_constraint_rules_by_object_entity_id', 'enum_predicate_constraint_elements_by_object_entity_id', 'qualifiers_by_object_entity_id', 'statements_by_subject_id', 'statements_by_object_entity_id', 'description', 'golden_id', 'is_a', 'name', 'pathname', 'thumbnail', 'website')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    template = sgqlc.types.Field('Template', graphql_name='template')
    triple_requests_by_subject_entity_id = sgqlc.types.Field(sgqlc.types.non_null(TripleRequestsConnection), graphql_name='tripleRequestsBySubjectEntityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TripleRequestsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TripleRequestCondition, graphql_name='condition', default=None)),
))
    )
    po_predicate_constraint_rules_by_object_entity_id = sgqlc.types.Field(sgqlc.types.non_null(PoPredicateConstraintRulesConnection), graphql_name='poPredicateConstraintRulesByObjectEntityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    enum_predicate_constraint_elements_by_object_entity_id = sgqlc.types.Field(sgqlc.types.non_null(EnumPredicateConstraintElementsConnection), graphql_name='enumPredicateConstraintElementsByObjectEntityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    qualifiers_by_object_entity_id = sgqlc.types.Field(sgqlc.types.non_null(QualifiersConnection), graphql_name='qualifiersByObjectEntityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(QualifiersOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(QualifierCondition, graphql_name='condition', default=None)),
))
    )
    statements_by_subject_id = sgqlc.types.Field(sgqlc.types.non_null(StatementsConnection), graphql_name='statementsBySubjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StatementsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(StatementCondition, graphql_name='condition', default=None)),
))
    )
    statements_by_object_entity_id = sgqlc.types.Field(sgqlc.types.non_null(StatementsConnection), graphql_name='statementsByObjectEntityId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StatementsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(StatementCondition, graphql_name='condition', default=None)),
))
    )
    description = sgqlc.types.Field(String, graphql_name='description')
    golden_id = sgqlc.types.Field(String, graphql_name='goldenId')
    is_a = sgqlc.types.Field(sgqlc.types.non_null(EntitiesConnection), graphql_name='isA', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    name = sgqlc.types.Field(String, graphql_name='name')
    pathname = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='pathname')
    thumbnail = sgqlc.types.Field(String, graphql_name='thumbnail')
    website = sgqlc.types.Field(String, graphql_name='website')


class EnumPredicateConstraint(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('parent_id', 'target', 'parent', 'enum_predicate_constraint_elements_by_constraint_id')
    parent_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='parentId')
    target = sgqlc.types.Field(sgqlc.types.non_null(EnumPredicateConstraintTargetType), graphql_name='target')
    parent = sgqlc.types.Field(sgqlc.types.non_null(BasePredicateConstraint), graphql_name='parent')
    enum_predicate_constraint_elements_by_constraint_id = sgqlc.types.Field(sgqlc.types.non_null(EnumPredicateConstraintElementsConnection), graphql_name='enumPredicateConstraintElementsByConstraintId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )


class EnumPredicateConstraintElement(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'constraint_id', 'object_value', 'object_entity_id', 'constraint', 'object_entity')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    constraint_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='constraintId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(EnumPredicateConstraint), graphql_name='constraint')
    object_entity = sgqlc.types.Field(Entity, graphql_name='objectEntity')


class FormatPredicateConstraint(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('parent_id', 'regex_pattern', 'parent')
    parent_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='parentId')
    regex_pattern = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='regexPattern')
    parent = sgqlc.types.Field(sgqlc.types.non_null(BasePredicateConstraint), graphql_name='parent')


class LedgerRecord(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'user_id', 'created_at', 'amount', 'reason', 'triple_id', 'triple')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    amount = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='amount')
    reason = sgqlc.types.Field(sgqlc.types.non_null(LedgerRecordReason), graphql_name='reason')
    triple_id = sgqlc.types.Field(UUID, graphql_name='tripleId')
    triple = sgqlc.types.Field('Triple', graphql_name='triple')


class PoPredicateConstraint(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('parent_id', 'target', 'parent', 'po_predicate_constraint_rules_by_constraint_id')
    parent_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='parentId')
    target = sgqlc.types.Field(sgqlc.types.non_null(PoPredicateObjectConstraintTargetType), graphql_name='target')
    parent = sgqlc.types.Field(sgqlc.types.non_null(BasePredicateConstraint), graphql_name='parent')
    po_predicate_constraint_rules_by_constraint_id = sgqlc.types.Field(sgqlc.types.non_null(PoPredicateConstraintRulesConnection), graphql_name='poPredicateConstraintRulesByConstraintId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )


class PoPredicateConstraintRule(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'constraint_id', 'predicate_id', 'object_value', 'object_entity_id', 'constraint', 'predicate', 'object_entity')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    constraint_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='constraintId')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    constraint = sgqlc.types.Field(sgqlc.types.non_null(PoPredicateConstraint), graphql_name='constraint')
    predicate = sgqlc.types.Field(sgqlc.types.non_null('Predicate'), graphql_name='predicate')
    object_entity = sgqlc.types.Field(Entity, graphql_name='objectEntity')


class Predicate(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'name', 'description', 'object_type', 'cid', 'label', 'triples', 'template_predicates', 'triple_requests', 'base_predicate_constraints', 'po_predicate_constraint_rules', 'qualifiers', 'statements', 'show_in_infobox')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    name = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='name')
    description = sgqlc.types.Field(String, graphql_name='description')
    object_type = sgqlc.types.Field(sgqlc.types.non_null(ValueType), graphql_name='objectType')
    cid = sgqlc.types.Field(String, graphql_name='cid')
    label = sgqlc.types.Field(String, graphql_name='label')
    triples = sgqlc.types.Field(sgqlc.types.non_null(TriplesConnection), graphql_name='triples', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TriplesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TripleCondition, graphql_name='condition', default=None)),
))
    )
    template_predicates = sgqlc.types.Field(sgqlc.types.non_null(TemplatePredicatesConnection), graphql_name='templatePredicates', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TemplatePredicatesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TemplatePredicateCondition, graphql_name='condition', default=None)),
))
    )
    triple_requests = sgqlc.types.Field(sgqlc.types.non_null(TripleRequestsConnection), graphql_name='tripleRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TripleRequestsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TripleRequestCondition, graphql_name='condition', default=None)),
))
    )
    base_predicate_constraints = sgqlc.types.Field(sgqlc.types.non_null(BasePredicateConstraintsConnection), graphql_name='basePredicateConstraints', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    po_predicate_constraint_rules = sgqlc.types.Field(sgqlc.types.non_null(PoPredicateConstraintRulesConnection), graphql_name='poPredicateConstraintRules', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    qualifiers = sgqlc.types.Field(sgqlc.types.non_null(QualifiersConnection), graphql_name='qualifiers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(QualifiersOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(QualifierCondition, graphql_name='condition', default=None)),
))
    )
    statements = sgqlc.types.Field(sgqlc.types.non_null(StatementsConnection), graphql_name='statements', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StatementsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(StatementCondition, graphql_name='condition', default=None)),
))
    )
    show_in_infobox = sgqlc.types.Field(Boolean, graphql_name='showInInfobox')


class Qualifier(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'subject_id', 'predicate_id', 'object_value', 'object_entity_id', 'user_id', 'date_created', 'date_accepted', 'date_rejected', 'date_constraints_violated', 'date_slashed', 'validation_status', 'subject', 'predicate', 'object_entity')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='subjectId')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    date_created = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='dateCreated')
    date_accepted = sgqlc.types.Field(Datetime, graphql_name='dateAccepted')
    date_rejected = sgqlc.types.Field(Datetime, graphql_name='dateRejected')
    date_constraints_violated = sgqlc.types.Field(Datetime, graphql_name='dateConstraintsViolated')
    date_slashed = sgqlc.types.Field(Datetime, graphql_name='dateSlashed')
    validation_status = sgqlc.types.Field(sgqlc.types.non_null(ValidationStatus), graphql_name='validationStatus')
    subject = sgqlc.types.Field(sgqlc.types.non_null('Statement'), graphql_name='subject')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Predicate), graphql_name='predicate')
    object_entity = sgqlc.types.Field(Entity, graphql_name='objectEntity')


class Query(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('query', 'node', 'base_predicate_constraints', 'citations', 'entities', 'ledger_records', 'predicates', 'qualifiers', 'statements', 'templates', 'template_predicates', 'top_user_submitters', 'top_user_validators', 'triples', 'triple_requests', 'user_flags', 'base_predicate_constraint', 'citation', 'entity', 'enum_predicate_constraint', 'enum_predicate_constraint_element', 'format_predicate_constraint', 'ledger_record', 'po_predicate_constraint', 'po_predicate_constraint_rule', 'predicate', 'predicate_by_name', 'qualifier', 'statement', 'template', 'template_by_entity_id', 'template_predicate', 'triple', 'triple_request', 'user_flag', 'user_flag_by_user_id_and_flag', 'validation', '_statement_by_sp', '_statements_by_sp', 'current_user', 'current_user_submitters_ranking', 'current_user_user_id', 'current_user_validators_ranking', 'entity_by_golden_id', 'entity_by_name', 'pending_triple_request', 'unvalidated_triple', 'base_predicate_constraint_by_node_id', 'citation_by_node_id', 'entity_by_node_id', 'enum_predicate_constraint_by_node_id', 'enum_predicate_constraint_element_by_node_id', 'format_predicate_constraint_by_node_id', 'ledger_record_by_node_id', 'po_predicate_constraint_by_node_id', 'po_predicate_constraint_rule_by_node_id', 'predicate_by_node_id', 'qualifier_by_node_id', 'statement_by_node_id', 'template_by_node_id', 'template_predicate_by_node_id', 'triple_by_node_id', 'triple_request_by_node_id', 'user_flag_by_node_id', 'validation_by_node_id')
    query = sgqlc.types.Field(sgqlc.types.non_null('Query'), graphql_name='query')
    node = sgqlc.types.Field(Node, graphql_name='node', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    base_predicate_constraints = sgqlc.types.Field(BasePredicateConstraintsConnection, graphql_name='basePredicateConstraints', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    citations = sgqlc.types.Field(CitationsConnection, graphql_name='citations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CitationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(CitationCondition, graphql_name='condition', default=None)),
))
    )
    entities = sgqlc.types.Field(EntitiesConnection, graphql_name='entities', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(EntitiesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(EntityCondition, graphql_name='condition', default=None)),
))
    )
    ledger_records = sgqlc.types.Field(LedgerRecordsConnection, graphql_name='ledgerRecords', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(LedgerRecordsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(LedgerRecordCondition, graphql_name='condition', default=None)),
))
    )
    predicates = sgqlc.types.Field(PredicatesConnection, graphql_name='predicates', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(PredicatesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(PredicateCondition, graphql_name='condition', default=None)),
))
    )
    qualifiers = sgqlc.types.Field(QualifiersConnection, graphql_name='qualifiers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(QualifiersOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(QualifierCondition, graphql_name='condition', default=None)),
))
    )
    statements = sgqlc.types.Field(StatementsConnection, graphql_name='statements', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StatementsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(StatementCondition, graphql_name='condition', default=None)),
))
    )
    templates = sgqlc.types.Field(TemplatesConnection, graphql_name='templates', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TemplatesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TemplateCondition, graphql_name='condition', default=None)),
))
    )
    template_predicates = sgqlc.types.Field(TemplatePredicatesConnection, graphql_name='templatePredicates', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TemplatePredicatesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TemplatePredicateCondition, graphql_name='condition', default=None)),
))
    )
    top_user_submitters = sgqlc.types.Field(TopUserSubmittersConnection, graphql_name='topUserSubmitters', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TopUserSubmittersOrderBy)), graphql_name='orderBy', default=('NATURAL',))),
        ('condition', sgqlc.types.Arg(TopUserSubmitterCondition, graphql_name='condition', default=None)),
))
    )
    top_user_validators = sgqlc.types.Field(TopUserValidatorsConnection, graphql_name='topUserValidators', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TopUserValidatorsOrderBy)), graphql_name='orderBy', default=('NATURAL',))),
        ('condition', sgqlc.types.Arg(TopUserValidatorCondition, graphql_name='condition', default=None)),
))
    )
    triples = sgqlc.types.Field(TriplesConnection, graphql_name='triples', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TriplesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TripleCondition, graphql_name='condition', default=None)),
))
    )
    triple_requests = sgqlc.types.Field(TripleRequestsConnection, graphql_name='tripleRequests', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TripleRequestsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TripleRequestCondition, graphql_name='condition', default=None)),
))
    )
    user_flags = sgqlc.types.Field(UserFlagsConnection, graphql_name='userFlags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UserFlagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(UserFlagCondition, graphql_name='condition', default=None)),
))
    )
    base_predicate_constraint = sgqlc.types.Field(BasePredicateConstraint, graphql_name='basePredicateConstraint', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    citation = sgqlc.types.Field(Citation, graphql_name='citation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    entity = sgqlc.types.Field(Entity, graphql_name='entity', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    enum_predicate_constraint = sgqlc.types.Field(EnumPredicateConstraint, graphql_name='enumPredicateConstraint', args=sgqlc.types.ArgDict((
        ('parent_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='parentId', default=None)),
))
    )
    enum_predicate_constraint_element = sgqlc.types.Field(EnumPredicateConstraintElement, graphql_name='enumPredicateConstraintElement', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    format_predicate_constraint = sgqlc.types.Field(FormatPredicateConstraint, graphql_name='formatPredicateConstraint', args=sgqlc.types.ArgDict((
        ('parent_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='parentId', default=None)),
))
    )
    ledger_record = sgqlc.types.Field(LedgerRecord, graphql_name='ledgerRecord', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    po_predicate_constraint = sgqlc.types.Field(PoPredicateConstraint, graphql_name='poPredicateConstraint', args=sgqlc.types.ArgDict((
        ('parent_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='parentId', default=None)),
))
    )
    po_predicate_constraint_rule = sgqlc.types.Field(PoPredicateConstraintRule, graphql_name='poPredicateConstraintRule', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    predicate = sgqlc.types.Field(Predicate, graphql_name='predicate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    predicate_by_name = sgqlc.types.Field(Predicate, graphql_name='predicateByName', args=sgqlc.types.ArgDict((
        ('name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='name', default=None)),
))
    )
    qualifier = sgqlc.types.Field(Qualifier, graphql_name='qualifier', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    statement = sgqlc.types.Field('Statement', graphql_name='statement', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    template = sgqlc.types.Field('Template', graphql_name='template', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    template_by_entity_id = sgqlc.types.Field('Template', graphql_name='templateByEntityId', args=sgqlc.types.ArgDict((
        ('entity_id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='entityId', default=None)),
))
    )
    template_predicate = sgqlc.types.Field('TemplatePredicate', graphql_name='templatePredicate', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    triple = sgqlc.types.Field('Triple', graphql_name='triple', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    triple_request = sgqlc.types.Field('TripleRequest', graphql_name='tripleRequest', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    user_flag = sgqlc.types.Field('UserFlag', graphql_name='userFlag', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    user_flag_by_user_id_and_flag = sgqlc.types.Field('UserFlag', graphql_name='userFlagByUserIdAndFlag', args=sgqlc.types.ArgDict((
        ('user_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='userId', default=None)),
        ('flag', sgqlc.types.Arg(sgqlc.types.non_null(UserFlagType), graphql_name='flag', default=None)),
))
    )
    validation = sgqlc.types.Field('Validation', graphql_name='validation', args=sgqlc.types.ArgDict((
        ('id', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='id', default=None)),
))
    )
    _statement_by_sp = sgqlc.types.Field('Statement', graphql_name='_statementBySp', args=sgqlc.types.ArgDict((
        ('subject', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='subject', default=None)),
        ('predicate', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='predicate', default=None)),
))
    )
    _statements_by_sp = sgqlc.types.Field('Statement', graphql_name='_statementsBySp', args=sgqlc.types.ArgDict((
        ('subject', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='subject', default=None)),
        ('predicate', sgqlc.types.Arg(sgqlc.types.non_null(UUID), graphql_name='predicate', default=None)),
))
    )
    current_user = sgqlc.types.Field('User', graphql_name='currentUser')
    current_user_submitters_ranking = sgqlc.types.Field(SubmittersRanking, graphql_name='currentUserSubmittersRanking')
    current_user_user_id = sgqlc.types.Field(String, graphql_name='currentUserUserId')
    current_user_validators_ranking = sgqlc.types.Field(ValidatorsRanking, graphql_name='currentUserValidatorsRanking')
    entity_by_golden_id = sgqlc.types.Field(Entity, graphql_name='entityByGoldenId', args=sgqlc.types.ArgDict((
        ('golden_id', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='goldenId', default=None)),
))
    )
    entity_by_name = sgqlc.types.Field(EntitiesConnection, graphql_name='entityByName', args=sgqlc.types.ArgDict((
        ('entity_name', sgqlc.types.Arg(sgqlc.types.non_null(String), graphql_name='entityName', default=None)),
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
))
    )
    pending_triple_request = sgqlc.types.Field('TripleRequest', graphql_name='pendingTripleRequest')
    unvalidated_triple = sgqlc.types.Field('Triple', graphql_name='unvalidatedTriple')
    base_predicate_constraint_by_node_id = sgqlc.types.Field(BasePredicateConstraint, graphql_name='basePredicateConstraintByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    citation_by_node_id = sgqlc.types.Field(Citation, graphql_name='citationByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    entity_by_node_id = sgqlc.types.Field(Entity, graphql_name='entityByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    enum_predicate_constraint_by_node_id = sgqlc.types.Field(EnumPredicateConstraint, graphql_name='enumPredicateConstraintByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    enum_predicate_constraint_element_by_node_id = sgqlc.types.Field(EnumPredicateConstraintElement, graphql_name='enumPredicateConstraintElementByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    format_predicate_constraint_by_node_id = sgqlc.types.Field(FormatPredicateConstraint, graphql_name='formatPredicateConstraintByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    ledger_record_by_node_id = sgqlc.types.Field(LedgerRecord, graphql_name='ledgerRecordByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    po_predicate_constraint_by_node_id = sgqlc.types.Field(PoPredicateConstraint, graphql_name='poPredicateConstraintByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    po_predicate_constraint_rule_by_node_id = sgqlc.types.Field(PoPredicateConstraintRule, graphql_name='poPredicateConstraintRuleByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    predicate_by_node_id = sgqlc.types.Field(Predicate, graphql_name='predicateByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    qualifier_by_node_id = sgqlc.types.Field(Qualifier, graphql_name='qualifierByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    statement_by_node_id = sgqlc.types.Field('Statement', graphql_name='statementByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    template_by_node_id = sgqlc.types.Field('Template', graphql_name='templateByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    template_predicate_by_node_id = sgqlc.types.Field('TemplatePredicate', graphql_name='templatePredicateByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    triple_by_node_id = sgqlc.types.Field('Triple', graphql_name='tripleByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    triple_request_by_node_id = sgqlc.types.Field('TripleRequest', graphql_name='tripleRequestByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    user_flag_by_node_id = sgqlc.types.Field('UserFlag', graphql_name='userFlagByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )
    validation_by_node_id = sgqlc.types.Field('Validation', graphql_name='validationByNodeId', args=sgqlc.types.ArgDict((
        ('node_id', sgqlc.types.Arg(sgqlc.types.non_null(ID), graphql_name='nodeId', default=None)),
))
    )


class Statement(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'subject_id', 'predicate_id', 'object_value', 'object_entity_id', 'user_id', 'date_created', 'date_accepted', 'date_rejected', 'date_constraints_violated', 'date_slashed', 'validation_status', 'subject', 'predicate', 'object_entity', 'citations_by_triple_id', 'qualifiers_by_subject_id')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    subject_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='subjectId')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    object_value = sgqlc.types.Field(String, graphql_name='objectValue')
    object_entity_id = sgqlc.types.Field(UUID, graphql_name='objectEntityId')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    date_created = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='dateCreated')
    date_accepted = sgqlc.types.Field(Datetime, graphql_name='dateAccepted')
    date_rejected = sgqlc.types.Field(Datetime, graphql_name='dateRejected')
    date_constraints_violated = sgqlc.types.Field(Datetime, graphql_name='dateConstraintsViolated')
    date_slashed = sgqlc.types.Field(Datetime, graphql_name='dateSlashed')
    validation_status = sgqlc.types.Field(sgqlc.types.non_null(ValidationStatus), graphql_name='validationStatus')
    subject = sgqlc.types.Field(sgqlc.types.non_null(Entity), graphql_name='subject')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Predicate), graphql_name='predicate')
    object_entity = sgqlc.types.Field(Entity, graphql_name='objectEntity')
    citations_by_triple_id = sgqlc.types.Field(sgqlc.types.non_null(CitationsConnection), graphql_name='citationsByTripleId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(CitationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(CitationCondition, graphql_name='condition', default=None)),
))
    )
    qualifiers_by_subject_id = sgqlc.types.Field(sgqlc.types.non_null(QualifiersConnection), graphql_name='qualifiersBySubjectId', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(QualifiersOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(QualifierCondition, graphql_name='condition', default=None)),
))
    )


class Template(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'entity_id', 'rank', 'entity', 'template_predicates')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    entity_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='entityId')
    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')
    entity = sgqlc.types.Field(sgqlc.types.non_null(Entity), graphql_name='entity')
    template_predicates = sgqlc.types.Field(sgqlc.types.non_null(TemplatePredicatesConnection), graphql_name='templatePredicates', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TemplatePredicatesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TemplatePredicateCondition, graphql_name='condition', default=None)),
))
    )


class TemplatePredicate(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'template_id', 'predicate_id', 'rank', 'template', 'predicate')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    template_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='templateId')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    rank = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='rank')
    template = sgqlc.types.Field(sgqlc.types.non_null(Template), graphql_name='template')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Predicate), graphql_name='predicate')


class TripleRequest(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'subject_entity_id', 'predicate_id', 'date_created', 'subject_entity', 'predicate')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    subject_entity_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='subjectEntityId')
    predicate_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='predicateId')
    date_created = sgqlc.types.Field(sgqlc.types.non_null(Datetime), graphql_name='dateCreated')
    subject_entity = sgqlc.types.Field(sgqlc.types.non_null(Entity), graphql_name='subjectEntity')
    predicate = sgqlc.types.Field(sgqlc.types.non_null(Predicate), graphql_name='predicate')


class User(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'nonce', 'created_at', 'stake_balance', 'token_balance', 'balance', 'triples', 'validations', 'ledger_records', 'user_flags', 'qualifiers', 'statements', 'remaining_skips', 'short_address', 'stats')
    id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='id')
    nonce = sgqlc.types.Field(sgqlc.types.non_null(Int), graphql_name='nonce')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    stake_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='stakeBalance')
    token_balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='tokenBalance')
    balance = sgqlc.types.Field(sgqlc.types.non_null(BigInt), graphql_name='balance')
    triples = sgqlc.types.Field(sgqlc.types.non_null(TriplesConnection), graphql_name='triples', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(TriplesOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(TripleCondition, graphql_name='condition', default=None)),
))
    )
    validations = sgqlc.types.Field(sgqlc.types.non_null(ValidationsConnection), graphql_name='validations', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(ValidationsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(ValidationCondition, graphql_name='condition', default=None)),
))
    )
    ledger_records = sgqlc.types.Field(sgqlc.types.non_null(LedgerRecordsConnection), graphql_name='ledgerRecords', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(LedgerRecordsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(LedgerRecordCondition, graphql_name='condition', default=None)),
))
    )
    user_flags = sgqlc.types.Field(sgqlc.types.non_null(UserFlagsConnection), graphql_name='userFlags', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(UserFlagsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(UserFlagCondition, graphql_name='condition', default=None)),
))
    )
    qualifiers = sgqlc.types.Field(sgqlc.types.non_null(QualifiersConnection), graphql_name='qualifiers', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(QualifiersOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(QualifierCondition, graphql_name='condition', default=None)),
))
    )
    statements = sgqlc.types.Field(sgqlc.types.non_null(StatementsConnection), graphql_name='statements', args=sgqlc.types.ArgDict((
        ('first', sgqlc.types.Arg(Int, graphql_name='first', default=None)),
        ('last', sgqlc.types.Arg(Int, graphql_name='last', default=None)),
        ('offset', sgqlc.types.Arg(Int, graphql_name='offset', default=None)),
        ('before', sgqlc.types.Arg(Cursor, graphql_name='before', default=None)),
        ('after', sgqlc.types.Arg(Cursor, graphql_name='after', default=None)),
        ('order_by', sgqlc.types.Arg(sgqlc.types.list_of(sgqlc.types.non_null(StatementsOrderBy)), graphql_name='orderBy', default=('PRIMARY_KEY_ASC',))),
        ('condition', sgqlc.types.Arg(StatementCondition, graphql_name='condition', default=None)),
))
    )
    remaining_skips = sgqlc.types.Field(Int, graphql_name='remainingSkips')
    short_address = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='shortAddress')
    stats = sgqlc.types.Field(sgqlc.types.non_null(UserStat), graphql_name='stats')


class UserFlag(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'user_id', 'flag', 'created_at')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    user_id = sgqlc.types.Field(sgqlc.types.non_null(String), graphql_name='userId')
    flag = sgqlc.types.Field(sgqlc.types.non_null(UserFlagType), graphql_name='flag')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')


class Validation(sgqlc.types.Type, Node):
    __schema__ = schema
    __field_names__ = ('id', 'triple_id', 'user_id', 'validation_type', 'created_at', 'triple', 'ground_truth_violation_reason')
    id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='id')
    triple_id = sgqlc.types.Field(sgqlc.types.non_null(UUID), graphql_name='tripleId')
    user_id = sgqlc.types.Field(String, graphql_name='userId')
    validation_type = sgqlc.types.Field(sgqlc.types.non_null(ValidationType), graphql_name='validationType')
    created_at = sgqlc.types.Field(Datetime, graphql_name='createdAt')
    triple = sgqlc.types.Field(sgqlc.types.non_null('Triple'), graphql_name='triple')
    ground_truth_violation_reason = sgqlc.types.Field(String, graphql_name='groundTruthViolationReason')



########################################################################
# Unions
########################################################################
class Triple(sgqlc.types.Union):
    __schema__ = schema
    __types__ = (Statement, Qualifier)



########################################################################
# Schema Entry Points
########################################################################
schema.query_type = Query
schema.mutation_type = Mutation
schema.subscription_type = Subscription

