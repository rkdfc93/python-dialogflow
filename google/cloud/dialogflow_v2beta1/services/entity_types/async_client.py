# -*- coding: utf-8 -*-
# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#
from collections import OrderedDict
import functools
import re
from typing import Dict, Optional, Sequence, Tuple, Type, Union
import pkg_resources

from google.api_core.client_options import ClientOptions
from google.api_core import exceptions as core_exceptions
from google.api_core import gapic_v1
from google.api_core import retry as retries
from google.auth import credentials as ga_credentials  # type: ignore
from google.oauth2 import service_account  # type: ignore

try:
    OptionalRetry = Union[retries.Retry, gapic_v1.method._MethodDefault]
except AttributeError:  # pragma: NO COVER
    OptionalRetry = Union[retries.Retry, object]  # type: ignore

from google.api_core import operation  # type: ignore
from google.api_core import operation_async  # type: ignore
from google.cloud.dialogflow_v2beta1.services.entity_types import pagers
from google.cloud.dialogflow_v2beta1.types import entity_type
from google.cloud.dialogflow_v2beta1.types import entity_type as gcd_entity_type
from google.protobuf import empty_pb2  # type: ignore
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from .transports.base import EntityTypesTransport, DEFAULT_CLIENT_INFO
from .transports.grpc_asyncio import EntityTypesGrpcAsyncIOTransport
from .client import EntityTypesClient


class EntityTypesAsyncClient:
    """Service for managing
    [EntityTypes][google.cloud.dialogflow.v2beta1.EntityType].
    """

    _client: EntityTypesClient

    DEFAULT_ENDPOINT = EntityTypesClient.DEFAULT_ENDPOINT
    DEFAULT_MTLS_ENDPOINT = EntityTypesClient.DEFAULT_MTLS_ENDPOINT

    entity_type_path = staticmethod(EntityTypesClient.entity_type_path)
    parse_entity_type_path = staticmethod(EntityTypesClient.parse_entity_type_path)
    common_billing_account_path = staticmethod(
        EntityTypesClient.common_billing_account_path
    )
    parse_common_billing_account_path = staticmethod(
        EntityTypesClient.parse_common_billing_account_path
    )
    common_folder_path = staticmethod(EntityTypesClient.common_folder_path)
    parse_common_folder_path = staticmethod(EntityTypesClient.parse_common_folder_path)
    common_organization_path = staticmethod(EntityTypesClient.common_organization_path)
    parse_common_organization_path = staticmethod(
        EntityTypesClient.parse_common_organization_path
    )
    common_project_path = staticmethod(EntityTypesClient.common_project_path)
    parse_common_project_path = staticmethod(
        EntityTypesClient.parse_common_project_path
    )
    common_location_path = staticmethod(EntityTypesClient.common_location_path)
    parse_common_location_path = staticmethod(
        EntityTypesClient.parse_common_location_path
    )

    @classmethod
    def from_service_account_info(cls, info: dict, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            info.

        Args:
            info (dict): The service account private key info.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EntityTypesAsyncClient: The constructed client.
        """
        return EntityTypesClient.from_service_account_info.__func__(EntityTypesAsyncClient, info, *args, **kwargs)  # type: ignore

    @classmethod
    def from_service_account_file(cls, filename: str, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
            file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            EntityTypesAsyncClient: The constructed client.
        """
        return EntityTypesClient.from_service_account_file.__func__(EntityTypesAsyncClient, filename, *args, **kwargs)  # type: ignore

    from_service_account_json = from_service_account_file

    @classmethod
    def get_mtls_endpoint_and_cert_source(
        cls, client_options: Optional[ClientOptions] = None
    ):
        """Return the API endpoint and client cert source for mutual TLS.

        The client cert source is determined in the following order:
        (1) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is not "true", the
        client cert source is None.
        (2) if `client_options.client_cert_source` is provided, use the provided one; if the
        default client cert source exists, use the default one; otherwise the client cert
        source is None.

        The API endpoint is determined in the following order:
        (1) if `client_options.api_endpoint` if provided, use the provided one.
        (2) if `GOOGLE_API_USE_CLIENT_CERTIFICATE` environment variable is "always", use the
        default mTLS endpoint; if the environment variabel is "never", use the default API
        endpoint; otherwise if client cert source exists, use the default mTLS endpoint, otherwise
        use the default API endpoint.

        More details can be found at https://google.aip.dev/auth/4114.

        Args:
            client_options (google.api_core.client_options.ClientOptions): Custom options for the
                client. Only the `api_endpoint` and `client_cert_source` properties may be used
                in this method.

        Returns:
            Tuple[str, Callable[[], Tuple[bytes, bytes]]]: returns the API endpoint and the
                client cert source to use.

        Raises:
            google.auth.exceptions.MutualTLSChannelError: If any errors happen.
        """
        return EntityTypesClient.get_mtls_endpoint_and_cert_source(client_options)  # type: ignore

    @property
    def transport(self) -> EntityTypesTransport:
        """Returns the transport used by the client instance.

        Returns:
            EntityTypesTransport: The transport used by the client instance.
        """
        return self._client.transport

    get_transport_class = functools.partial(
        type(EntityTypesClient).get_transport_class, type(EntityTypesClient)
    )

    def __init__(
        self,
        *,
        credentials: ga_credentials.Credentials = None,
        transport: Union[str, EntityTypesTransport] = "grpc_asyncio",
        client_options: ClientOptions = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
    ) -> None:
        """Instantiates the entity types client.

        Args:
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            transport (Union[str, ~.EntityTypesTransport]): The
                transport to use. If set to None, a transport is chosen
                automatically.
            client_options (ClientOptions): Custom options for the client. It
                won't take effect if a ``transport`` instance is provided.
                (1) The ``api_endpoint`` property can be used to override the
                default endpoint provided by the client. GOOGLE_API_USE_MTLS_ENDPOINT
                environment variable can also be used to override the endpoint:
                "always" (always use the default mTLS endpoint), "never" (always
                use the default regular endpoint) and "auto" (auto switch to the
                default mTLS endpoint if client certificate is present, this is
                the default value). However, the ``api_endpoint`` property takes
                precedence if provided.
                (2) If GOOGLE_API_USE_CLIENT_CERTIFICATE environment variable
                is "true", then the ``client_cert_source`` property can be used
                to provide client certificate for mutual TLS transport. If
                not provided, the default SSL client certificate will be used if
                present. If GOOGLE_API_USE_CLIENT_CERTIFICATE is "false" or not
                set, no client certificate will be used.

        Raises:
            google.auth.exceptions.MutualTlsChannelError: If mutual TLS transport
                creation failed for any reason.
        """
        self._client = EntityTypesClient(
            credentials=credentials,
            transport=transport,
            client_options=client_options,
            client_info=client_info,
        )

    async def list_entity_types(
        self,
        request: Union[entity_type.ListEntityTypesRequest, dict] = None,
        *,
        parent: str = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> pagers.ListEntityTypesAsyncPager:
        r"""Returns the list of all entity types in the specified
        agent.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_list_entity_types():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.ListEntityTypesRequest(
                    parent="parent_value",
                )

                # Make the request
                page_result = client.list_entity_types(request=request)

                # Handle the response
                for response in page_result:
                    print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.ListEntityTypesRequest, dict]):
                The request object. The request message for
                [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2beta1.EntityTypes.ListEntityTypes].
            parent (:class:`str`):
                Required. The agent to list all entity types from.
                Supported formats:

                -  ``projects/<Project ID>/agent``
                -  ``projects/<Project ID>/locations/<Location ID>/agent``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (:class:`str`):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.services.entity_types.pagers.ListEntityTypesAsyncPager:
                The response message for
                [EntityTypes.ListEntityTypes][google.cloud.dialogflow.v2beta1.EntityTypes.ListEntityTypes].

                Iterating over this object will yield results and
                resolve additional pages automatically.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = entity_type.ListEntityTypesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if language_code is not None:
            request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.list_entity_types,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # This method is paged; wrap the response in a pager, which provides
        # an `__aiter__` convenience method.
        response = pagers.ListEntityTypesAsyncPager(
            method=rpc,
            request=request,
            response=response,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def get_entity_type(
        self,
        request: Union[entity_type.GetEntityTypeRequest, dict] = None,
        *,
        name: str = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> entity_type.EntityType:
        r"""Retrieves the specified entity type.

        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_get_entity_type():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.GetEntityTypeRequest(
                    name="name_value",
                )

                # Make the request
                response = client.get_entity_type(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.GetEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.GetEntityType][google.cloud.dialogflow.v2beta1.EntityTypes.GetEntityType].
            name (:class:`str`):
                Required. The name of the entity type. Supported
                formats:

                -  ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``
                -  ``projects/<Project ID>/locations/<Location ID>/agent/entityTypes/<Entity Type ID>``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (:class:`str`):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.EntityType:
                Each intent parameter has a type, called the entity type, which dictates
                   exactly how data from an end-user expression is
                   extracted.

                   Dialogflow provides predefined system entities that
                   can match many common types of data. For example,
                   there are system entities for matching dates, times,
                   colors, email addresses, and so on. You can also
                   create your own custom entities for matching custom
                   data. For example, you could define a vegetable
                   entity that can match the types of vegetables
                   available for purchase with a grocery store agent.

                   For more information, see the [Entity
                   guide](\ https://cloud.google.com/dialogflow/docs/entities-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = entity_type.GetEntityTypeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name
        if language_code is not None:
            request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.get_entity_type,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def create_entity_type(
        self,
        request: Union[gcd_entity_type.CreateEntityTypeRequest, dict] = None,
        *,
        parent: str = None,
        entity_type: gcd_entity_type.EntityType = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_entity_type.EntityType:
        r"""Creates an entity type in the specified agent.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_create_entity_type():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                entity_type = dialogflow_v2beta1.EntityType()
                entity_type.display_name = "display_name_value"
                entity_type.kind = "KIND_REGEXP"

                request = dialogflow_v2beta1.CreateEntityTypeRequest(
                    parent="parent_value",
                    entity_type=entity_type,
                )

                # Make the request
                response = client.create_entity_type(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.CreateEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.CreateEntityType][google.cloud.dialogflow.v2beta1.EntityTypes.CreateEntityType].
            parent (:class:`str`):
                Required. The agent to create a entity type for.
                Supported formats:

                -  ``projects/<Project ID>/agent``
                -  ``projects/<Project ID>/locations/<Location ID>/agent``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entity_type (:class:`google.cloud.dialogflow_v2beta1.types.EntityType`):
                Required. The entity type to create.
                This corresponds to the ``entity_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (:class:`str`):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.EntityType:
                Each intent parameter has a type, called the entity type, which dictates
                   exactly how data from an end-user expression is
                   extracted.

                   Dialogflow provides predefined system entities that
                   can match many common types of data. For example,
                   there are system entities for matching dates, times,
                   colors, email addresses, and so on. You can also
                   create your own custom entities for matching custom
                   data. For example, you could define a vegetable
                   entity that can match the types of vegetables
                   available for purchase with a grocery store agent.

                   For more information, see the [Entity
                   guide](\ https://cloud.google.com/dialogflow/docs/entities-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entity_type, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_entity_type.CreateEntityTypeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if entity_type is not None:
            request.entity_type = entity_type
        if language_code is not None:
            request.language_code = language_code

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.create_entity_type,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def update_entity_type(
        self,
        request: Union[gcd_entity_type.UpdateEntityTypeRequest, dict] = None,
        *,
        entity_type: gcd_entity_type.EntityType = None,
        language_code: str = None,
        update_mask: field_mask_pb2.FieldMask = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> gcd_entity_type.EntityType:
        r"""Updates the specified entity type.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_update_entity_type():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                entity_type = dialogflow_v2beta1.EntityType()
                entity_type.display_name = "display_name_value"
                entity_type.kind = "KIND_REGEXP"

                request = dialogflow_v2beta1.UpdateEntityTypeRequest(
                    entity_type=entity_type,
                )

                # Make the request
                response = client.update_entity_type(request=request)

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.UpdateEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.UpdateEntityType][google.cloud.dialogflow.v2beta1.EntityTypes.UpdateEntityType].
            entity_type (:class:`google.cloud.dialogflow_v2beta1.types.EntityType`):
                Required. The entity type to update.
                This corresponds to the ``entity_type`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (:class:`str`):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            update_mask (:class:`google.protobuf.field_mask_pb2.FieldMask`):
                Optional. The mask to control which
                fields get updated.

                This corresponds to the ``update_mask`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.cloud.dialogflow_v2beta1.types.EntityType:
                Each intent parameter has a type, called the entity type, which dictates
                   exactly how data from an end-user expression is
                   extracted.

                   Dialogflow provides predefined system entities that
                   can match many common types of data. For example,
                   there are system entities for matching dates, times,
                   colors, email addresses, and so on. You can also
                   create your own custom entities for matching custom
                   data. For example, you could define a vegetable
                   entity that can match the types of vegetables
                   available for purchase with a grocery store agent.

                   For more information, see the [Entity
                   guide](\ https://cloud.google.com/dialogflow/docs/entities-overview).

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([entity_type, language_code, update_mask])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = gcd_entity_type.UpdateEntityTypeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if entity_type is not None:
            request.entity_type = entity_type
        if language_code is not None:
            request.language_code = language_code
        if update_mask is not None:
            request.update_mask = update_mask

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.update_entity_type,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata(
                (("entity_type.name", request.entity_type.name),)
            ),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Done; return the response.
        return response

    async def delete_entity_type(
        self,
        request: Union[entity_type.DeleteEntityTypeRequest, dict] = None,
        *,
        name: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> None:
        r"""Deletes the specified entity type.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_delete_entity_type():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.DeleteEntityTypeRequest(
                    name="name_value",
                )

                # Make the request
                client.delete_entity_type(request=request)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.DeleteEntityTypeRequest, dict]):
                The request object. The request message for
                [EntityTypes.DeleteEntityType][google.cloud.dialogflow.v2beta1.EntityTypes.DeleteEntityType].
            name (:class:`str`):
                Required. The name of the entity type to delete.
                Supported formats:

                -  ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``
                -  ``projects/<Project ID>/locations/<Location ID>/agent/entityTypes/<Entity Type ID>``

                This corresponds to the ``name`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.
        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([name])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = entity_type.DeleteEntityTypeRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if name is not None:
            request.name = name

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.delete_entity_type,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("name", request.name),)),
        )

        # Send the request.
        await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

    async def batch_update_entity_types(
        self,
        request: Union[entity_type.BatchUpdateEntityTypesRequest, dict] = None,
        *,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates/Creates multiple entity types in the specified agent.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``:
           [BatchUpdateEntityTypesResponse][google.cloud.dialogflow.v2beta1.BatchUpdateEntityTypesResponse]

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_batch_update_entity_types():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.BatchUpdateEntityTypesRequest(
                    entity_type_batch_uri="entity_type_batch_uri_value",
                    parent="parent_value",
                )

                # Make the request
                operation = client.batch_update_entity_types(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.BatchUpdateEntityTypesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntityTypes].
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be
                :class:`google.cloud.dialogflow_v2beta1.types.BatchUpdateEntityTypesResponse`
                The response message for
                [EntityTypes.BatchUpdateEntityTypes][google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntityTypes].

        """
        # Create or coerce a protobuf request object.
        request = entity_type.BatchUpdateEntityTypesRequest(request)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_update_entity_types,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            entity_type.BatchUpdateEntityTypesResponse,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    async def batch_delete_entity_types(
        self,
        request: Union[entity_type.BatchDeleteEntityTypesRequest, dict] = None,
        *,
        parent: str = None,
        entity_type_names: Sequence[str] = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes entity types in the specified agent.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_batch_delete_entity_types():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.BatchDeleteEntityTypesRequest(
                    parent="parent_value",
                    entity_type_names=['entity_type_names_value_1', 'entity_type_names_value_2'],
                )

                # Make the request
                operation = client.batch_delete_entity_types(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.BatchDeleteEntityTypesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchDeleteEntityTypes][google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntityTypes].
            parent (:class:`str`):
                Required. The name of the agent to delete all entities
                types for. Supported formats:

                -  ``projects/<Project ID>/agent``,
                -  ``projects/<Project ID>/locations/<Location ID>/agent``.

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entity_type_names (:class:`Sequence[str]`):
                Required. The names entity types to delete. All names
                must point to the same agent as ``parent``.

                This corresponds to the ``entity_type_names`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entity_type_names])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = entity_type.BatchDeleteEntityTypesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if entity_type_names:
            request.entity_type_names.extend(entity_type_names)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_delete_entity_types,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    async def batch_create_entities(
        self,
        request: Union[entity_type.BatchCreateEntitiesRequest, dict] = None,
        *,
        parent: str = None,
        entities: Sequence[entity_type.EntityType.Entity] = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Creates multiple new entities in the specified entity type.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_batch_create_entities():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                entities = dialogflow_v2beta1.Entity()
                entities.value = "value_value"

                request = dialogflow_v2beta1.BatchCreateEntitiesRequest(
                    parent="parent_value",
                    entities=entities,
                )

                # Make the request
                operation = client.batch_create_entities(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.BatchCreateEntitiesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchCreateEntities][google.cloud.dialogflow.v2beta1.EntityTypes.BatchCreateEntities].
            parent (:class:`str`):
                Required. The name of the entity type to create entities
                in. Supported formats:

                -  ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``
                -  ``projects/<Project ID>/locations/<Location ID>/agent/entityTypes/<Entity Type ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entities (:class:`Sequence[google.cloud.dialogflow_v2beta1.types.EntityType.Entity]`):
                Required. The entities to create.
                This corresponds to the ``entities`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (:class:`str`):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entities, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = entity_type.BatchCreateEntitiesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if language_code is not None:
            request.language_code = language_code
        if entities:
            request.entities.extend(entities)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_create_entities,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    async def batch_update_entities(
        self,
        request: Union[entity_type.BatchUpdateEntitiesRequest, dict] = None,
        *,
        parent: str = None,
        entities: Sequence[entity_type.EntityType.Entity] = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Updates or creates multiple entities in the specified entity
        type. This method does not affect entities in the entity type
        that aren't explicitly specified in the request.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_batch_update_entities():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                entities = dialogflow_v2beta1.Entity()
                entities.value = "value_value"

                request = dialogflow_v2beta1.BatchUpdateEntitiesRequest(
                    parent="parent_value",
                    entities=entities,
                )

                # Make the request
                operation = client.batch_update_entities(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.BatchUpdateEntitiesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchUpdateEntities][google.cloud.dialogflow.v2beta1.EntityTypes.BatchUpdateEntities].
            parent (:class:`str`):
                Required. The name of the entity type to update or
                create entities in. Supported formats:

                -  ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``
                -  ``projects/<Project ID>/locations/<Location ID>/agent/entityTypes/<Entity Type ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entities (:class:`Sequence[google.cloud.dialogflow_v2beta1.types.EntityType.Entity]`):
                Required. The entities to update or
                create.

                This corresponds to the ``entities`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (:class:`str`):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entities, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = entity_type.BatchUpdateEntitiesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if language_code is not None:
            request.language_code = language_code
        if entities:
            request.entities.extend(entities)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_update_entities,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    async def batch_delete_entities(
        self,
        request: Union[entity_type.BatchDeleteEntitiesRequest, dict] = None,
        *,
        parent: str = None,
        entity_values: Sequence[str] = None,
        language_code: str = None,
        retry: OptionalRetry = gapic_v1.method.DEFAULT,
        timeout: float = None,
        metadata: Sequence[Tuple[str, str]] = (),
    ) -> operation_async.AsyncOperation:
        r"""Deletes entities in the specified entity type.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``: An `Empty
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#empty>`__

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.


        .. code-block:: python

            from google.cloud import dialogflow_v2beta1

            def sample_batch_delete_entities():
                # Create a client
                client = dialogflow_v2beta1.EntityTypesClient()

                # Initialize request argument(s)
                request = dialogflow_v2beta1.BatchDeleteEntitiesRequest(
                    parent="parent_value",
                    entity_values=['entity_values_value_1', 'entity_values_value_2'],
                )

                # Make the request
                operation = client.batch_delete_entities(request=request)

                print("Waiting for operation to complete...")

                response = operation.result()

                # Handle the response
                print(response)

        Args:
            request (Union[google.cloud.dialogflow_v2beta1.types.BatchDeleteEntitiesRequest, dict]):
                The request object. The request message for
                [EntityTypes.BatchDeleteEntities][google.cloud.dialogflow.v2beta1.EntityTypes.BatchDeleteEntities].
            parent (:class:`str`):
                Required. The name of the entity type to delete entries
                for. Supported formats:

                -  ``projects/<Project ID>/agent/entityTypes/<Entity Type ID>``
                -  ``projects/<Project ID>/locations/<Location ID>/agent/entityTypes/<Entity Type ID>``

                This corresponds to the ``parent`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            entity_values (:class:`Sequence[str]`):
                Required. The reference ``values`` of the entities to
                delete. Note that these are not fully-qualified names,
                i.e. they don't start with ``projects/<Project ID>``.

                This corresponds to the ``entity_values`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            language_code (:class:`str`):
                Optional. The language used to access language-specific
                data. If not specified, the agent's default language is
                used. For more information, see `Multilingual intent and
                entity
                data <https://cloud.google.com/dialogflow/docs/agents-multilingual#intent-entity>`__.

                This corresponds to the ``language_code`` field
                on the ``request`` instance; if ``request`` is provided, this
                should not be set.
            retry (google.api_core.retry.Retry): Designation of what errors, if any,
                should be retried.
            timeout (float): The timeout for this request.
            metadata (Sequence[Tuple[str, str]]): Strings which should be
                sent along with the request as metadata.

        Returns:
            google.api_core.operation_async.AsyncOperation:
                An object representing a long-running operation.

                The result type for the operation will be :class:`google.protobuf.empty_pb2.Empty` A generic empty message that you can re-use to avoid defining duplicated
                   empty messages in your APIs. A typical example is to
                   use it as the request or the response type of an API
                   method. For instance:

                      service Foo {
                         rpc Bar(google.protobuf.Empty) returns
                         (google.protobuf.Empty);

                      }

                   The JSON representation for Empty is empty JSON
                   object {}.

        """
        # Create or coerce a protobuf request object.
        # Quick check: If we got a request object, we should *not* have
        # gotten any keyword arguments that map to the request.
        has_flattened_params = any([parent, entity_values, language_code])
        if request is not None and has_flattened_params:
            raise ValueError(
                "If the `request` argument is set, then none of "
                "the individual field arguments should be set."
            )

        request = entity_type.BatchDeleteEntitiesRequest(request)

        # If we have keyword arguments corresponding to fields on the
        # request, apply these.
        if parent is not None:
            request.parent = parent
        if language_code is not None:
            request.language_code = language_code
        if entity_values:
            request.entity_values.extend(entity_values)

        # Wrap the RPC method; this adds retry and timeout information,
        # and friendly error handling.
        rpc = gapic_v1.method_async.wrap_method(
            self._client._transport.batch_delete_entities,
            default_timeout=None,
            client_info=DEFAULT_CLIENT_INFO,
        )

        # Certain fields should be provided within the metadata header;
        # add these here.
        metadata = tuple(metadata) + (
            gapic_v1.routing_header.to_grpc_metadata((("parent", request.parent),)),
        )

        # Send the request.
        response = await rpc(
            request,
            retry=retry,
            timeout=timeout,
            metadata=metadata,
        )

        # Wrap the response in an operation future.
        response = operation_async.from_gapic(
            response,
            self._client._transport.operations_client,
            empty_pb2.Empty,
            metadata_type=struct_pb2.Struct,
        )

        # Done; return the response.
        return response

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await self.transport.close()


try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dialogflow",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()


__all__ = ("EntityTypesAsyncClient",)
