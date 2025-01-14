# coding=utf-8
# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from knack.help_files import helps
# pylint: disable=line-too-long, too-many-lines

helps['iotcentral'] = """
type: group
short-summary: Manage IoT Central assets.
"""

helps['iotcentral app'] = """
type: group
short-summary: Manage IoT Central applications.
"""

helps['iotcentral app create'] = """
type: command
short-summary: Create an IoT Central application.
long-summary: |
    For an introduction to IoT Central, see https://docs.microsoft.com/azure/iot-central/.
    The F1 Sku is no longer supported. Please use the S1 Sku (default) for app creation.
    For more pricing information, please visit https://azure.microsoft.com/pricing/details/iot-central/.
examples:
  - name: Create an IoT Central application in the standard pricing tier S1, in the region of the resource group.
    text: >
        az iotcentral app create --resource-group MyResourceGroup --name my-app-resource --subdomain my-app-subdomain
  - name: Create an IoT Central application with the standard pricing tier S1 in the 'westus' region, with a custom display name, based on the iotc-default template.
    text: >
        az iotcentral app create --resource-group MyResourceGroup --name my-app-resource-name --sku S1 --location westus --subdomain my-app-subdomain --template iotc-default@1.0.0 --display-name 'My Custom Display Name'
"""

helps['iotcentral app delete'] = """
type: command
short-summary: Delete an IoT Central application.
examples:
  - name: Delete an IoT Central application. (autogenerated)
    text: az iotcentral app delete --name MyIoTCentralApplication --resource-group MyResourceGroup
    crafted: true
"""

helps['iotcentral app list'] = """
type: command
short-summary: List IoT Central applications.
examples:
  - name: List all IoT Central applications in a subscription.
    text: >
        az iotcentral app list
  - name: List all IoT Central applications in the resource group 'MyGroup'
    text: >
        az iotcentral app list --resource-group MyGroup
"""

helps['iotcentral app show'] = """
type: command
short-summary: Get the details of an IoT Central application.
examples:
  - name: Show an IoT Central application.
    text: >
        az iotcentral app show --name MyApp
"""

helps['iotcentral app update'] = """
type: command
short-summary: Update metadata for an IoT Central application.
"""
