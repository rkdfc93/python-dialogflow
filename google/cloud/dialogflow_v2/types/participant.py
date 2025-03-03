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
import proto  # type: ignore

from google.cloud.dialogflow_v2.types import audio_config
from google.cloud.dialogflow_v2.types import session
from google.protobuf import field_mask_pb2  # type: ignore
from google.protobuf import struct_pb2  # type: ignore
from google.protobuf import timestamp_pb2  # type: ignore
from google.rpc import status_pb2  # type: ignore


__protobuf__ = proto.module(
    package="google.cloud.dialogflow.v2",
    manifest={
        "Participant",
        "Message",
        "CreateParticipantRequest",
        "GetParticipantRequest",
        "ListParticipantsRequest",
        "ListParticipantsResponse",
        "UpdateParticipantRequest",
        "AnalyzeContentRequest",
        "DtmfParameters",
        "AnalyzeContentResponse",
        "SuggestArticlesRequest",
        "SuggestArticlesResponse",
        "SuggestFaqAnswersRequest",
        "SuggestFaqAnswersResponse",
        "SuggestSmartRepliesRequest",
        "SuggestSmartRepliesResponse",
        "OutputAudio",
        "AutomatedAgentReply",
        "ArticleAnswer",
        "FaqAnswer",
        "SmartReplyAnswer",
        "SuggestionResult",
        "AnnotatedMessagePart",
        "MessageAnnotation",
        "AssistQueryParameters",
    },
)


class Participant(proto.Message):
    r"""Represents a conversation participant (human agent, virtual
    agent, end-user).

    Attributes:
        name (str):
            Optional. The unique identifier of this participant. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        role (google.cloud.dialogflow_v2.types.Participant.Role):
            Immutable. The role this participant plays in
            the conversation. This field must be set during
            participant creation and is then immutable.
        sip_recording_media_label (str):
            Optional. Label applied to streams
            representing this participant in SIPREC XML
            metadata and SDP. This is used to assign
            transcriptions from that media stream to this
            participant. This field can be updated.
        documents_metadata_filters (Sequence[google.cloud.dialogflow_v2.types.Participant.DocumentsMetadataFiltersEntry]):
            Optional. Key-value filters on the metadata of documents
            returned by article suggestion. If specified, article
            suggestion only returns suggested documents that match all
            filters in their
            [Document.metadata][google.cloud.dialogflow.v2.Document.metadata].
            Multiple values for a metadata key should be concatenated by
            comma. For example, filters to match all documents that have
            'US' or 'CA' in their market metadata values and 'agent' in
            their user metadata values will be

            ::

               documents_metadata_filters {
                 key: "market"
                 value: "US,CA"
               }
               documents_metadata_filters {
                 key: "user"
                 value: "agent"
               }
    """

    class Role(proto.Enum):
        r"""Enumeration of the roles a participant can play in a
        conversation.
        """
        ROLE_UNSPECIFIED = 0
        HUMAN_AGENT = 1
        AUTOMATED_AGENT = 2
        END_USER = 3

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    role = proto.Field(
        proto.ENUM,
        number=2,
        enum=Role,
    )
    sip_recording_media_label = proto.Field(
        proto.STRING,
        number=6,
    )
    documents_metadata_filters = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=8,
    )


class Message(proto.Message):
    r"""Represents a message posted into a conversation.

    Attributes:
        name (str):
            Optional. The unique identifier of the message. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        content (str):
            Required. The message content.
        language_code (str):
            Optional. The message language. This should be a
            `BCP-47 <https://www.rfc-editor.org/rfc/bcp/bcp47.txt>`__
            language tag. Example: "en-US".
        participant (str):
            Output only. The participant that sends this
            message.
        participant_role (google.cloud.dialogflow_v2.types.Participant.Role):
            Output only. The role of the participant.
        create_time (google.protobuf.timestamp_pb2.Timestamp):
            Output only. The time when the message was
            created in Contact Center AI.
        send_time (google.protobuf.timestamp_pb2.Timestamp):
            Optional. The time when the message was sent.
        message_annotation (google.cloud.dialogflow_v2.types.MessageAnnotation):
            Output only. The annotation for the message.
        sentiment_analysis (google.cloud.dialogflow_v2.types.SentimentAnalysisResult):
            Output only. The sentiment analysis result
            for the message.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )
    content = proto.Field(
        proto.STRING,
        number=2,
    )
    language_code = proto.Field(
        proto.STRING,
        number=3,
    )
    participant = proto.Field(
        proto.STRING,
        number=4,
    )
    participant_role = proto.Field(
        proto.ENUM,
        number=5,
        enum="Participant.Role",
    )
    create_time = proto.Field(
        proto.MESSAGE,
        number=6,
        message=timestamp_pb2.Timestamp,
    )
    send_time = proto.Field(
        proto.MESSAGE,
        number=9,
        message=timestamp_pb2.Timestamp,
    )
    message_annotation = proto.Field(
        proto.MESSAGE,
        number=7,
        message="MessageAnnotation",
    )
    sentiment_analysis = proto.Field(
        proto.MESSAGE,
        number=8,
        message=session.SentimentAnalysisResult,
    )


class CreateParticipantRequest(proto.Message):
    r"""The request message for
    [Participants.CreateParticipant][google.cloud.dialogflow.v2.Participants.CreateParticipant].

    Attributes:
        parent (str):
            Required. Resource identifier of the conversation adding the
            participant. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        participant (google.cloud.dialogflow_v2.types.Participant):
            Required. The participant to create.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    participant = proto.Field(
        proto.MESSAGE,
        number=2,
        message="Participant",
    )


class GetParticipantRequest(proto.Message):
    r"""The request message for
    [Participants.GetParticipant][google.cloud.dialogflow.v2.Participants.GetParticipant].

    Attributes:
        name (str):
            Required. The name of the participant. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
    """

    name = proto.Field(
        proto.STRING,
        number=1,
    )


class ListParticipantsRequest(proto.Message):
    r"""The request message for
    [Participants.ListParticipants][google.cloud.dialogflow.v2.Participants.ListParticipants].

    Attributes:
        parent (str):
            Required. The conversation to list all participants from.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>``.
        page_size (int):
            Optional. The maximum number of items to
            return in a single page. By default 100 and at
            most 1000.
        page_token (str):
            Optional. The next_page_token value returned from a previous
            list request.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    page_size = proto.Field(
        proto.INT32,
        number=2,
    )
    page_token = proto.Field(
        proto.STRING,
        number=3,
    )


class ListParticipantsResponse(proto.Message):
    r"""The response message for
    [Participants.ListParticipants][google.cloud.dialogflow.v2.Participants.ListParticipants].

    Attributes:
        participants (Sequence[google.cloud.dialogflow_v2.types.Participant]):
            The list of participants. There is a maximum number of items
            returned based on the page_size field in the request.
        next_page_token (str):
            Token to retrieve the next page of results or
            empty if there are no more results in the list.
    """

    @property
    def raw_page(self):
        return self

    participants = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="Participant",
    )
    next_page_token = proto.Field(
        proto.STRING,
        number=2,
    )


class UpdateParticipantRequest(proto.Message):
    r"""The request message for
    [Participants.UpdateParticipant][google.cloud.dialogflow.v2.Participants.UpdateParticipant].

    Attributes:
        participant (google.cloud.dialogflow_v2.types.Participant):
            Required. The participant to update.
        update_mask (google.protobuf.field_mask_pb2.FieldMask):
            Required. The mask to specify which fields to
            update.
    """

    participant = proto.Field(
        proto.MESSAGE,
        number=1,
        message="Participant",
    )
    update_mask = proto.Field(
        proto.MESSAGE,
        number=2,
        message=field_mask_pb2.FieldMask,
    )


class AnalyzeContentRequest(proto.Message):
    r"""The request message for
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        participant (str):
            Required. The name of the participant this text comes from.
            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        text_input (google.cloud.dialogflow_v2.types.TextInput):
            The natural language text to be processed.

            This field is a member of `oneof`_ ``input``.
        event_input (google.cloud.dialogflow_v2.types.EventInput):
            An input event to send to Dialogflow.

            This field is a member of `oneof`_ ``input``.
        reply_audio_config (google.cloud.dialogflow_v2.types.OutputAudioConfig):
            Speech synthesis configuration.
            The speech synthesis settings for a virtual
            agent that may be configured for the associated
            conversation profile are not used when calling
            AnalyzeContent. If this configuration is not
            supplied, speech synthesis is disabled.
        query_params (google.cloud.dialogflow_v2.types.QueryParameters):
            Parameters for a Dialogflow virtual-agent
            query.
        assist_query_params (google.cloud.dialogflow_v2.types.AssistQueryParameters):
            Parameters for a human assist query.
        request_id (str):
            A unique identifier for this request. Restricted to 36 ASCII
            characters. A random UUID is recommended. This request is
            only idempotent if a ``request_id`` is provided.
    """

    participant = proto.Field(
        proto.STRING,
        number=1,
    )
    text_input = proto.Field(
        proto.MESSAGE,
        number=6,
        oneof="input",
        message=session.TextInput,
    )
    event_input = proto.Field(
        proto.MESSAGE,
        number=8,
        oneof="input",
        message=session.EventInput,
    )
    reply_audio_config = proto.Field(
        proto.MESSAGE,
        number=5,
        message=audio_config.OutputAudioConfig,
    )
    query_params = proto.Field(
        proto.MESSAGE,
        number=9,
        message=session.QueryParameters,
    )
    assist_query_params = proto.Field(
        proto.MESSAGE,
        number=14,
        message="AssistQueryParameters",
    )
    request_id = proto.Field(
        proto.STRING,
        number=11,
    )


class DtmfParameters(proto.Message):
    r"""The message in the response that indicates the parameters of
    DTMF.

    Attributes:
        accepts_dtmf_input (bool):
            Indicates whether DTMF input can be handled
            in the next request.
    """

    accepts_dtmf_input = proto.Field(
        proto.BOOL,
        number=1,
    )


class AnalyzeContentResponse(proto.Message):
    r"""The response message for
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent].

    Attributes:
        reply_text (str):
            The output text content.
            This field is set if the automated agent
            responded with text to show to the user.
        reply_audio (google.cloud.dialogflow_v2.types.OutputAudio):
            The audio data bytes encoded as specified in the request.
            This field is set if:

            -  ``reply_audio_config`` was specified in the request, or
            -  The automated agent responded with audio to play to the
               user. In such case, ``reply_audio.config`` contains
               settings used to synthesize the speech.

            In some scenarios, multiple output audio fields may be
            present in the response structure. In these cases, only the
            top-most-level audio output has content.
        automated_agent_reply (google.cloud.dialogflow_v2.types.AutomatedAgentReply):
            Only set if a Dialogflow automated agent has responded. Note
            that:
            [AutomatedAgentReply.detect_intent_response.output_audio][]
            and
            [AutomatedAgentReply.detect_intent_response.output_audio_config][]
            are always empty, use
            [reply_audio][google.cloud.dialogflow.v2.AnalyzeContentResponse.reply_audio]
            instead.
        message (google.cloud.dialogflow_v2.types.Message):
            Message analyzed by CCAI.
        human_agent_suggestion_results (Sequence[google.cloud.dialogflow_v2.types.SuggestionResult]):
            The suggestions for most recent human agent. The order is
            the same as
            [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs]
            of
            [HumanAgentAssistantConfig.human_agent_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.human_agent_suggestion_config].

            Note that any failure of Agent Assist features will not lead
            to the overall failure of an AnalyzeContent API call.
            Instead, the features will fail silently with the error
            field set in the corresponding SuggestionResult.
        end_user_suggestion_results (Sequence[google.cloud.dialogflow_v2.types.SuggestionResult]):
            The suggestions for end user. The order is the same as
            [HumanAgentAssistantConfig.SuggestionConfig.feature_configs][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.SuggestionConfig.feature_configs]
            of
            [HumanAgentAssistantConfig.end_user_suggestion_config][google.cloud.dialogflow.v2.HumanAgentAssistantConfig.end_user_suggestion_config].

            Same as human_agent_suggestion_results, any failure of Agent
            Assist features will not lead to the overall failure of an
            AnalyzeContent API call. Instead, the features will fail
            silently with the error field set in the corresponding
            SuggestionResult.
        dtmf_parameters (google.cloud.dialogflow_v2.types.DtmfParameters):
            Indicates the parameters of DTMF.
    """

    reply_text = proto.Field(
        proto.STRING,
        number=1,
    )
    reply_audio = proto.Field(
        proto.MESSAGE,
        number=2,
        message="OutputAudio",
    )
    automated_agent_reply = proto.Field(
        proto.MESSAGE,
        number=3,
        message="AutomatedAgentReply",
    )
    message = proto.Field(
        proto.MESSAGE,
        number=5,
        message="Message",
    )
    human_agent_suggestion_results = proto.RepeatedField(
        proto.MESSAGE,
        number=6,
        message="SuggestionResult",
    )
    end_user_suggestion_results = proto.RepeatedField(
        proto.MESSAGE,
        number=7,
        message="SuggestionResult",
    )
    dtmf_parameters = proto.Field(
        proto.MESSAGE,
        number=9,
        message="DtmfParameters",
    )


class SuggestArticlesRequest(proto.Message):
    r"""The request message for
    [Participants.SuggestArticles][google.cloud.dialogflow.v2.Participants.SuggestArticles].

    Attributes:
        parent (str):
            Required. The name of the participant to fetch suggestion
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        latest_message (str):
            Optional. The name of the latest conversation message to
            compile suggestion for. If empty, it will be the latest
            message of the conversation.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Optional. Max number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestArticlesRequest.latest_message]
            to use as context when compiling the suggestion. By default
            20 and at most 50.
        assist_query_params (google.cloud.dialogflow_v2.types.AssistQueryParameters):
            Parameters for a human assist query.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_message = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size = proto.Field(
        proto.INT32,
        number=3,
    )
    assist_query_params = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AssistQueryParameters",
    )


class SuggestArticlesResponse(proto.Message):
    r"""The response message for
    [Participants.SuggestArticles][google.cloud.dialogflow.v2.Participants.SuggestArticles].

    Attributes:
        article_answers (Sequence[google.cloud.dialogflow_v2.types.ArticleAnswer]):
            Articles ordered by score in descending
            order.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestArticlesResponse.latest_message]
            to compile the suggestion. It may be smaller than the
            [SuggestArticlesRequest.context_size][google.cloud.dialogflow.v2.SuggestArticlesRequest.context_size]
            field in the request if there aren't that many messages in
            the conversation.
    """

    article_answers = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="ArticleAnswer",
    )
    latest_message = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size = proto.Field(
        proto.INT32,
        number=3,
    )


class SuggestFaqAnswersRequest(proto.Message):
    r"""The request message for
    [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2.Participants.SuggestFaqAnswers].

    Attributes:
        parent (str):
            Required. The name of the participant to fetch suggestion
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        latest_message (str):
            Optional. The name of the latest conversation message to
            compile suggestion for. If empty, it will be the latest
            message of the conversation.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Optional. Max number of messages prior to and including
            [latest_message] to use as context when compiling the
            suggestion. By default 20 and at most 50.
        assist_query_params (google.cloud.dialogflow_v2.types.AssistQueryParameters):
            Parameters for a human assist query.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    latest_message = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size = proto.Field(
        proto.INT32,
        number=3,
    )
    assist_query_params = proto.Field(
        proto.MESSAGE,
        number=4,
        message="AssistQueryParameters",
    )


class SuggestFaqAnswersResponse(proto.Message):
    r"""The request message for
    [Participants.SuggestFaqAnswers][google.cloud.dialogflow.v2.Participants.SuggestFaqAnswers].

    Attributes:
        faq_answers (Sequence[google.cloud.dialogflow_v2.types.FaqAnswer]):
            Answers extracted from FAQ documents.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestFaqAnswersResponse.latest_message]
            to compile the suggestion. It may be smaller than the
            [SuggestFaqAnswersRequest.context_size][google.cloud.dialogflow.v2.SuggestFaqAnswersRequest.context_size]
            field in the request if there aren't that many messages in
            the conversation.
    """

    faq_answers = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="FaqAnswer",
    )
    latest_message = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size = proto.Field(
        proto.INT32,
        number=3,
    )


class SuggestSmartRepliesRequest(proto.Message):
    r"""The request message for
    [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2.Participants.SuggestSmartReplies].

    Attributes:
        parent (str):
            Required. The name of the participant to fetch suggestion
            for. Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/participants/<Participant ID>``.
        current_text_input (google.cloud.dialogflow_v2.types.TextInput):
            The current natural language text segment to
            compile suggestion for. This provides a way for
            user to get follow up smart reply suggestion
            after a smart reply selection, without sending a
            text message.
        latest_message (str):
            The name of the latest conversation message to compile
            suggestion for. If empty, it will be the latest message of
            the conversation.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Max number of messages prior to and including
            [latest_message] to use as context when compiling the
            suggestion. By default 20 and at most 50.
    """

    parent = proto.Field(
        proto.STRING,
        number=1,
    )
    current_text_input = proto.Field(
        proto.MESSAGE,
        number=4,
        message=session.TextInput,
    )
    latest_message = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size = proto.Field(
        proto.INT32,
        number=3,
    )


class SuggestSmartRepliesResponse(proto.Message):
    r"""The response message for
    [Participants.SuggestSmartReplies][google.cloud.dialogflow.v2.Participants.SuggestSmartReplies].

    Attributes:
        smart_reply_answers (Sequence[google.cloud.dialogflow_v2.types.SmartReplyAnswer]):
            Output only. Multiple reply options provided
            by smart reply service. The order is based on
            the rank of the model prediction. The maximum
            number of the returned replies is set in
            SmartReplyConfig.
        latest_message (str):
            The name of the latest conversation message used to compile
            suggestion for.

            Format:
            ``projects/<Project ID>/locations/<Location ID>/conversations/<Conversation ID>/messages/<Message ID>``.
        context_size (int):
            Number of messages prior to and including
            [latest_message][google.cloud.dialogflow.v2.SuggestSmartRepliesResponse.latest_message]
            to compile the suggestion. It may be smaller than the
            [SuggestSmartRepliesRequest.context_size][google.cloud.dialogflow.v2.SuggestSmartRepliesRequest.context_size]
            field in the request if there aren't that many messages in
            the conversation.
    """

    smart_reply_answers = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="SmartReplyAnswer",
    )
    latest_message = proto.Field(
        proto.STRING,
        number=2,
    )
    context_size = proto.Field(
        proto.INT32,
        number=3,
    )


class OutputAudio(proto.Message):
    r"""Represents the natural language speech audio to be played to
    the end user.

    Attributes:
        config (google.cloud.dialogflow_v2.types.OutputAudioConfig):
            Instructs the speech synthesizer how to
            generate the speech audio.
        audio (bytes):
            The natural language speech audio.
    """

    config = proto.Field(
        proto.MESSAGE,
        number=1,
        message=audio_config.OutputAudioConfig,
    )
    audio = proto.Field(
        proto.BYTES,
        number=2,
    )


class AutomatedAgentReply(proto.Message):
    r"""Represents a response from an automated agent.

    Attributes:
        detect_intent_response (google.cloud.dialogflow_v2.types.DetectIntentResponse):
            Response of the Dialogflow
            [Sessions.DetectIntent][google.cloud.dialogflow.v2.Sessions.DetectIntent]
            call.
        automated_agent_reply_type (google.cloud.dialogflow_v2.types.AutomatedAgentReply.AutomatedAgentReplyType):
            AutomatedAgentReply type.
        allow_cancellation (bool):
            Indicates whether the partial automated agent
            reply is interruptible when a later reply
            message arrives. e.g. if the agent specified
            some music as partial response, it can be
            cancelled.
    """

    class AutomatedAgentReplyType(proto.Enum):
        r"""Represents different automated agent reply types."""
        AUTOMATED_AGENT_REPLY_TYPE_UNSPECIFIED = 0
        PARTIAL = 1
        FINAL = 2

    detect_intent_response = proto.Field(
        proto.MESSAGE,
        number=1,
        message=session.DetectIntentResponse,
    )
    automated_agent_reply_type = proto.Field(
        proto.ENUM,
        number=7,
        enum=AutomatedAgentReplyType,
    )
    allow_cancellation = proto.Field(
        proto.BOOL,
        number=8,
    )


class ArticleAnswer(proto.Message):
    r"""Represents article answer.

    Attributes:
        title (str):
            The article title.
        uri (str):
            The article URI.
        snippets (Sequence[str]):
            Article snippets.
        confidence (float):
            Article match confidence.
            The system's confidence score that this article
            is a good match for this conversation, as a
            value from 0.0 (completely uncertain) to 1.0
            (completely certain).
        metadata (Sequence[google.cloud.dialogflow_v2.types.ArticleAnswer.MetadataEntry]):
            A map that contains metadata about the answer
            and the document from which it originates.
        answer_record (str):
            The name of answer record, in the format of
            "projects/<Project ID>/locations/<Location
            ID>/answerRecords/<Answer Record ID>".
    """

    title = proto.Field(
        proto.STRING,
        number=1,
    )
    uri = proto.Field(
        proto.STRING,
        number=2,
    )
    snippets = proto.RepeatedField(
        proto.STRING,
        number=3,
    )
    confidence = proto.Field(
        proto.FLOAT,
        number=4,
    )
    metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    answer_record = proto.Field(
        proto.STRING,
        number=6,
    )


class FaqAnswer(proto.Message):
    r"""Represents answer from "frequently asked questions".

    Attributes:
        answer (str):
            The piece of text from the ``source`` knowledge base
            document.
        confidence (float):
            The system's confidence score that this
            Knowledge answer is a good match for this
            conversational query, range from 0.0 (completely
            uncertain) to 1.0 (completely certain).
        question (str):
            The corresponding FAQ question.
        source (str):
            Indicates which Knowledge Document this answer was extracted
            from. Format:
            ``projects/<Project ID>/locations/<Location ID>/agent/knowledgeBases/<Knowledge Base ID>/documents/<Document ID>``.
        metadata (Sequence[google.cloud.dialogflow_v2.types.FaqAnswer.MetadataEntry]):
            A map that contains metadata about the answer
            and the document from which it originates.
        answer_record (str):
            The name of answer record, in the format of
            "projects/<Project ID>/locations/<Location
            ID>/answerRecords/<Answer Record ID>".
    """

    answer = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence = proto.Field(
        proto.FLOAT,
        number=2,
    )
    question = proto.Field(
        proto.STRING,
        number=3,
    )
    source = proto.Field(
        proto.STRING,
        number=4,
    )
    metadata = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=5,
    )
    answer_record = proto.Field(
        proto.STRING,
        number=6,
    )


class SmartReplyAnswer(proto.Message):
    r"""Represents a smart reply answer.

    Attributes:
        reply (str):
            The content of the reply.
        confidence (float):
            Smart reply confidence.
            The system's confidence score that this reply is
            a good match for this conversation, as a value
            from 0.0 (completely uncertain) to 1.0
            (completely certain).
        answer_record (str):
            The name of answer record, in the format of
            "projects/<Project ID>/locations/<Location
            ID>/answerRecords/<Answer Record ID>".
    """

    reply = proto.Field(
        proto.STRING,
        number=1,
    )
    confidence = proto.Field(
        proto.FLOAT,
        number=2,
    )
    answer_record = proto.Field(
        proto.STRING,
        number=3,
    )


class SuggestionResult(proto.Message):
    r"""One response of different type of suggestion response which is used
    in the response of
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent]
    and
    [Participants.AnalyzeContent][google.cloud.dialogflow.v2.Participants.AnalyzeContent],
    as well as
    [HumanAgentAssistantEvent][google.cloud.dialogflow.v2.HumanAgentAssistantEvent].

    This message has `oneof`_ fields (mutually exclusive fields).
    For each oneof, at most one member field can be set at the same time.
    Setting any member of the oneof automatically clears all other
    members.

    .. _oneof: https://proto-plus-python.readthedocs.io/en/stable/fields.html#oneofs-mutually-exclusive-fields

    Attributes:
        error (google.rpc.status_pb2.Status):
            Error status if the request failed.

            This field is a member of `oneof`_ ``suggestion_response``.
        suggest_articles_response (google.cloud.dialogflow_v2.types.SuggestArticlesResponse):
            SuggestArticlesResponse if request is for
            ARTICLE_SUGGESTION.

            This field is a member of `oneof`_ ``suggestion_response``.
        suggest_faq_answers_response (google.cloud.dialogflow_v2.types.SuggestFaqAnswersResponse):
            SuggestFaqAnswersResponse if request is for FAQ_ANSWER.

            This field is a member of `oneof`_ ``suggestion_response``.
        suggest_smart_replies_response (google.cloud.dialogflow_v2.types.SuggestSmartRepliesResponse):
            SuggestSmartRepliesResponse if request is for SMART_REPLY.

            This field is a member of `oneof`_ ``suggestion_response``.
    """

    error = proto.Field(
        proto.MESSAGE,
        number=1,
        oneof="suggestion_response",
        message=status_pb2.Status,
    )
    suggest_articles_response = proto.Field(
        proto.MESSAGE,
        number=2,
        oneof="suggestion_response",
        message="SuggestArticlesResponse",
    )
    suggest_faq_answers_response = proto.Field(
        proto.MESSAGE,
        number=3,
        oneof="suggestion_response",
        message="SuggestFaqAnswersResponse",
    )
    suggest_smart_replies_response = proto.Field(
        proto.MESSAGE,
        number=4,
        oneof="suggestion_response",
        message="SuggestSmartRepliesResponse",
    )


class AnnotatedMessagePart(proto.Message):
    r"""Represents a part of a message possibly annotated with an
    entity. The part can be an entity or purely a part of the
    message between two entities or message start/end.

    Attributes:
        text (str):
            A part of a message possibly annotated with
            an entity.
        entity_type (str):
            The `Dialogflow system entity
            type <https://cloud.google.com/dialogflow/docs/reference/system-entities>`__
            of this message part. If this is empty, Dialogflow could not
            annotate the phrase part with a system entity.
        formatted_value (google.protobuf.struct_pb2.Value):
            The `Dialogflow system entity formatted
            value <https://cloud.google.com/dialogflow/docs/reference/system-entities>`__
            of this message part. For example for a system entity of
            type ``@sys.unit-currency``, this may contain:

            .. raw:: html

                <pre>
                {
                  "amount": 5,
                  "currency": "USD"
                }
                </pre>
    """

    text = proto.Field(
        proto.STRING,
        number=1,
    )
    entity_type = proto.Field(
        proto.STRING,
        number=2,
    )
    formatted_value = proto.Field(
        proto.MESSAGE,
        number=3,
        message=struct_pb2.Value,
    )


class MessageAnnotation(proto.Message):
    r"""Represents the result of annotation for the message.

    Attributes:
        parts (Sequence[google.cloud.dialogflow_v2.types.AnnotatedMessagePart]):
            The collection of annotated message parts ordered by their
            position in the message. You can recover the annotated
            message by concatenating [AnnotatedMessagePart.text].
        contain_entities (bool):
            Indicates whether the text message contains
            entities.
    """

    parts = proto.RepeatedField(
        proto.MESSAGE,
        number=1,
        message="AnnotatedMessagePart",
    )
    contain_entities = proto.Field(
        proto.BOOL,
        number=2,
    )


class AssistQueryParameters(proto.Message):
    r"""Represents the parameters of human assist query.

    Attributes:
        documents_metadata_filters (Sequence[google.cloud.dialogflow_v2.types.AssistQueryParameters.DocumentsMetadataFiltersEntry]):
            Key-value filters on the metadata of documents returned by
            article suggestion. If specified, article suggestion only
            returns suggested documents that match all filters in their
            [Document.metadata][google.cloud.dialogflow.v2.Document.metadata].
            Multiple values for a metadata key should be concatenated by
            comma. For example, filters to match all documents that have
            'US' or 'CA' in their market metadata values and 'agent' in
            their user metadata values will be

            ::

               documents_metadata_filters {
                 key: "market"
                 value: "US,CA"
               }
               documents_metadata_filters {
                 key: "user"
                 value: "agent"
               }
    """

    documents_metadata_filters = proto.MapField(
        proto.STRING,
        proto.STRING,
        number=1,
    )


__all__ = tuple(sorted(__protobuf__.manifest))
