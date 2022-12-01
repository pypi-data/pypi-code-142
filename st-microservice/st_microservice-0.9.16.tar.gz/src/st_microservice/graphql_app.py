from typing import Any, Mapping
import asyncio
from datetime import date, datetime
from graphql import GraphQLField, GraphQLObjectType, GraphQLInterfaceType, GraphQLResolveInfo, MiddlewareManager
from ariadne import load_schema_from_path, make_executable_schema, SchemaDirectiveVisitor, FallbackResolversSetter, \
    ScalarType
from ariadne.graphql import GraphQLError
from ariadne.asgi import GraphQL
from ariadne.asgi.handlers import GraphQLHTTPHandler, GraphQLTransportWSHandler
from ariadne.types import Extension, SchemaBindable

from .auth_utils import get_token_from_header, get_user_from_token, JWTAuthBackend, AuthCredentials


# Directives

class NoAuthenticationDirective(SchemaDirectiveVisitor):
    def visit_field_definition(
            self,
            field: GraphQLField,
            object_type: GraphQLObjectType | GraphQLInterfaceType,
    ) -> GraphQLField:
        field.__require_authentication__ = False
        return field

    def visit_object(self, object_: GraphQLObjectType) -> GraphQLObjectType:
        object_.__require_authentication__ = False
        return object_


class NeedPermissionDirective(SchemaDirectiveVisitor):
    def visit_field_definition(
        self,
        field: GraphQLField,
        object_type: GraphQLObjectType | GraphQLInterfaceType,
    ) -> GraphQLField:
        if self.args['strict'] or object_type.name == 'Mutation' or object_type.name == 'Subscription':
            field.__require_scope__ = self.args['scope']
        else:
            field.__hide_noscope__ = self.args['scope']
        return field

    def visit_object(self, object_: GraphQLObjectType) -> GraphQLObjectType:
        if self.args['strict']:
            object_.__require_scope__ = self.args['scope']
        else:
            object_.__hide_noscope__ = self.args['scope']
        return object_


class DBModelDirective(SchemaDirectiveVisitor):
    def visit_object(self, object_: GraphQLObjectType) -> GraphQLObjectType:
        object_.__db_model__ = True
        object_.__primary_keys__ = self.args['primary_keys']
        return object_


class AllFilterDirective(SchemaDirectiveVisitor):
    def visit_object(self, object_: GraphQLObjectType) -> GraphQLObjectType:
        object_.__all_filter__ = True
        return object_


class FilterDirective(SchemaDirectiveVisitor):
    def visit_field_definition(
        self,
        field: GraphQLField,
        object_type: GraphQLObjectType | GraphQLInterfaceType,
    ) -> GraphQLField:
        field.__filter__ = True
        return field


class NoFilterDirective(SchemaDirectiveVisitor):
    def visit_field_definition(
        self,
        field: GraphQLField,
        object_type: GraphQLObjectType | GraphQLInterfaceType,
    ) -> GraphQLField:
        field.__filter__ = False
        return field


# Middleware

class HideResult(BaseException):
    pass


def check_permission(info: GraphQLResolveInfo):
    if info.field_name != '__schema':
        request = info.context['request']
        field = info.parent_type.fields[info.field_name]

        # Check for Authentication
        if hasattr(field, '__require_authentication__'):
            needs_auth = field.__require_authentication__
        elif hasattr(info.parent_type, '__require_authentication__'):
            needs_auth = info.parent_type.__require_authentication__
        else:
            needs_auth = True

        if needs_auth and not request.user.is_authenticated:
            raise GraphQLError(message='Requires Authentication')

        # check for Strict Permission
        if hasattr(field, '__require_scope__'):
            needs_scope = field.__require_scope__
        elif hasattr(info.parent_type, '__require_scope__'):
            needs_scope = info.parent_type.__require_scope__
        else:
            needs_scope = None

        if needs_scope is not None and needs_scope not in request.auth.scopes:
            raise GraphQLError(message=f'Requires Scope: {needs_scope}')

        # check for Loose Permission
        if hasattr(field, '__hide_noscope__'):
            hide_noscope = field.__hide_noscope__
        elif hasattr(info.parent_type, '__hide_noscope__'):
            hide_noscope = info.parent_type.__hide_noscope__
        else:
            hide_noscope = None

        if hide_noscope is not None and hide_noscope not in request.auth.scopes:
            raise HideResult()


async def check_permission_middleware(resolver, obj, info: GraphQLResolveInfo, **args):
    try:
        check_permission(info)
    except HideResult:
        return None

    # Return resolver
    if asyncio.iscoroutinefunction(resolver):
        return await resolver(obj, info, **args)
    else:
        return resolver(obj, info, **args)


class DBRollbackExtension(Extension):
    def has_errors(self, errors, context) -> None:
        context['request'].state.dbsession.rollback()


# Custom Scalars

date_scalar = ScalarType("Date")


@date_scalar.serializer
def serialize_date(value: date):
    return value.isoformat()


@date_scalar.value_parser
def parse_date(value: str):
    return date.fromisoformat(value)


datetime_scalar = ScalarType("DateTime")


@datetime_scalar.serializer
def serialize_datetime(value: datetime):
    return value.isoformat()


@datetime_scalar.value_parser
def parse_datetime(value: str):
    return date.fromisoformat(value)


# Fallback Resolver

def strict_default_field_resolver(source: Any, info: GraphQLResolveInfo, **args: Any) -> Any:
    """Strict Default field resolver.
    Same as default but raise Error when atrribute doesn't exist instead of returning None
    """
    field_name = info.field_name
    try:
        value = (
            source[field_name]
            if isinstance(source, Mapping)
            else getattr(source, field_name)
        )
    except (KeyError, AttributeError):
        raise GraphQLError(f"Attribute {field_name} does not exist on {info.parent_type.name} object")

    if callable(value):
        return value(info, **args)
    return value


class StrictFallbackResolverSetter(FallbackResolversSetter):
    def add_resolver_to_field(self, _: str, field_object: GraphQLField) -> None:
        if field_object.resolve is None:
            field_object.resolve = strict_default_field_resolver


def on_websocket_connect(websocket, payload: Any):
    """ Alternative to Header authentication if cookie auth cannot be used """
    if not isinstance(payload, Mapping) or 'Authorization' not in payload:
        return
    token = get_token_from_header(payload['Authorization'])

    for middleware in websocket.scope['app'].user_middleware:
        auth_backend = middleware.options.get('backend')
        if isinstance(auth_backend, JWTAuthBackend):
            user = get_user_from_token(token, auth_backend.secret)
            websocket.scope['user'] = user
            websocket.scope['auth'] = AuthCredentials(user.scopes)
            break


# Exported

def create_graphql(schema_path, bindables: list[SchemaBindable], debug: bool):
    fallback_resolvers = StrictFallbackResolverSetter()
    type_defs = load_schema_from_path(schema_path)

    schema = make_executable_schema(type_defs, bindables, date_scalar, datetime_scalar, fallback_resolvers, directives={
        'no_authentication': NoAuthenticationDirective,
        'need_permission': NeedPermissionDirective,
        'db_model': DBModelDirective,
        'all_filter': AllFilterDirective,
        'filter': FilterDirective,
        'no_filter': NoFilterDirective
    })

    return GraphQL(
        schema,
        debug=debug,
        http_handler=GraphQLHTTPHandler(
            middleware=[check_permission_middleware],
            extensions=[DBRollbackExtension]
        ),
        websocket_handler=GraphQLTransportWSHandler(on_connect=on_websocket_connect)
    )
