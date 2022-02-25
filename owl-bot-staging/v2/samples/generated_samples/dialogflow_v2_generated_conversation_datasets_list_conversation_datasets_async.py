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
# Generated code. DO NOT EDIT!
#
# Snippet for ListConversationDatasets
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2_generated_ConversationDatasets_ListConversationDatasets_async]
from google.cloud import dialogflow_v2


async def sample_list_conversation_datasets():
    # Create a client
    client = dialogflow_v2.ConversationDatasetsAsyncClient()

    # Initialize request argument(s)
    request = dialogflow_v2.ListConversationDatasetsRequest(
        parent="parent_value",
    )

    # Make the request
    page_result = client.list_conversation_datasets(request=request)

    # Handle the response
    async for response in page_result:
        print(response)

# [END dialogflow_v2_generated_ConversationDatasets_ListConversationDatasets_async]
