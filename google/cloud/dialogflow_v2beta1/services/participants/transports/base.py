# -*- coding: utf-8 -*-
# Copyright 2020 Google LLC
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
import abc
from typing import Awaitable, Callable, Dict, Optional, Sequence, Union
import packaging.version
import pkg_resources

import google.auth  # type: ignore
import google.api_core  # type: ignore
from google.api_core import exceptions as core_exceptions  # type: ignore
from google.api_core import gapic_v1  # type: ignore
from google.api_core import retry as retries  # type: ignore
from google.auth import credentials as ga_credentials  # type: ignore

from google.cloud.dialogflow_v2beta1.types import participant
from google.cloud.dialogflow_v2beta1.types import participant as gcd_participant

try:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo(
        gapic_version=pkg_resources.get_distribution(
            "google-cloud-dialogflow",
        ).version,
    )
except pkg_resources.DistributionNotFound:
    DEFAULT_CLIENT_INFO = gapic_v1.client_info.ClientInfo()

try:
    # google.auth.__version__ was added in 1.26.0
    _GOOGLE_AUTH_VERSION = google.auth.__version__
except AttributeError:
    try:  # try pkg_resources if it is available
        _GOOGLE_AUTH_VERSION = pkg_resources.get_distribution("google-auth").version
    except pkg_resources.DistributionNotFound:  # pragma: NO COVER
        _GOOGLE_AUTH_VERSION = None

_API_CORE_VERSION = google.api_core.__version__


class ParticipantsTransport(abc.ABC):
    """Abstract transport class for Participants."""

    AUTH_SCOPES = (
        "https://www.googleapis.com/auth/cloud-platform",
        "https://www.googleapis.com/auth/dialogflow",
    )

    DEFAULT_HOST: str = "dialogflow.googleapis.com"

    def __init__(
        self,
        *,
        host: str = DEFAULT_HOST,
        credentials: ga_credentials.Credentials = None,
        credentials_file: Optional[str] = None,
        scopes: Optional[Sequence[str]] = None,
        quota_project_id: Optional[str] = None,
        client_info: gapic_v1.client_info.ClientInfo = DEFAULT_CLIENT_INFO,
        **kwargs,
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
            credentials_file (Optional[str]): A file with credentials that can
                be loaded with :func:`google.auth.load_credentials_from_file`.
                This argument is mutually exclusive with credentials.
            scopes (Optional[Sequence[str]]): A list of scopes.
            quota_project_id (Optional[str]): An optional project to use for billing
                and quota.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
        """
        # Save the hostname. Default to port 443 (HTTPS) if none is specified.
        if ":" not in host:
            host += ":443"
        self._host = host

        scopes_kwargs = self._get_scopes_kwargs(self._host, scopes)

        # Save the scopes.
        self._scopes = scopes or self.AUTH_SCOPES

        # If no credentials are provided, then determine the appropriate
        # defaults.
        if credentials and credentials_file:
            raise core_exceptions.DuplicateCredentialArgs(
                "'credentials_file' and 'credentials' are mutually exclusive"
            )

        if credentials_file is not None:
            credentials, _ = google.auth.load_credentials_from_file(
                credentials_file, **scopes_kwargs, quota_project_id=quota_project_id
            )

        elif credentials is None:
            credentials, _ = google.auth.default(
                **scopes_kwargs, quota_project_id=quota_project_id
            )

        # Save the credentials.
        self._credentials = credentials

    # TODO(busunkim): These two class methods are in the base transport
    # to avoid duplicating code across the transport classes. These functions
    # should be deleted once the minimum required versions of google-api-core
    # and google-auth are increased.

    # TODO: Remove this function once google-auth >= 1.25.0 is required
    @classmethod
    def _get_scopes_kwargs(
        cls, host: str, scopes: Optional[Sequence[str]]
    ) -> Dict[str, Optional[Sequence[str]]]:
        """Returns scopes kwargs to pass to google-auth methods depending on the google-auth version"""

        scopes_kwargs = {}

        if _GOOGLE_AUTH_VERSION and (
            packaging.version.parse(_GOOGLE_AUTH_VERSION)
            >= packaging.version.parse("1.25.0")
        ):
            scopes_kwargs = {"scopes": scopes, "default_scopes": cls.AUTH_SCOPES}
        else:
            scopes_kwargs = {"scopes": scopes or cls.AUTH_SCOPES}

        return scopes_kwargs

    # TODO: Remove this function once google-api-core >= 1.26.0 is required
    @classmethod
    def _get_self_signed_jwt_kwargs(
        cls, host: str, scopes: Optional[Sequence[str]]
    ) -> Dict[str, Union[Optional[Sequence[str]], str]]:
        """Returns kwargs to pass to grpc_helpers.create_channel depending on the google-api-core version"""

        self_signed_jwt_kwargs: Dict[str, Union[Optional[Sequence[str]], str]] = {}

        if _API_CORE_VERSION and (
            packaging.version.parse(_API_CORE_VERSION)
            >= packaging.version.parse("1.26.0")
        ):
            self_signed_jwt_kwargs["default_scopes"] = cls.AUTH_SCOPES
            self_signed_jwt_kwargs["scopes"] = scopes
            self_signed_jwt_kwargs["default_host"] = cls.DEFAULT_HOST
        else:
            self_signed_jwt_kwargs["scopes"] = scopes or cls.AUTH_SCOPES

        return self_signed_jwt_kwargs

    def _prep_wrapped_messages(self, client_info):
        # Precompute the wrapped methods.
        self._wrapped_methods = {
            self.create_participant: gapic_v1.method.wrap_method(
                self.create_participant, default_timeout=None, client_info=client_info,
            ),
            self.get_participant: gapic_v1.method.wrap_method(
                self.get_participant, default_timeout=None, client_info=client_info,
            ),
            self.list_participants: gapic_v1.method.wrap_method(
                self.list_participants, default_timeout=None, client_info=client_info,
            ),
            self.update_participant: gapic_v1.method.wrap_method(
                self.update_participant, default_timeout=None, client_info=client_info,
            ),
            self.analyze_content: gapic_v1.method.wrap_method(
                self.analyze_content,
                default_retry=retries.Retry(
                    initial=0.1,
                    maximum=60.0,
                    multiplier=1.3,
                    predicate=retries.if_exception_type(
                        core_exceptions.ServiceUnavailable,
                    ),
                    deadline=220.0,
                ),
                default_timeout=220.0,
                client_info=client_info,
            ),
            self.suggest_articles: gapic_v1.method.wrap_method(
                self.suggest_articles, default_timeout=None, client_info=client_info,
            ),
            self.suggest_faq_answers: gapic_v1.method.wrap_method(
                self.suggest_faq_answers, default_timeout=None, client_info=client_info,
            ),
            self.suggest_smart_replies: gapic_v1.method.wrap_method(
                self.suggest_smart_replies,
                default_timeout=None,
                client_info=client_info,
            ),
            self.list_suggestions: gapic_v1.method.wrap_method(
                self.list_suggestions, default_timeout=None, client_info=client_info,
            ),
            self.compile_suggestion: gapic_v1.method.wrap_method(
                self.compile_suggestion, default_timeout=None, client_info=client_info,
            ),
        }

    @property
    def create_participant(
        self,
    ) -> Callable[
        [gcd_participant.CreateParticipantRequest],
        Union[gcd_participant.Participant, Awaitable[gcd_participant.Participant]],
    ]:
        raise NotImplementedError()

    @property
    def get_participant(
        self,
    ) -> Callable[
        [participant.GetParticipantRequest],
        Union[participant.Participant, Awaitable[participant.Participant]],
    ]:
        raise NotImplementedError()

    @property
    def list_participants(
        self,
    ) -> Callable[
        [participant.ListParticipantsRequest],
        Union[
            participant.ListParticipantsResponse,
            Awaitable[participant.ListParticipantsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def update_participant(
        self,
    ) -> Callable[
        [gcd_participant.UpdateParticipantRequest],
        Union[gcd_participant.Participant, Awaitable[gcd_participant.Participant]],
    ]:
        raise NotImplementedError()

    @property
    def analyze_content(
        self,
    ) -> Callable[
        [gcd_participant.AnalyzeContentRequest],
        Union[
            gcd_participant.AnalyzeContentResponse,
            Awaitable[gcd_participant.AnalyzeContentResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def suggest_articles(
        self,
    ) -> Callable[
        [participant.SuggestArticlesRequest],
        Union[
            participant.SuggestArticlesResponse,
            Awaitable[participant.SuggestArticlesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def suggest_faq_answers(
        self,
    ) -> Callable[
        [participant.SuggestFaqAnswersRequest],
        Union[
            participant.SuggestFaqAnswersResponse,
            Awaitable[participant.SuggestFaqAnswersResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def suggest_smart_replies(
        self,
    ) -> Callable[
        [participant.SuggestSmartRepliesRequest],
        Union[
            participant.SuggestSmartRepliesResponse,
            Awaitable[participant.SuggestSmartRepliesResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def list_suggestions(
        self,
    ) -> Callable[
        [participant.ListSuggestionsRequest],
        Union[
            participant.ListSuggestionsResponse,
            Awaitable[participant.ListSuggestionsResponse],
        ],
    ]:
        raise NotImplementedError()

    @property
    def compile_suggestion(
        self,
    ) -> Callable[
        [participant.CompileSuggestionRequest],
        Union[
            participant.CompileSuggestionResponse,
            Awaitable[participant.CompileSuggestionResponse],
        ],
    ]:
        raise NotImplementedError()


__all__ = ("ParticipantsTransport",)