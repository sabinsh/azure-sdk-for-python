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


class EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink(Model):
    """Defines the Web Application Firewall policy for the endpoint (if
    applicable).

    :param id: Resource ID.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, **kwargs):
        super(EndpointPropertiesUpdateParametersWebApplicationFirewallPolicyLink, self).__init__(**kwargs)
        self.id = kwargs.get('id', None)
