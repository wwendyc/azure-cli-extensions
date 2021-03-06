# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
import warnings

from azure.core.exceptions import map_error
from azure.core.paging import ItemPaged
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse

from .. import models

T = TypeVar('T')
ClsType = Optional[Callable[[
    PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class DashboardOperations(object):
    """DashboardOperations operations.

    You should not instantiate directly this class, but create a Client instance that will create it for you and attach it as attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~portal.models
    :param client: Client for service requests.
    :param config: Configuration of service client.
    :param serializer: An object model serializer.
    :param deserializer: An object model deserializer.
    """

    models = models

    def __init__(self, client, config, serializer, deserializer):
        self._client = client
        self._serialize = serializer
        self._deserialize = deserializer
        self._config = config

    def create_or_update(
        self,
        resource_group_name,  # type: str
        dashboard_name,  # type: str
        location,  # type: str
        tags=None,  # type: Optional[Dict[str, str]]
        lenses=None,  # type: Optional[Dict[str, "DashboardLens"]]
        metadata=None,  # type: Optional[Dict[str, object]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Dashboard"
        """Creates or updates a Dashboard.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param dashboard_name: The name of the dashboard.
        :type dashboard_name: str
        :param location: Resource location.
        :type location: str
        :param tags: Resource tags.
        :type tags: dict[str, str]
        :param lenses: The dashboard lenses.
        :type lenses: dict[str, ~portal.models.DashboardLens]
        :param metadata: The dashboard metadata.
        :type metadata: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dashboard or Dashboard or the result of cls(response)
        :rtype: ~portal.models.Dashboard or ~portal.models.Dashboard
        :raises: ~portal.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Dashboard"]
        error_map = kwargs.pop('error_map', {})

        dashboard = models.Dashboard(
            location=location, tags=tags, lenses=lenses, metadata=metadata)
        api_version = "2019-01-01-preview"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dashboardName': self._serialize.url("dashboard_name", dashboard_name, 'str', max_length=64, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query(
            "api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(dashboard, 'Dashboard')

        # Construct and send request
        request = self._client.put(
            url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(
            request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code,
                      response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(
                response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Dashboard', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Dashboard', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {
        'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}'}

    def delete(
        self,
        resource_group_name,  # type: str
        dashboard_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes the Dashboard.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param dashboard_name: The name of the dashboard.
        :type dashboard_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None or the result of cls(response)
        :rtype: None
        :raises: ~portal.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-01-01-preview"

        # Construct URL
        url = self.delete.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dashboardName': self._serialize.url("dashboard_name", dashboard_name, 'str', max_length=64, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query(
            "api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}

        # Construct and send request
        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(
            request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code,
                      response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(
                response, self._deserialize)

        if cls:
            return cls(pipeline_response, None, {})

    delete.metadata = {
        'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}'}

    def get(
        self,
        resource_group_name,  # type: str
        dashboard_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Dashboard"
        """Gets the Dashboard.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param dashboard_name: The name of the dashboard.
        :type dashboard_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dashboard or the result of cls(response)
        :rtype: ~portal.models.Dashboard
        :raises: ~portal.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Dashboard"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-01-01-preview"

        # Construct URL
        url = self.get.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dashboardName': self._serialize.url("dashboard_name", dashboard_name, 'str', max_length=64, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query(
            "api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'

        # Construct and send request
        request = self._client.get(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(
            request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code,
                      response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(
                response, self._deserialize)

        deserialized = self._deserialize('Dashboard', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    get.metadata = {
        'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}'}

    def update(
        self,
        resource_group_name,  # type: str
        dashboard_name,  # type: str
        lenses=None,  # type: Optional[Dict[str, "DashboardLens"]]
        metadata=None,  # type: Optional[Dict[str, object]]
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Dashboard"
        """Updates an existing Dashboard.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param dashboard_name: The name of the dashboard.
        :type dashboard_name: str
        :param lenses: The dashboard lenses.
        :type lenses: dict[str, ~portal.models.DashboardLens]
        :param metadata: The dashboard metadata.
        :type metadata: dict[str, object]
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dashboard or the result of cls(response)
        :rtype: ~portal.models.Dashboard
        :raises: ~portal.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Dashboard"]
        error_map = kwargs.pop('error_map', {})

        dashboard = models.PatchableDashboard(lenses=lenses, metadata=metadata)
        api_version = "2019-01-01-preview"

        # Construct URL
        url = self.update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dashboardName': self._serialize.url("dashboard_name", dashboard_name, 'str', max_length=64, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query(
            "api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(dashboard, 'PatchableDashboard')

        # Construct and send request
        request = self._client.patch(
            url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(
            request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200]:
            map_error(status_code=response.status_code,
                      response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(
                response, self._deserialize)

        deserialized = self._deserialize('Dashboard', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    update.metadata = {
        'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}'}

    def list_by_resource_group(
        self,
        resource_group_name,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DashboardListResult"
        """Gets all the Dashboards within a resource group.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DashboardListResult or the result of cls(response)
        :rtype: ~portal.models.DashboardListResult
        :raises: ~portal.models.ErrorResponseException:
        """
        cls = kwargs.pop(
            'cls', None)  # type: ClsType["models.DashboardListResult"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-01-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_resource_group.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                    'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}
            query_parameters['api-version'] = self._serialize.query(
                "api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(
                url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize(
                'DashboardListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(
                request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code,
                          response=response, error_map=error_map)
                raise models.ErrorResponseException.from_response(
                    response, self._deserialize)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_resource_group.metadata = {
        'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards'}

    def list_by_subscription(
        self,
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.DashboardListResult"
        """Gets all the dashboards within a subscription.

        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DashboardListResult or the result of cls(response)
        :rtype: ~portal.models.DashboardListResult
        :raises: ~portal.models.ErrorResponseException:
        """
        cls = kwargs.pop(
            'cls', None)  # type: ClsType["models.DashboardListResult"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-01-01-preview"

        def prepare_request(next_link=None):
            if not next_link:
                # Construct URL
                url = self.list_by_subscription.metadata['url']
                path_format_arguments = {
                    'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
                }
                url = self._client.format_url(url, **path_format_arguments)
            else:
                url = next_link

            # Construct parameters
            query_parameters = {}
            query_parameters['api-version'] = self._serialize.query(
                "api_version", api_version, 'str')

            # Construct headers
            header_parameters = {}
            header_parameters['Accept'] = 'application/json'

            # Construct and send request
            request = self._client.get(
                url, query_parameters, header_parameters)
            return request

        def extract_data(pipeline_response):
            deserialized = self._deserialize(
                'DashboardListResult', pipeline_response)
            list_of_elem = deserialized.value
            if cls:
                list_of_elem = cls(list_of_elem)
            return deserialized.next_link, iter(list_of_elem)

        def get_next(next_link=None):
            request = prepare_request(next_link)

            pipeline_response = self._client._pipeline.run(
                request, stream=False, **kwargs)
            response = pipeline_response.http_response

            if response.status_code not in [200]:
                map_error(status_code=response.status_code,
                          response=response, error_map=error_map)
                raise models.ErrorResponseException.from_response(
                    response, self._deserialize)

            return pipeline_response

        return ItemPaged(
            get_next, extract_data
        )
    list_by_subscription.metadata = {
        'url': '/subscriptions/{subscriptionId}/providers/Microsoft.Portal/dashboards'}

    def dashboard_import(
        self,
        resource_group_name,  # type: str
        dashboard_name,  # type: str
        dashboard,  # type: "models.Dashboard"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.Dashboard"
        """Creates or updates a Dashboard.

        :param resource_group_name: The name of the resource group.
        :type resource_group_name: str
        :param dashboard_name: The name of the dashboard.
        :type dashboard_name: str
        :param dashboard: The parameters required to create or update a dashboard.
        :type dashboard: ~portal.models.Dashboard
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: Dashboard or Dashboard or the result of cls(response)
        :rtype: ~portal.models.Dashboard or ~portal.models.Dashboard
        :raises: ~portal.models.ErrorResponseException:
        """
        cls = kwargs.pop('cls', None)  # type: ClsType["models.Dashboard"]
        error_map = kwargs.pop('error_map', {})
        api_version = "2019-01-01-preview"

        # Construct URL
        url = self.create_or_update.metadata['url']
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("resource_group_name", resource_group_name, 'str'),
            'dashboardName': self._serialize.url("dashboard_name", dashboard_name, 'str', max_length=64, min_length=3),
        }
        url = self._client.format_url(url, **path_format_arguments)

        # Construct parameters
        query_parameters = {}
        query_parameters['api-version'] = self._serialize.query(
            "api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Accept'] = 'application/json'
        header_parameters['Content-Type'] = 'application/json'

        # Construct body
        body_content = self._serialize.body(dashboard, 'Dashboard')

        # Construct and send request
        request = self._client.put(
            url, query_parameters, header_parameters, body_content)
        pipeline_response = self._client._pipeline.run(
            request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code,
                      response=response, error_map=error_map)
            raise models.ErrorResponseException.from_response(
                response, self._deserialize)

        deserialized = None
        if response.status_code == 200:
            deserialized = self._deserialize('Dashboard', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize('Dashboard', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    create_or_update.metadata = {
        'url': '/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.Portal/dashboards/{dashboardName}'}
