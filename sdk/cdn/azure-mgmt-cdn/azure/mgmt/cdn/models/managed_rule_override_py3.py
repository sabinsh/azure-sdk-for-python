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


class ManagedRuleOverride(Model):
    """Defines a managed rule group override setting.

    All required parameters must be populated in order to send to Azure.

    :param rule_id: Required. Identifier for the managed rule.
    :type rule_id: str
    :param enabled_state: Describes if the managed rule is in enabled or
     disabled state. Defaults to Disabled if not specified. Possible values
     include: 'Disabled', 'Enabled'
    :type enabled_state: str or ~azure.mgmt.cdn.models.ManagedRuleEnabledState
    :param action: Describes the override action to be applied when rule
     matches.
    :type action: ~azure.mgmt.cdn.models.ActionType
    """

    _validation = {
        'rule_id': {'required': True},
    }

    _attribute_map = {
        'rule_id': {'key': 'ruleId', 'type': 'str'},
        'enabled_state': {'key': 'enabledState', 'type': 'str'},
        'action': {'key': 'action', 'type': 'ActionType'},
    }

    def __init__(self, *, rule_id: str, enabled_state=None, action=None, **kwargs) -> None:
        super(ManagedRuleOverride, self).__init__(**kwargs)
        self.rule_id = rule_id
        self.enabled_state = enabled_state
        self.action = action
