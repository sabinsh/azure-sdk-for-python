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


class CdnEndpoint(Model):
    """Defines the ARM Resource ID for the linked endpoints.

    :param id: ARM Resource ID string.
    :type id: str
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'str'},
    }

    def __init__(self, *, id: str=None, **kwargs) -> None:
        super(CdnEndpoint, self).__init__(**kwargs)
        self.id = id
