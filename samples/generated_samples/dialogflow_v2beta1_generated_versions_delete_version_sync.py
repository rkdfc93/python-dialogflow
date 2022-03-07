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
# Generated code. DO NOT EDIT!
#
# Snippet for DeleteVersion
# NOTE: This snippet has been automatically generated for illustrative purposes only.
# It may require modifications to work in your environment.

# To install the latest published package dependency, execute the following:
#   python3 -m pip install google-cloud-dialogflow


# [START dialogflow_v2beta1_generated_Versions_DeleteVersion_sync]
from google.cloud import dialogflow_v2beta1


def sample_delete_version():
    # Create a client
    client = dialogflow_v2beta1.VersionsClient()

    # Initialize request argument(s)
    request = dialogflow_v2beta1.DeleteVersionRequest(
        name="name_value",
    )

    # Make the request
    client.delete_version(request=request)


# [END dialogflow_v2beta1_generated_Versions_DeleteVersion_sync]