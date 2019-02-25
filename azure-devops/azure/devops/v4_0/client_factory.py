# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------


class ClientFactoryV4_0(object):
    """ClientFactoryV4_0.
    A factory class to get the 4.0 clients.
    """

    def __init__(self, connection):
        self._connection = connection

    def get_accounts_client(self):
        """get_accounts_client.
        Gets the 4.0 version of the AccountsClient
        :rtype: :class:`<AccountsClient> <azure.devops.v4_0.accounts.accounts_client.AccountsClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.accounts.accounts_client.AccountsClient')

    def get_build_client(self):
        """get_build_client.
        Gets the 4.0 version of the BuildClient
        :rtype: :class:`<BuildClient> <azure.devops.v4_0.build.build_client.BuildClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.build.build_client.BuildClient')

    def get_contributions_client(self):
        """get_contributions_client.
        Gets the 4.0 version of the ContributionsClient
        :rtype: :class:`<ContributionsClient> <azure.devops.v4_0.contributions.contributions_client.ContributionsClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.contributions.contributions_client.ContributionsClient')

    def get_core_client(self):
        """get_core_client.
        Gets the 4.0 version of the CoreClient
        :rtype: :class:`<CoreClient> <azure.devops.v4_0.core.core_client.CoreClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.core.core_client.CoreClient')

    def get_customer_intelligence_client(self):
        """get_customer_intelligence_client.
        Gets the 4.0 version of the CustomerIntelligenceClient
        :rtype: :class:`<CustomerIntelligenceClient> <azure.devops.v4_0.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.customer_intelligence.customer_intelligence_client.CustomerIntelligenceClient')

    def get_dashboard_client(self):
        """get_dashboard_client.
        Gets the 4.0 version of the DashboardClient
        :rtype: :class:`<DashboardClient> <azure.devops.v4_0.dashboard.dashboard_client.DashboardClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.dashboard.dashboard_client.DashboardClient')

    def get_extension_management_client(self):
        """get_extension_management_client.
        Gets the 4.0 version of the ExtensionManagementClient
        :rtype: :class:`<ExtensionManagementClient> <azure.devops.v4_0.extension_management.extension_management_client.ExtensionManagementClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.extension_management.extension_management_client.ExtensionManagementClient')

    def get_feature_availability_client(self):
        """get_feature_availability_client.
        Gets the 4.0 version of the FeatureAvailabilityClient
        :rtype: :class:`<FeatureAvailabilityClient> <azure.devops.v4_0.feature_availability.feature_availability_client.FeatureAvailabilityClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.feature_availability.feature_availability_client.FeatureAvailabilityClient')

    def get_feature_management_client(self):
        """get_feature_management_client.
        Gets the 4.0 version of the FeatureManagementClient
        :rtype: :class:`<FeatureManagementClient> <azure.devops.v4_0.feature_management.feature_management_client.FeatureManagementClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.feature_management.feature_management_client.FeatureManagementClient')

    def get_file_container_client(self):
        """get_file_container_client.
        Gets the 4.0 version of the FileContainerClient
        :rtype: :class:`<FileContainerClient> <azure.devops.v4_0.file_container.file_container_client.FileContainerClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.file_container.file_container_client.FileContainerClient')

    def get_gallery_client(self):
        """get_gallery_client.
        Gets the 4.0 version of the GalleryClient
        :rtype: :class:`<GalleryClient> <azure.devops.v4_0.gallery.gallery_client.GalleryClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.gallery.gallery_client.GalleryClient')

    def get_git_client(self):
        """get_git_client.
        Gets the 4.0 version of the GitClient
        :rtype: :class:`<GitClient> <azure.devops.v4_0.git.git_client.GitClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.git.git_client.GitClient')

    def get_identity_client(self):
        """get_identity_client.
        Gets the 4.0 version of the IdentityClient
        :rtype: :class:`<IdentityClient> <azure.devops.v4_0.identity.identity_client.IdentityClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.identity.identity_client.IdentityClient')

    def get_licensing_client(self):
        """get_licensing_client.
        Gets the 4.0 version of the LicensingClient
        :rtype: :class:`<LicensingClient> <azure.devops.v4_0.licensing.licensing_client.LicensingClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.licensing.licensing_client.LicensingClient')

    def get_location_client(self):
        """get_location_client.
        Gets the 4.0 version of the LocationClient
        :rtype: :class:`<LocationClient> <azure.devops.v4_0.location.location_client.LocationClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.location.location_client.LocationClient')

    def get_member_entitlement_management_client(self):
        """get_member_entitlement_management_client.
        Gets the 4.0 version of the MemberEntitlementManagementClient
        :rtype: :class:`<MemberEntitlementManagementClient> <azure.devops.v4_0.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.member_entitlement_management.member_entitlement_management_client.MemberEntitlementManagementClient')

    def get_notification_client(self):
        """get_notification_client.
        Gets the 4.0 version of the NotificationClient
        :rtype: :class:`<NotificationClient> <azure.devops.v4_0.notification.notification_client.NotificationClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.notification.notification_client.NotificationClient')

    def get_operations_client(self):
        """get_operations_client.
        Gets the 4.0 version of the OperationsClient
        :rtype: :class:`<OperationsClient> <azure.devops.v4_0.operations.operations_client.OperationsClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.operations.operations_client.OperationsClient')

    def get_policy_client(self):
        """get_policy_client.
        Gets the 4.0 version of the PolicyClient
        :rtype: :class:`<PolicyClient> <azure.devops.v4_0.policy.policy_client.PolicyClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.policy.policy_client.PolicyClient')

    def get_project_analysis_client(self):
        """get_project_analysis_client.
        Gets the 4.0 version of the ProjectAnalysisClient
        :rtype: :class:`<ProjectAnalysisClient> <azure.devops.v4_0.project_analysis.project_analysis_client.ProjectAnalysisClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.project_analysis.project_analysis_client.ProjectAnalysisClient')

    def get_release_client(self):
        """get_release_client.
        Gets the 4.0 version of the ReleaseClient
        :rtype: :class:`<ReleaseClient> <azure.devops.v4_0.release.release_client.ReleaseClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.release.release_client.ReleaseClient')

    def get_security_client(self):
        """get_security_client.
        Gets the 4.0 version of the SecurityClient
        :rtype: :class:`<SecurityClient> <azure.devops.v4_0.security.security_client.SecurityClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.security.security_client.SecurityClient')

    def get_service_hooks_client(self):
        """get_service_hooks_client.
        Gets the 4.0 version of the ServiceHooksClient
        :rtype: :class:`<ServiceHooksClient> <azure.devops.v4_0.service_hooks.service_hooks_client.ServiceHooksClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.service_hooks.service_hooks_client.ServiceHooksClient')

    def get_settings_client(self):
        """get_settings_client.
        Gets the 4.0 version of the SettingsClient
        :rtype: :class:`<SettingsClient> <azure.devops.v4_0.settings.settings_client.SettingsClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.settings.settings_client.SettingsClient')

    def get_task_client(self):
        """get_task_client.
        Gets the 4.0 version of the TaskClient
        :rtype: :class:`<TaskClient> <azure.devops.v4_0.task.task_client.TaskClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.task.task_client.TaskClient')

    def get_task_agent_client(self):
        """get_task_agent_client.
        Gets the 4.0 version of the TaskAgentClient
        :rtype: :class:`<TaskAgentClient> <azure.devops.v4_0.task_agent.task_agent_client.TaskAgentClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.task_agent.task_agent_client.TaskAgentClient')

    def get_test_client(self):
        """get_test_client.
        Gets the 4.0 version of the TestClient
        :rtype: :class:`<TestClient> <azure.devops.v4_0.test.test_client.TestClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.test.test_client.TestClient')

    def get_tfvc_client(self):
        """get_tfvc_client.
        Gets the 4.0 version of the TfvcClient
        :rtype: :class:`<TfvcClient> <azure.devops.v4_0.tfvc.tfvc_client.TfvcClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.tfvc.tfvc_client.TfvcClient')

    def get_wiki_client(self):
        """get_wiki_client.
        Gets the 4.0 version of the WikiClient
        :rtype: :class:`<WikiClient> <azure.devops.v4_0.wiki.wiki_client.WikiClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.wiki.wiki_client.WikiClient')

    def get_work_client(self):
        """get_work_client.
        Gets the 4.0 version of the WorkClient
        :rtype: :class:`<WorkClient> <azure.devops.v4_0.work.work_client.WorkClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.work.work_client.WorkClient')

    def get_work_item_tracking_client(self):
        """get_work_item_tracking_client.
        Gets the 4.0 version of the WorkItemTrackingClient
        :rtype: :class:`<WorkItemTrackingClient> <azure.devops.v4_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.work_item_tracking.work_item_tracking_client.WorkItemTrackingClient')

    def get_work_item_tracking_process_client(self):
        """get_work_item_tracking_process_client.
        Gets the 4.0 version of the WorkItemTrackingProcessClient
        :rtype: :class:`<WorkItemTrackingProcessClient> <azure.devops.v4_0.work_item_tracking_process.work_item_tracking_process_client.WorkItemTrackingProcessClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.work_item_tracking_process.work_item_tracking_process_client.WorkItemTrackingProcessClient')

    def get_work_item_tracking_process_definitions_client(self):
        """get_work_item_tracking_process_definitions_client.
        Gets the 4.0 version of the WorkItemTrackingProcessDefinitionsClient
        :rtype: :class:`<WorkItemTrackingProcessDefinitionsClient> <azure.devops.v4_0.work_item_tracking_process_definitions.work_item_tracking_process_definitions_client.WorkItemTrackingProcessDefinitionsClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.work_item_tracking_process_definitions.work_item_tracking_process_definitions_client.WorkItemTrackingProcessDefinitionsClient')

    def get_work_item_tracking_process_template_client(self):
        """get_work_item_tracking_process_template_client.
        Gets the 4.0 version of the WorkItemTrackingProcessTemplateClient
        :rtype: :class:`<WorkItemTrackingProcessTemplateClient> <azure.devops.v4_0.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient>`
        """
        return self._connection.get_client('azure.devops.v4_0.work_item_tracking_process_template.work_item_tracking_process_template_client.WorkItemTrackingProcessTemplateClient')

