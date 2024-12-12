from __future__ import annotations

from typing import Annotated, Any, Literal, TypedDict, NotRequired

from pydantic import AnyUrl, Field


class ExternalDocumentation(TypedDict):
    description: NotRequired[str]
    url: AnyUrl


class XML(TypedDict):
    name: NotRequired[str]
    namespace: NotRequired[AnyUrl]
    prefix: NotRequired[str]
    attribute: NotRequired[bool]
    wrapped: NotRequired[bool]


class Discriminator(TypedDict):
    propertyName: str
    mapping: NotRequired[dict[str, str]]


class Reference(TypedDict):
    ref: Annotated[str, Field(alias="$ref")]


class Schema(TypedDict):
    title: NotRequired[str]
    multipleOf: NotRequired[float]
    maximum: NotRequired[float]
    exclusiveMaximum: NotRequired[float]
    minimum: NotRequired[float]
    exclusiveMinimum: NotRequired[float]
    maxLength: NotRequired[int]
    minLength: NotRequired[int]
    pattern: NotRequired[str]
    maxItems: NotRequired[int]
    minItems: NotRequired[int]
    uniqueItems: NotRequired[bool]
    maxProperties: NotRequired[int]
    minProperties: NotRequired[int]
    required: NotRequired[list[str]]
    enum: NotRequired[list[Any]]
    type: NotRequired[str | list[str]]
    allOf: NotRequired[list[Schema | Reference]]
    oneOf: NotRequired[list[Schema | Reference]]
    anyOf: NotRequired[list[Schema | Reference]]
    not_: Annotated[NotRequired[Schema | Reference], Field(alias="not")]
    items: NotRequired[Schema | Reference]
    properties: NotRequired[dict[str, Schema | Reference]]
    additionalProperties: NotRequired[bool | Schema | Reference]
    description: NotRequired[str]
    format: NotRequired[str]
    default: NotRequired[Any]
    nullable: NotRequired[bool]
    discriminator: NotRequired[Discriminator]
    readOnly: NotRequired[bool]
    writeOnly: NotRequired[bool]
    xml: NotRequired[XML]
    externalDocs: NotRequired[ExternalDocumentation]
    example: NotRequired[Any]
    deprecated: NotRequired[bool]
    contentMediaType: NotRequired[str]
    contentEncoding: NotRequired[str]


class Example(TypedDict):
    summary: NotRequired[str]
    description: NotRequired[str]
    value: NotRequired[Any]
    externalValue: NotRequired[AnyUrl]


class Encoding(TypedDict):
    contentType: NotRequired[str]
    headers: NotRequired[dict[str, Header | Reference]]
    style: NotRequired[str]
    explode: NotRequired[bool]
    allowReserved: NotRequired[bool]


class MediaType(TypedDict):
    schema_: NotRequired[Schema | Reference]
    example: NotRequired[Any]
    examples: NotRequired[dict[str, Example | Reference]]
    encoding: NotRequired[dict[str, Encoding]]


class Parameter(TypedDict):
    name: str
    in_: str
    description: NotRequired[str]
    required: NotRequired[bool]
    deprecated: NotRequired[bool]
    allowEmptyValue: NotRequired[bool]
    style: NotRequired[str]
    explode: NotRequired[bool]
    allowReserved: NotRequired[bool]
    schema_: NotRequired[Schema | Reference]
    example: NotRequired[Any]
    examples: NotRequired[dict[str, Example | Reference]]
    content: NotRequired[dict[str, MediaType]]


class Header(TypedDict):
    description: NotRequired[str]
    required: NotRequired[bool]
    deprecated: NotRequired[bool]
    allowEmptyValue: NotRequired[bool]
    style: NotRequired[str]
    explode: NotRequired[bool]
    allowReserved: NotRequired[bool]
    schema_: NotRequired[Schema | Reference]
    example: NotRequired[Any]
    examples: NotRequired[dict[str, Example | Reference]]
    content: NotRequired[dict[str, MediaType]]


class RequestBody(TypedDict):
    description: NotRequired[str]
    content: dict[str, MediaType]
    required: NotRequired[bool]


class Link(TypedDict):
    operationRef: NotRequired[str]
    operationId: NotRequired[str]
    parameters: NotRequired[dict[str, Any]]
    requestBody: NotRequired[Any]
    description: NotRequired[str]
    server: NotRequired["Server"]  # Forward reference


class Response(TypedDict):
    description: str
    headers: NotRequired[dict[str, Header | Reference]]
    content: NotRequired[dict[str, MediaType]]
    links: NotRequired[dict[str, Link | Reference]]


class Operation(TypedDict):
    tags: NotRequired[list[str]]
    summary: NotRequired[str]
    description: NotRequired[str]
    externalDocs: NotRequired[ExternalDocumentation]
    operationId: NotRequired[str]
    parameters: NotRequired[list[Parameter | Reference]]
    requestBody: NotRequired[RequestBody | Reference]
    responses: dict[str, Response | Reference]
    callbacks: NotRequired[dict[str, dict[str, "PathItem"]]]  # Forward reference
    deprecated: NotRequired[bool]
    security: NotRequired[list[dict[str, list[str]]]]
    servers: NotRequired[list["Server"]]


class ServerVariable(TypedDict):
    enum: NotRequired[list[str]]
    default: str
    description: NotRequired[str]


class Server(TypedDict):
    url: str
    description: NotRequired[str]
    variables: NotRequired[dict[str, ServerVariable]]


class PathItem(TypedDict):
    ref: NotRequired[str]
    summary: NotRequired[str]
    description: NotRequired[str]
    get: NotRequired[Operation]
    put: NotRequired[Operation]
    post: NotRequired[Operation]
    delete: NotRequired[Operation]
    options: NotRequired[Operation]
    head: NotRequired[Operation]
    patch: NotRequired[Operation]
    trace: NotRequired[Operation]
    servers: NotRequired[list[Server]]
    parameters: NotRequired[list[Parameter | Reference]]


class SecurityScheme(TypedDict):
    type: str
    description: NotRequired[str]
    name: NotRequired[str]
    in_: NotRequired[str]
    scheme: NotRequired[str]
    bearerFormat: NotRequired[str]
    flows: NotRequired["OAuthFlows"]  # Forward reference
    openIdConnectUrl: NotRequired[AnyUrl]


class OAuthFlows(TypedDict):
    implicit: NotRequired["OAuthFlow"]
    password: NotRequired["OAuthFlow"]
    clientCredentials: NotRequired["OAuthFlow"]
    authorizationCode: NotRequired["OAuthFlow"]


class OAuthFlow(TypedDict):
    authorizationUrl: NotRequired[AnyUrl]
    tokenUrl: NotRequired[AnyUrl]
    refreshUrl: NotRequired[AnyUrl]
    scopes: dict[str, str]


class Components(TypedDict):
    schemas: NotRequired[dict[str, Schema | Reference]]
    responses: NotRequired[dict[str, Response | Reference]]
    parameters: NotRequired[dict[str, Parameter | Reference]]
    examples: NotRequired[dict[str, Example | Reference]]
    requestBodies: NotRequired[dict[str, RequestBody | Reference]]
    headers: NotRequired[dict[str, Header | Reference]]
    securitySchemes: NotRequired[dict[str, SecurityScheme | Reference]]
    links: NotRequired[dict[str, Link | Reference]]
    callbacks: NotRequired[dict[str, dict[str, "PathItem"]]]


class Tag(TypedDict):
    name: str
    description: NotRequired[str]
    externalDocs: NotRequired[ExternalDocumentation]


class OpenAPI(TypedDict):
    openapi: Literal["3.1.0"]
    info: Info
    jsonSchemaDialect: NotRequired[str]
    servers: NotRequired[list[Server]]
    paths: NotRequired[dict[str, PathItem]]
    webhooks: NotRequired[dict[str, PathItem | Reference]]
    components: NotRequired[Components]
    security: NotRequired[list[dict[str, list[str]]]]
    tags: NotRequired[list[Tag]]
    externalDocs: NotRequired[ExternalDocumentation]


class Contact(TypedDict):
    name: NotRequired[str]
    url: NotRequired[AnyUrl]
    email: NotRequired[str]


class License(TypedDict):
    name: str
    identifier: NotRequired[str]
    url: NotRequired[AnyUrl]


class Info(TypedDict):
    title: str
    summary: NotRequired[str]
    description: NotRequired[str]
    termsOfService: NotRequired[AnyUrl]
    contact: NotRequired[Contact]
    license: NotRequired[License]
    version: str
