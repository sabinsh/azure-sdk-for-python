# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ActionType(Model):
    """Defines the action to take on rule match.

    All required parameters must be populated in order to send to Azure.

    :param action_type: Required. Describes type of action. Possible values
     include: 'Allow', 'Block', 'Log', 'Redirect'
    :type action_type: str or ~azure.mgmt.cdn.models.Action
    :param redirect_url: If action type is redirect, this field represents URL
     to be re-directed.
    :type redirect_url: str
    :param custom_block_response_status_code: If the action type is block,
     customer can override the response status code.
    :type custom_block_response_status_code: int
    :param custom_block_response_body: If the action type is block, customer
     can override the response body. The body must be specified in base64
     encoding.
    :type custom_block_response_body: str
    """

    _validation = {
        'action_type': {'required': True},
        'custom_block_response_status_code': {'maximum': 599, 'minimum': 200},
        'custom_block_response_body': {'pattern': r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$'},
    }

    _attribute_map = {
        'action_type': {'key': 'actionType', 'type': 'str'},
        'redirect_url': {'key': 'redirectUrl', 'type': 'str'},
        'custom_block_response_status_code': {'key': 'customBlockResponseStatusCode', 'type': 'int'},
        'custom_block_response_body': {'key': 'customBlockResponseBody', 'type': 'str'},
    }

    def __init__(self, *, action_type, redirect_url: str=None, custom_block_response_status_code: int=None, custom_block_response_body: str=None, **kwargs) -> None:
        super(ActionType, self).__init__(**kwargs)
        self.action_type = action_type
        self.redirect_url = redirect_url
        self.custom_block_response_status_code = custom_block_response_status_code
        self.custom_block_response_body = custom_block_response_body
