# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------
from typing import TYPE_CHECKING
import datetime
import warnings

from azure.core.exceptions import ClientAuthenticationError, HttpResponseError, ResourceExistsError, ResourceNotFoundError, map_error
from azure.core.pipeline import PipelineResponse
from azure.core.pipeline.transport import HttpRequest, HttpResponse
from azure.core.polling import LROPoller, NoPolling, PollingMethod
from azure.mgmt.core.exceptions import ARMErrorFormat
from azure.mgmt.core.polling.arm_polling import ARMPolling
from typing import Any, Callable, Dict, Generic, Optional, TypeVar, Union
from .. import models


if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports

    T = TypeVar('T')
    ClsType = Optional[Callable[[
        PipelineResponse[HttpRequest, HttpResponse], T, Dict[str, Any]], Any]]


class ResourceTypeRegistrationOperations(object):
    """ResourceTypeRegistrationOperations operations.

    You should not instantiate this class directly. Instead, you should create a Client instance that
    instantiates it for you and attaches it as an attribute.

    :ivar models: Alias to model classes used in this operation group.
    :type models: ~providerhub.models
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

    def _create_or_update_initial(
        self,
        provider_namespace,  # type: str
        resource_type,  # type: str
        nested_resource_type,  # type: str
        routing_type,  # type: str or "models.RoutingType"
        regionality,  # type: "models.Regionality"
        endpoints,  # type: list["models.ResourceTypeEndpoint"]
        resource_creation_begin,  # type: "models.ExtensionOptions"
        resource_patch_begin,  # type: "models.ExtensionOptions"
        marketplace_type,  # type: "models.ResourceTypeRegistrationPropertiesMarketplaceType"
        swagger_specifications,  # type: list["models.SwaggerSpecification"]
        allowed_unauthorized_actions,  # type: list[str]
        # type: list["models.AuthorizationActionMapping"]
        authorization_action_mappings,
        linked_access_checks,  # type: list["models.LinkedAccessCheck"]
        default_api_version,  # type: str
        logging_rules,  # type: list["models.LoggingRule"]
        throttling_rules,  # type: list["models.ThrottlingRule"]
        required_features,  # type: list[str]
        enable_async_operation,  # type: bool
        enable_third_party_s2s,  # type: bool
        is_pure_proxy,  # type: bool
        identity_management,  # type: "models.IdentityManagementProperties"
        # type: "models.CheckNameAvailabilitySpecifications"
        check_name_availability_specifications,
        disallowed_action_verbs,  # type: list[str]
        service_tree_infos,  # type: list["models.ServiceTreeInfo"]
        subscription_state_rules,  # type: list["models.SubscriptionStateRule"]
        template_deployment_options,  # type: "models.TemplateDeploymentOptions"
        extended_locations,  # type: list["models.ExtendedLocationOptions"]
        resource_move_policy,  # type: "models.ResourceMovePolicy"
        resource_deletion_policy,  # type: "models.ResourceDeletionPolicy"
        opt_in_headers,  # type: "models.OptInHeaderType"
        required_features_policy,  # type: "models.FeaturesPolicy"
        extensions, # type: "models.ResourceTypeExtension"
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.ResourceTypeRegistration"
        # type: ClsType["models.ResourceTypeRegistration"]
        cls = kwargs.pop('cls', None)
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-20"
        content_type = kwargs.pop("content_type", "application/json")
        accept = "application/json"

        # Construct URL
        url = self._create_or_update_initial.metadata['url']  # type: ignore
        resourceTypes = resource_type.split("/")
        resourceTypeUrlSuffix = "/resourcetypeRegistrations/".join(resourceTypes)
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'providerNamespace': self._serialize.url("provider_namespace", provider_namespace, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)
        url = url + resourceTypeUrlSuffix

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query(
            "api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Content-Type'] = self._serialize.header(
            "content_type", content_type, 'str')
        header_parameters['Accept'] = self._serialize.header(
            "accept", accept, 'str')

        request_header_options = models.RequestHeaderOptions(
            opt_in_headers=opt_in_headers) if opt_in_headers else None
        features_rule = models.FeaturesRule(
            required_features_policy=required_features_policy) if required_features_policy else None
        extensions = models.ResourceTypeExtension(
            extensions=extensions) if extensions else None
        extension_options = models.ResourceTypeExtensionOptions(resource_creation_begin=resource_creation_begin,
                                                                resource_patch_begin=resource_patch_begin) if resource_creation_begin or resource_patch_begin else None

        properties = models.ResourceTypeRegistration(routing_type=routing_type, regionality=regionality, endpoints=endpoints, extension_options=extension_options, marketplace_type=marketplace_type, swagger_specifications=swagger_specifications, allowed_unauthorized_actions=allowed_unauthorized_actions, authorization_action_mappings=authorization_action_mappings, linked_access_checks=linked_access_checks, default_api_version=default_api_version, logging_rules=logging_rules, throttling_rules=throttling_rules, required_features=required_features, features_rule=features_rule, enable_async_operation=enable_async_operation,
                                                 enable_third_party_s2s=enable_third_party_s2s, is_pure_proxy=is_pure_proxy, identity_management=identity_management, check_name_availability_specifications=check_name_availability_specifications, disallowed_action_verbs=disallowed_action_verbs, service_tree_infos=service_tree_infos, request_header_options=request_header_options, subscription_state_rules=subscription_state_rules, template_deployment_options=template_deployment_options, extended_locations=extended_locations, resource_move_policy=resource_move_policy, resource_deletion_policy=resource_deletion_policy)

        body_content_kwargs = {}  # type: Dict[str, Any]
        body_content = self._serialize.body(properties, 'ResourceTypeRegistration')
        body_content_kwargs['content'] = body_content
        request = self._client.put(
            url, query_parameters, header_parameters, **body_content_kwargs)
        pipeline_response = self._client._pipeline.run(
            request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 201]:
            map_error(status_code=response.status_code,
                      response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(
                response=response, model=error, error_format=ARMErrorFormat)

        if response.status_code == 200:
            deserialized = self._deserialize(
                'ResourceTypeRegistration', pipeline_response)

        if response.status_code == 201:
            deserialized = self._deserialize(
                'ResourceTypeRegistration', pipeline_response)

        if cls:
            return cls(pipeline_response, deserialized, {})

        return deserialized
    _create_or_update_initial.metadata = {
        'url': '/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/resourcetypeRegistrations/'}  # type: ignore

    def begin_create_or_update(
        self,
        provider_namespace,  # type: str
        resource_type,  # type: str
        nested_resource_type,  # type: str
        routing_type,  # type: str or "models.RoutingType"
        regionality,  # type: "models.Regionality"
        endpoints,  # type: list["models.ResourceTypeEndpoint"]
        resource_creation_begin,  # type: "models.ExtensionOptions"
        resource_patch_begin,  # type: "models.ExtensionOptions"
        marketplace_type,  # type: "models.ResourceTypeRegistrationPropertiesMarketplaceType"
        swagger_specifications,  # type: list["models.SwaggerSpecification"]
        allowed_unauthorized_actions,  # type: list[str]
        # type: list["models.AuthorizationActionMapping"]
        authorization_action_mappings,
        linked_access_checks,  # type: list["models.LinkedAccessCheck"]
        default_api_version,  # type: str
        logging_rules,  # type: list["models.LoggingRule"]
        throttling_rules,  # type: list["models.ThrottlingRule"]
        required_features,  # type: list[str]
        enable_async_operation,  # type: bool
        enable_third_party_s2s,  # type: bool
        is_pure_proxy,  # type: bool
        identity_management,  # type: "models.IdentityManagementProperties"
        # type: "models.CheckNameAvailabilitySpecifications"
        check_name_availability_specifications,
        disallowed_action_verbs,  # type: list[str]
        service_tree_infos,  # type: list["models.ServiceTreeInfo"]
        subscription_state_rules,  # type: list["models.SubscriptionStateRule"]
        template_deployment_options,  # type: "models.TemplateDeploymentOptions"
        extended_locations,  # type: list["models.ExtendedLocationOptions"]
        resource_move_policy,  # type: "models.ResourceMovePolicy"
        resource_deletion_policy,  # type: "models.ResourceDeletionPolicy"
        opt_in_headers,  # type: "models.OptInHeaderType"
        required_features_policy,  # type: "models.FeaturesPolicy"
        extensions, # type: "models.ResourceTypeExtension",
        **kwargs  # type: Any
    ):
        # type: (...) -> LROPoller["models.ResourceTypeRegistration"]
        """Creates or updates a resource type.

        :param provider_namespace: The name of the resource provider hosted within ProviderHub.
        :type provider_namespace: str
        :param resource_type: The resource type.
        :type resource_type: str
        :param properties: The resource type registration parameters supplied to the CreateOrUpdate operation.
        :type properties: ~providerhub.models.ResourceTypeRegistration
        :keyword callable cls: A custom type or function that will be passed the direct response
        :keyword str continuation_token: A continuation token to restart a poller from a saved state.
        :keyword polling: True for ARMPolling, False for no polling, or a
         polling object for personal polling strategy
        :paramtype polling: bool or ~azure.core.polling.PollingMethod
        :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
        :return: An instance of LROPoller that returns either ResourceTypeRegistration or the result of cls(response)
        :rtype: ~azure.core.polling.LROPoller[~providerhub.models.ResourceTypeRegistration]
        :raises ~azure.core.exceptions.HttpResponseError:
        """
        polling = kwargs.pop(
            'polling', True)  # type: Union[bool, PollingMethod]
        # type: ClsType["models.ResourceTypeRegistration"]
        cls = kwargs.pop('cls', None)
        lro_delay = kwargs.pop(
            'polling_interval',
            self._config.polling_interval
        )
        cont_token = kwargs.pop('continuation_token',
                                None)  # type: Optional[str]
        if cont_token is None:
            raw_result = self._create_or_update_initial(
                provider_namespace=provider_namespace,
                resource_type=resource_type,
                nested_resource_type=nested_resource_type,
                routing_type=routing_type,
                regionality=regionality,
                endpoints=endpoints,
                resource_creation_begin=resource_creation_begin,
                resource_patch_begin=resource_patch_begin,
                marketplace_type=marketplace_type,
                swagger_specifications=swagger_specifications,
                allowed_unauthorized_actions=allowed_unauthorized_actions,
                authorization_action_mappings=authorization_action_mappings,
                linked_access_checks=linked_access_checks,
                default_api_version=default_api_version,
                logging_rules=logging_rules,
                throttling_rules=throttling_rules,
                required_features=required_features,
                enable_async_operation=enable_async_operation,
                enable_third_party_s2s=enable_third_party_s2s,
                is_pure_proxy=is_pure_proxy,
                identity_management=identity_management,
                check_name_availability_specifications=check_name_availability_specifications,
                disallowed_action_verbs=disallowed_action_verbs,
                service_tree_infos=service_tree_infos,
                subscription_state_rules=subscription_state_rules,
                template_deployment_options=template_deployment_options,
                extended_locations=extended_locations,
                resource_move_policy=resource_move_policy,
                resource_deletion_policy=resource_deletion_policy,
                opt_in_headers=opt_in_headers,
                required_features_policy=required_features_policy,
                extensions=extensions,
                cls=lambda x, y, z: x,
                **kwargs
            )

        kwargs.pop('error_map', None)
        kwargs.pop('content_type', None)

        def get_long_running_output(pipeline_response):
            deserialized = self._deserialize(
                'ResourceTypeRegistration', pipeline_response)

            if cls:
                return cls(pipeline_response, deserialized, {})
            return deserialized

        nestedResourceTypeSuffix = f'/resourcetypeRegistrations/{nested_resource_type}' if nested_resource_type else ''
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'providerNamespace': self._serialize.url("provider_namespace", provider_namespace, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
        }

        if polling is True:
            polling_method = ARMPolling(lro_delay, lro_options={
                                        'final-state-via': 'azure-async-operation'}, path_format_arguments=path_format_arguments, **kwargs)
        elif polling is False:
            polling_method = NoPolling()
        else:
            polling_method = polling
        if cont_token:
            return LROPoller.from_continuation_token(
                polling_method=polling_method,
                continuation_token=cont_token,
                client=self._client,
                deserialization_callback=get_long_running_output
            )
        else:
            return LROPoller(self._client, raw_result, get_long_running_output, polling_method)
    begin_create_or_update.metadata = {
        'url': '/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/resourcetypeRegistrations/'}  # type: ignore

    def delete(
        self,
        provider_namespace,  # type: str
        resource_type,  # type: str
        nested_resource_type,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        """Deletes a resource type.

        :param provider_namespace: The name of the resource provider hosted within ProviderHub.
        :type provider_namespace: str
        :param resource_type: The resource type.
        :type resource_type: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: None, or the result of cls(response)
        :rtype: None
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        cls = kwargs.pop('cls', None)  # type: ClsType[None]
        error_map = {
            401: ClientAuthenticationError, 404: ResourceNotFoundError, 409: ResourceExistsError
        }
        error_map.update(kwargs.pop('error_map', {}))
        api_version = "2020-11-20"
        accept = "application/json"


        # Construct URL
        url = self.delete.metadata['url']  # type: ignore
        resourceTypes = resource_type.split("/")
        resourceTypeUrlSuffix = "/resourcetypeRegistrations/".join(resourceTypes)
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str', min_length=1),
            'providerNamespace': self._serialize.url("provider_namespace", provider_namespace, 'str'),
            'resourceType': self._serialize.url("resource_type", resource_type, 'str'),
        }
        url = self._client.format_url(url, **path_format_arguments)
        url = url + resourceTypeUrlSuffix

        # Construct parameters
        query_parameters = {}  # type: Dict[str, Any]
        query_parameters['api-version'] = self._serialize.query(
            "api_version", api_version, 'str')

        # Construct headers
        header_parameters = {}  # type: Dict[str, Any]
        header_parameters['Accept'] = self._serialize.header(
            "accept", accept, 'str')

        request = self._client.delete(url, query_parameters, header_parameters)
        pipeline_response = self._client._pipeline.run(
            request, stream=False, **kwargs)
        response = pipeline_response.http_response

        if response.status_code not in [200, 204]:
            map_error(status_code=response.status_code,
                      response=response, error_map=error_map)
            error = self._deserialize(models.ErrorResponse, response)
            raise HttpResponseError(
                response=response, model=error, error_format=ARMErrorFormat)

        if cls:
            return cls(pipeline_response, None, {})
    delete.metadata = {
        'url': '/subscriptions/{subscriptionId}/providers/Microsoft.ProviderHub/providerRegistrations/{providerNamespace}/resourcetypeRegistrations/'}  # type: ignore
