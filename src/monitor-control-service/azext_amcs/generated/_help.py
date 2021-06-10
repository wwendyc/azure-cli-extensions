# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------
# pylint: disable=too-many-lines

from knack.help_files import helps


helps['monitor data-collection'] = '''
    type: group
    short-summary: Manage Monitor
'''

helps['monitor data-collection endpoint'] = """
    type: group
    short-summary: Manage data collection endpoint with monitor control service
"""

helps['monitor data-collection endpoint list'] = """
    type: command
    short-summary: "Lists all data collection endpoints in the specified resource group. And Lists all data collection \
endpoints in the specified subscription."
    examples:
      - name: List data collection endpoints by resource group
        text: |-
               az monitor data-collection endpoint list --resource-group "myResourceGroup"
      - name: List data collection endpoints by subscription
        text: |-
               az monitor data-collection endpoint list
"""

helps['monitor data-collection endpoint show'] = """
    type: command
    short-summary: "Returns the specified data collection endpoint."
    examples:
      - name: Get data collection endpoint
        text: |-
               az monitor data-collection endpoint show --name "myCollectionEndpoint" --resource-group \
"myResourceGroup"
"""

helps['monitor data-collection endpoint delete'] = """
    type: command
    short-summary: "Deletes a data collection endpoint."
    examples:
      - name: Delete data collection endpoint
        text: |-
               az monitor data-collection endpoint delete --name "myCollectionEndpoint" --resource-group \
"myResourceGroup"
"""

helps['monitor data-collection rule association'] = """
    type: group
    short-summary: Manage data collection rule association with monitor control service
"""

helps['monitor data-collection rule association list'] = """
    type: command
    short-summary: "Lists associations for the specified data collection rule. And Lists associations for the \
specified resource."
    examples:
      - name: List associations for specified data collection rule
        text: |-
               az monitor data-collection rule association list --rule-name "myCollectionRule" --resource-group \
"myResourceGroup"
      - name: List associations for specified resource
        text: |-
               az monitor data-collection rule association list --resource "subscriptions/703362b3-f278-4e4b-9179-c76ea\
f41ffc2/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualMachines/myVm"
"""

helps['monitor data-collection rule association show'] = """
    type: command
    short-summary: "Returns the specified association."
    examples:
      - name: Get association
        text: |-
               az monitor data-collection rule association show --name "myAssociation" --resource \
"subscriptions/703362b3-f278-4e4b-9179-c76eaf41ffc2/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualM\
achines/myVm"
"""

helps['monitor data-collection rule association delete'] = """
    type: command
    short-summary: "Deletes an association."
    examples:
      - name: Delete association
        text: |-
               az monitor data-collection rule association delete --name "myAssociation" --resource \
"subscriptions/703362b3-f278-4e4b-9179-c76eaf41ffc2/resourceGroups/myResourceGroup/providers/Microsoft.Compute/virtualM\
achines/myVm"
"""

helps['monitor data-collection rule'] = """
    type: group
    short-summary: Manage data collection rule with monitor control service
"""

helps['monitor data-collection rule list'] = """
    type: command
    short-summary: "Lists all data collection rules in the specified resource group. And Lists all data collection \
rules in the specified subscription."
    examples:
      - name: List data collection rules by resource group
        text: |-
               az monitor data-collection rule list --resource-group "myResourceGroup"
      - name: List data collection rules by subscription
        text: |-
               az monitor data-collection rule list
"""

helps['monitor data-collection rule show'] = """
    type: command
    short-summary: "Returns the specified data collection rule."
    examples:
      - name: Get data collection rule
        text: |-
               az monitor data-collection rule show --name "myCollectionRule" --resource-group "myResourceGroup"
"""

helps['monitor data-collection rule delete'] = """
    type: command
    short-summary: "Deletes a data collection rule."
    examples:
      - name: Delete data collection rule
        text: |-
               az monitor data-collection rule delete --name "myCollectionRule" --resource-group "myResourceGroup"
"""
