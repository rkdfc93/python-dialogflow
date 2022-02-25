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
# Snippet for UpdateConversationProfile
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2_generated_ConversationProfiles_UpdateConversationProfile_async]
from google.cloud import dialogflow_v2


async def sample_update_conversation_profile():
    # Create a client
    client = dialogflow_v2.ConversationProfilesAsyncClient()

    # Initialize request argument(s)
    conversation_profile = dialogflow_v2.ConversationProfile()
    conversation_profile.display_name = "display_name_value"

    request = dialogflow_v2.UpdateConversationProfileRequest(
        conversation_profile=conversation_profile,
    )

    # Make the request
    response = await client.update_conversation_profile(request=request)

    # Handle the response
    print(response)

# [END dialogflow_v2_generated_ConversationProfiles_UpdateConversationProfile_async]
