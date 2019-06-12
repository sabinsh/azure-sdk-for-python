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


class PolicySettings(Model):
    """Defines contents of a web application firewall global configuration.

    :param enabled_state: describes if the policy is in enabled state or
     disabled state. Possible values include: 'Disabled', 'Enabled'
    :type enabled_state: str or ~azure.mgmt.cdn.models.PolicyEnabledState
    :param mode: Describes if it is in detection mode or prevention mode at
     policy level. Possible values include: 'Prevention', 'Detection'
    :type mode: str or ~azure.mgmt.cdn.models.PolicyMode
    :param default_redirect_url: If action type is redirect, this field
     represents the default redirect URL for the client.
    :type default_redirect_url: str
    :param default_custom_block_response_status_code: If the action type is
     block, this field defines the default customer overridable http response
     status code.
    :type default_custom_block_response_status_code: int
    :param default_custom_block_response_body: If the action type is block,
     customer can override the response body. The body must be specified in
     base64 encoding.
    :type default_custom_block_response_body: str
    """

    _validation = {
        'default_custom_block_response_status_code': {'maximum': 599, 'minimum': 200},
        'default_custom_block_response_body': {'pattern': r'^(?:[A-Za-z0-9+/]{4})*(?:[A-Za-z0-9+/]{2}==|[A-Za-z0-9+/]{3}=|[A-Za-z0-9+/]{4})$'},
    }

    _attribute_map = {
        'enabled_state': {'key': 'enabledState', 'type': 'str'},
        'mode': {'key': 'mode', 'type': 'str'},
        'default_redirect_url': {'key': 'defaultRedirectUrl', 'type': 'str'},
        'default_custom_block_response_status_code': {'key': 'defaultCustomBlockResponseStatusCode', 'type': 'int'},
        'default_custom_block_response_body': {'key': 'defaultCustomBlockResponseBody', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(PolicySettings, self).__init__(**kwargs)
        self.enabled_state = kwargs.get('enabled_state', None)
        self.mode = kwargs.get('mode', None)
        self.default_redirect_url = kwargs.get('default_redirect_url', None)
        self.default_custom_block_response_status_code = kwargs.get('default_custom_block_response_status_code', None)
        self.default_custom_block_response_body = kwargs.get('default_custom_block_response_body', None)
