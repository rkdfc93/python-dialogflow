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
import warnings
from typing import Callable, Dict, Optional, Sequence, Tuple, Union

from google.api_core import grpc_helpers
from google.api_core import operations_v1
from google.api_core import gapic_v1
import google.auth  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore
from google.auth.transport.grpc import SslCredentials  # type: ignore

import grpc  # type: ignore

from google.cloud.dialogflow_v2.types import entity_type
from google.cloud.dialogflow_v2.types import entity_type as gcd_entity_type
from google.longrunning import operations_pb2  # type: ignore
from google.protobuf import empty_pb2  # type: ignore
from .base import EntityTypesTransport, DEFAULT_CLIENT_INFO


class EntityTypesGrpcTransport(EntityTypesTransport):
    """gRPC backend transport for EntityTypes.

    Service for managing
    [EntityTypes][google.cloud.dialogflow.v2.EntityType].

    This class defines the same methods as the primary client, so the
    primary client can load the underlying transport implementation
    and call it.

    It sends protocol buffers over the wire using gRPC (which is built on
    top of HTTP/2); the ``grpcio`` package must be installed.
    """

    _stubs: Dict[str, Callable]

    def __init__(
        self,
        *,
        host: str = "dialogflow.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Sequence[str] = None,
        channel: grpc.Channel = None,
        api_mtls_endpoint: str = None,
        client_cert_source: Callable[[], Tuple[bytes, bytes]] = None,
        ssl_channel_credentials: grpc.ChannelCredentials = None,
        client_cert_source_for_mtls: Callable[[], Tuple[bytes, bytes]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        always_use_jwt_access: Optional[bool] = False,
    ) -> None:
        """Instantiate the transport.

        Args:
            host (Optional[str]):
                 The hostname to connect to.
            credentials (Optional[google.auth.credentials.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify the application to the service; if none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is ignored if ``channel`` is provided.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is ignored if ``channel`` is provided.
            scopes (Optional(Sequence[str])): A list of scopes. This argument is
                ignored if ``channel`` is provided.
            channel (Optional[grpc.Channel]): A ``Channel`` instance through
                which to make calls.
            api_mtls_endpoint (Optional[str]): Deprecated. The mutual TLS endpoint.
                If provided, it overrides the ``host`` argument and tries to create
                a mutual TLS channel with client SSL credentials from
                ``client_cert_source`` or application default SSL credentials.
            client_cert_source (Optional[Callable[[], Tuple[bytes, bytes]]]):
                Deprecated. A callback to provide client SSL certificate bytes and
                private key bytes, both in PEM format. It is ignored if
                ``api_mtls_endpoint`` is None.
            ssl_channel_credentials (grpc.ChannelCredentials): SSL credentials
                for the grpc channel. It is ignored if ``channel`` is provided.
            client_cert_source_for_mtls (Optional[Callable[[], Tuple[bytes, bytes]]]):
                A callback to provide client certificate bytes and private key bytes,
                both in PEM format. It is used to configure a mutual TLS channel. It is
                ignored if ``channel`` or ``ssl_channel_credentials`` is provided.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            always_use_jwt_access (Optional[bool]): Whether self signed JWT should
                be used for service account credentials.

        Raises:
          google.auth.exceptions.MutualTLSChannelError: If mutual TLS transport
              creation failed for any reason.
          google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """
        self._grpc_channel = None
        self._ssl_channel_credentials = ssl_channel_credentials
        self._stubs: Dict[str, Callable] = {}
        self._operations_client: Optional[operations_v1.OperationsClient] = None

        if api_mtls_endpoint:
            warnings.warn("api_mtls_endpoint is deprecated", DeprecationWarning)
        if client_cert_source:
            warnings.warn("client_cert_source is deprecated", DeprecationWarning)

        if channel:
            # Ignore credentials if a channel was passed.
            credentials = False
            # If a channel was explicitly provided, set it.
            self._grpc_channel = channel
            self._ssl_channel_credentials = None

        else:
            if api_mtls_endpoint:
                host = api_mtls_endpoint

                # Create SSL credentials with client_cert_source or application
                # default SSL credentials.
                if client_cert_source:
                    cert, key = client_cert_source()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )
                else:
                    self._ssl_channel_credentials = SslCredentials().ssl_credentials

            else:
                if client_cert_source_for_mtls and not ssl_channel_credentials:
                    cert, key = client_cert_source_for_mtls()
                    self._ssl_channel_credentials = grpc.ssl_channel_credentials(
                        certificate_chain=cert, private_key=key
                    )

        # The base transport sets the host, credentials and scopes
        super().__init__(
            host=host,
            credentials=credentials,
            credentials_file=credentials_file,
            scopes=scopes,
            quota_project_id=quota_project_id,
            client_info=client_info,
            always_use_jwt_access=always_use_jwt_access,
        )

        if not self._grpc_channel:
            self._grpc_channel = type(self).create_channel(
                self._host,
                # use the credentials which are saved
                credentials=self._credentials,
                # Set ``credentials_file`` to ``None`` here as
                # the credentials that we saved earlier should be used.
                credentials_file=None,
                scopes=self._scopes,
                ssl_credentials=self._ssl_channel_credentials,
                quota_project_id=quota_project_id,
                options=[
                    ("grpc.max_send_message_length", -1),
                    ("grpc.max_receive_message_length", -1),
                ],
            )

        # Wrap messages. This must be done after self._grpc_channel exists
        self._prep_wrapped_messages(client_info)

    @classmethod
    def create_channel(
        cls,
        host: str = "dialogflow.googleapis.com",
        credentials: ga_credentials.Credentials = None,
        credentials_file: str = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        **kwargs,
    ) -> grpc.Channel:
        """Create and return a gRPC channel object.
        Args:
            host (Optional[str]): The host for the channel to use.
            credentials (Optional[~.Credentials]): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A optional list of scopes needed for this
                service. These are only used when credentials are not specified and
                are passed to :func:`google.auth.default`.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            kwargs (Optional[dict]): Keyword arguments, which are passed to the
                channel creation.
        Returns:
            grpc.Channel: A gRPC channel object.

        Raises:
            google.api_core.exceptions.DuplicateCredentialArgs: If both ``credentials``
              and ``credentials_file`` are passed.
        """

        return grpc_helpers.create_channel(
            host,
            credentials=credentials,
            credentials_file=credentials_file,
            quota_project_id=quota_project_id,
            default_scopes=cls.AUTH_SCOPES,
            scopes=scopes,
            default_host=cls.DEFAULT_HOST,
            **kwargs,
        )

    @property
    def grpc_channel(self) -> grpc.Channel:
        """Return the channel designed to connect to this service."""
        return self._grpc_channel

    @property
    def operations_client(self) -> operations_v1.OperationsClient:
        """Create the client designed to process long-running operations.

        This property caches on the instance; repeated calls return the same
        client.
        """
        # Quick check: Only create a new client if we do not already have one.
        if self._operations_client is None:
            self._operations_client = operations_v1.OperationsClient(self.grpc_channel)

        # Return the client from cache.
        return self._operations_client

    @property
    def list_entity_types(
        self,
    ) -> Callable[
        [entity_type.ListEntityTypesRequest], entity_type.ListEntityTypesResponse
    ]:
        r"""Return a callable for the list entity types method over gRPC.

        Returns the list of all entity types in the specified
        agent.

        Returns:
            Callable[[~.ListEntityTypesRequest],
                    ~.ListEntityTypesResponse]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "list_entity_types" not in self._stubs:
            self._stubs["list_entity_types"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/ListEntityTypes",
                request_serializer=entity_type.ListEntityTypesRequest.serialize,
                response_deserializer=entity_type.ListEntityTypesResponse.deserialize,
            )
        return self._stubs["list_entity_types"]

    @property
    def get_entity_type(
        self,
    ) -> Callable[[entity_type.GetEntityTypeRequest], entity_type.EntityType]:
        r"""Return a callable for the get entity type method over gRPC.

        Retrieves the specified entity type.

        Returns:
            Callable[[~.GetEntityTypeRequest],
                    ~.EntityType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "get_entity_type" not in self._stubs:
            self._stubs["get_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/GetEntityType",
                request_serializer=entity_type.GetEntityTypeRequest.serialize,
                response_deserializer=entity_type.EntityType.deserialize,
            )
        return self._stubs["get_entity_type"]

    @property
    def create_entity_type(
        self,
    ) -> Callable[
        [gcd_entity_type.CreateEntityTypeRequest], gcd_entity_type.EntityType
    ]:
        r"""Return a callable for the create entity type method over gRPC.

        Creates an entity type in the specified agent.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        Returns:
            Callable[[~.CreateEntityTypeRequest],
                    ~.EntityType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "create_entity_type" not in self._stubs:
            self._stubs["create_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/CreateEntityType",
                request_serializer=gcd_entity_type.CreateEntityTypeRequest.serialize,
                response_deserializer=gcd_entity_type.EntityType.deserialize,
            )
        return self._stubs["create_entity_type"]

    @property
    def update_entity_type(
        self,
    ) -> Callable[
        [gcd_entity_type.UpdateEntityTypeRequest], gcd_entity_type.EntityType
    ]:
        r"""Return a callable for the update entity type method over gRPC.

        Updates the specified entity type.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        Returns:
            Callable[[~.UpdateEntityTypeRequest],
                    ~.EntityType]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "update_entity_type" not in self._stubs:
            self._stubs["update_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/UpdateEntityType",
                request_serializer=gcd_entity_type.UpdateEntityTypeRequest.serialize,
                response_deserializer=gcd_entity_type.EntityType.deserialize,
            )
        return self._stubs["update_entity_type"]

    @property
    def delete_entity_type(
        self,
    ) -> Callable[[entity_type.DeleteEntityTypeRequest], empty_pb2.Empty]:
        r"""Return a callable for the delete entity type method over gRPC.

        Deletes the specified entity type.

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        Returns:
            Callable[[~.DeleteEntityTypeRequest],
                    ~.Empty]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "delete_entity_type" not in self._stubs:
            self._stubs["delete_entity_type"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/DeleteEntityType",
                request_serializer=entity_type.DeleteEntityTypeRequest.serialize,
                response_deserializer=empty_pb2.Empty.FromString,
            )
        return self._stubs["delete_entity_type"]

    @property
    def batch_update_entity_types(
        self,
    ) -> Callable[
        [entity_type.BatchUpdateEntityTypesRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the batch update entity types method over gRPC.

        Updates/Creates multiple entity types in the specified agent.

        This method is a `long-running
        operation <https://cloud.google.com/dialogflow/es/docs/how/long-running-operations>`__.
        The returned ``Operation`` type has the following
        method-specific fields:

        -  ``metadata``: An empty `Struct
           message <https://developers.google.com/protocol-buffers/docs/reference/google.protobuf#struct>`__
        -  ``response``:
           [BatchUpdateEntityTypesResponse][google.cloud.dialogflow.v2.BatchUpdateEntityTypesResponse]

        Note: You should always train an agent prior to sending it
        queries. See the `training
        documentation <https://cloud.google.com/dialogflow/es/docs/training>`__.

        Returns:
            Callable[[~.BatchUpdateEntityTypesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_entity_types" not in self._stubs:
            self._stubs["batch_update_entity_types"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchUpdateEntityTypes",
                request_serializer=entity_type.BatchUpdateEntityTypesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_update_entity_types"]

    @property
    def batch_delete_entity_types(
        self,
    ) -> Callable[
        [entity_type.BatchDeleteEntityTypesRequest], operations_pb2.Operation
    ]:
        r"""Return a callable for the batch delete entity types method over gRPC.

        Deletes entity types in the specified agent.

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

        Returns:
            Callable[[~.BatchDeleteEntityTypesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_entity_types" not in self._stubs:
            self._stubs["batch_delete_entity_types"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchDeleteEntityTypes",
                request_serializer=entity_type.BatchDeleteEntityTypesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_delete_entity_types"]

    @property
    def batch_create_entities(
        self,
    ) -> Callable[[entity_type.BatchCreateEntitiesRequest], operations_pb2.Operation]:
        r"""Return a callable for the batch create entities method over gRPC.

        Creates multiple new entities in the specified entity type.

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

        Returns:
            Callable[[~.BatchCreateEntitiesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_create_entities" not in self._stubs:
            self._stubs["batch_create_entities"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchCreateEntities",
                request_serializer=entity_type.BatchCreateEntitiesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_create_entities"]

    @property
    def batch_update_entities(
        self,
    ) -> Callable[[entity_type.BatchUpdateEntitiesRequest], operations_pb2.Operation]:
        r"""Return a callable for the batch update entities method over gRPC.

        Updates or creates multiple entities in the specified entity
        type. This method does not affect entities in the entity type
        that aren't explicitly specified in the request.

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

        Returns:
            Callable[[~.BatchUpdateEntitiesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_update_entities" not in self._stubs:
            self._stubs["batch_update_entities"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchUpdateEntities",
                request_serializer=entity_type.BatchUpdateEntitiesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_update_entities"]

    @property
    def batch_delete_entities(
        self,
    ) -> Callable[[entity_type.BatchDeleteEntitiesRequest], operations_pb2.Operation]:
        r"""Return a callable for the batch delete entities method over gRPC.

        Deletes entities in the specified entity type.

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

        Returns:
            Callable[[~.BatchDeleteEntitiesRequest],
                    ~.Operation]:
                A function that, when called, will call the underlying RPC
                on the server.
        """
        # Generate a "stub function" on-the-fly which will actually make
        # the request.
        # gRPC handles serialization and deserialization, so we just need
        # to pass in the functions for each.
        if "batch_delete_entities" not in self._stubs:
            self._stubs["batch_delete_entities"] = self.grpc_channel.unary_unary(
                "/google.cloud.dialogflow.v2.EntityTypes/BatchDeleteEntities",
                request_serializer=entity_type.BatchDeleteEntitiesRequest.serialize,
                response_deserializer=operations_pb2.Operation.FromString,
            )
        return self._stubs["batch_delete_entities"]

    def close(self):
        self.grpc_channel.close()


__all__ = ("EntityTypesGrpcTransport",)
