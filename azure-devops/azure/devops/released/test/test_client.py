# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------
# Generated file, DO NOT EDIT
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------------------------

from msrest import Serializer, Deserializer
from ...client import Client
from ...v4_1.test import models


class TestClient(Client):
    """Test
    :param str base_url: Service URL
    :param Authentication creds: Authenticated credentials.
    """

    def __init__(self, base_url=None, creds=None):
        super(TestClient, self).__init__(base_url, creds)
        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

    resource_area_identifier = 'c2aa639c-3ccc-4740-b3b6-ce2a1e1d984e'

    def get_action_results(self, project, run_id, test_case_result_id, iteration_id, action_path=None):
        """GetActionResults.
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int iteration_id:
        :param str action_path:
        :rtype: [TestActionResultModel]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        if action_path is not None:
            route_values['actionPath'] = self._serialize.url('action_path', action_path, 'str')
        response = self._send(http_method='GET',
                              location_id='eaf40c31-ff84-4062-aafd-d5664be11a37',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[TestActionResultModel]', self._unwrap_collection(response))

    def get_test_iteration(self, project, run_id, test_case_result_id, iteration_id, include_action_results=None):
        """GetTestIteration.
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int iteration_id:
        :param bool include_action_results:
        :rtype: :class:`<TestIterationDetailsModel> <azure.devops.v4_1.test.models.TestIterationDetailsModel>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        query_parameters = {}
        if include_action_results is not None:
            query_parameters['includeActionResults'] = self._serialize.query('include_action_results', include_action_results, 'bool')
        response = self._send(http_method='GET',
                              location_id='73eb9074-3446-4c44-8296-2f811950ff8d',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestIterationDetailsModel', response)

    def get_test_iterations(self, project, run_id, test_case_result_id, include_action_results=None):
        """GetTestIterations.
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param bool include_action_results:
        :rtype: [TestIterationDetailsModel]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if include_action_results is not None:
            query_parameters['includeActionResults'] = self._serialize.query('include_action_results', include_action_results, 'bool')
        response = self._send(http_method='GET',
                              location_id='73eb9074-3446-4c44-8296-2f811950ff8d',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestIterationDetailsModel]', self._unwrap_collection(response))

    def get_result_parameters(self, project, run_id, test_case_result_id, iteration_id, param_name=None):
        """GetResultParameters.
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param int iteration_id:
        :param str param_name:
        :rtype: [TestResultParameterModel]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        if iteration_id is not None:
            route_values['iterationId'] = self._serialize.url('iteration_id', iteration_id, 'int')
        query_parameters = {}
        if param_name is not None:
            query_parameters['paramName'] = self._serialize.query('param_name', param_name, 'str')
        response = self._send(http_method='GET',
                              location_id='7c69810d-3354-4af3-844a-180bd25db08a',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestResultParameterModel]', self._unwrap_collection(response))

    def create_test_plan(self, test_plan, project):
        """CreateTestPlan.
        :param :class:`<PlanUpdateModel> <azure.devops.v4_1.test.models.PlanUpdateModel>` test_plan:
        :param str project: Project ID or project name
        :rtype: :class:`<TestPlan> <azure.devops.v4_1.test.models.TestPlan>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_plan, 'PlanUpdateModel')
        response = self._send(http_method='POST',
                              location_id='51712106-7278-4208-8563-1c96f40cf5e4',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestPlan', response)

    def delete_test_plan(self, project, plan_id):
        """DeleteTestPlan.
        :param str project: Project ID or project name
        :param int plan_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        self._send(http_method='DELETE',
                   location_id='51712106-7278-4208-8563-1c96f40cf5e4',
                   version='4.1',
                   route_values=route_values)

    def get_plan_by_id(self, project, plan_id):
        """GetPlanById.
        :param str project: Project ID or project name
        :param int plan_id:
        :rtype: :class:`<TestPlan> <azure.devops.v4_1.test.models.TestPlan>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        response = self._send(http_method='GET',
                              location_id='51712106-7278-4208-8563-1c96f40cf5e4',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('TestPlan', response)

    def get_plans(self, project, owner=None, skip=None, top=None, include_plan_details=None, filter_active_plans=None):
        """GetPlans.
        :param str project: Project ID or project name
        :param str owner:
        :param int skip:
        :param int top:
        :param bool include_plan_details:
        :param bool filter_active_plans:
        :rtype: [TestPlan]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if owner is not None:
            query_parameters['owner'] = self._serialize.query('owner', owner, 'str')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if include_plan_details is not None:
            query_parameters['includePlanDetails'] = self._serialize.query('include_plan_details', include_plan_details, 'bool')
        if filter_active_plans is not None:
            query_parameters['filterActivePlans'] = self._serialize.query('filter_active_plans', filter_active_plans, 'bool')
        response = self._send(http_method='GET',
                              location_id='51712106-7278-4208-8563-1c96f40cf5e4',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPlan]', self._unwrap_collection(response))

    def update_test_plan(self, plan_update_model, project, plan_id):
        """UpdateTestPlan.
        :param :class:`<PlanUpdateModel> <azure.devops.v4_1.test.models.PlanUpdateModel>` plan_update_model:
        :param str project: Project ID or project name
        :param int plan_id:
        :rtype: :class:`<TestPlan> <azure.devops.v4_1.test.models.TestPlan>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        content = self._serialize.body(plan_update_model, 'PlanUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='51712106-7278-4208-8563-1c96f40cf5e4',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestPlan', response)

    def get_point(self, project, plan_id, suite_id, point_ids, wit_fields=None):
        """GetPoint.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :param int point_ids:
        :param str wit_fields:
        :rtype: :class:`<TestPoint> <azure.devops.v4_1.test.models.TestPoint>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if point_ids is not None:
            route_values['pointIds'] = self._serialize.url('point_ids', point_ids, 'int')
        query_parameters = {}
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        response = self._send(http_method='GET',
                              location_id='3bcfd5c8-be62-488e-b1da-b8289ce9299c',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestPoint', response)

    def get_points(self, project, plan_id, suite_id, wit_fields=None, configuration_id=None, test_case_id=None, test_point_ids=None, include_point_details=None, skip=None, top=None):
        """GetPoints.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :param str wit_fields:
        :param str configuration_id:
        :param str test_case_id:
        :param str test_point_ids:
        :param bool include_point_details:
        :param int skip:
        :param int top:
        :rtype: [TestPoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if wit_fields is not None:
            query_parameters['witFields'] = self._serialize.query('wit_fields', wit_fields, 'str')
        if configuration_id is not None:
            query_parameters['configurationId'] = self._serialize.query('configuration_id', configuration_id, 'str')
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'str')
        if test_point_ids is not None:
            query_parameters['testPointIds'] = self._serialize.query('test_point_ids', test_point_ids, 'str')
        if include_point_details is not None:
            query_parameters['includePointDetails'] = self._serialize.query('include_point_details', include_point_details, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='3bcfd5c8-be62-488e-b1da-b8289ce9299c',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def update_test_points(self, point_update_model, project, plan_id, suite_id, point_ids):
        """UpdateTestPoints.
        :param :class:`<PointUpdateModel> <azure.devops.v4_1.test.models.PointUpdateModel>` point_update_model:
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :param str point_ids:
        :rtype: [TestPoint]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if point_ids is not None:
            route_values['pointIds'] = self._serialize.url('point_ids', point_ids, 'str')
        content = self._serialize.body(point_update_model, 'PointUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='3bcfd5c8-be62-488e-b1da-b8289ce9299c',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestPoint]', self._unwrap_collection(response))

    def add_test_results_to_test_run(self, results, project, run_id):
        """AddTestResultsToTestRun.
        :param [TestCaseResult] results:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='POST',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_result_by_id(self, project, run_id, test_case_result_id, details_to_include=None):
        """GetTestResultById.
        :param str project: Project ID or project name
        :param int run_id:
        :param int test_case_result_id:
        :param str details_to_include:
        :rtype: :class:`<TestCaseResult> <azure.devops.v4_1.test.models.TestCaseResult>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        if test_case_result_id is not None:
            route_values['testCaseResultId'] = self._serialize.url('test_case_result_id', test_case_result_id, 'int')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        response = self._send(http_method='GET',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestCaseResult', response)

    def get_test_results(self, project, run_id, details_to_include=None, skip=None, top=None, outcomes=None):
        """GetTestResults.
        Get Test Results for a run based on filters.
        :param str project: Project ID or project name
        :param int run_id: Test Run Id for which results need to be fetched.
        :param str details_to_include: enum indicates details need to be fetched.
        :param int skip: Number of results to skip from beginning.
        :param int top: Number of results to return. Max is 1000 when detailsToInclude is None and 100 otherwise.
        :param [TestOutcome] outcomes: List of Testoutcome to filter results, comma seperated list of Testoutcome.
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        query_parameters = {}
        if details_to_include is not None:
            query_parameters['detailsToInclude'] = self._serialize.query('details_to_include', details_to_include, 'str')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if outcomes is not None:
            outcomes = ",".join(map(str, outcomes))
            query_parameters['outcomes'] = self._serialize.query('outcomes', outcomes, 'str')
        response = self._send(http_method='GET',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def update_test_results(self, results, project, run_id):
        """UpdateTestResults.
        :param [TestCaseResult] results:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: [TestCaseResult]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(results, '[TestCaseResult]')
        response = self._send(http_method='PATCH',
                              location_id='4637d869-3a76-4468-8057-0bb02aa385cf',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestCaseResult]', self._unwrap_collection(response))

    def get_test_run_statistics(self, project, run_id):
        """GetTestRunStatistics.
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestRunStatistic> <azure.devops.v4_1.test.models.TestRunStatistic>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='0a42c424-d764-4a16-a2d5-5c85f87d0ae8',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('TestRunStatistic', response)

    def create_test_run(self, test_run, project):
        """CreateTestRun.
        :param :class:`<RunCreateModel> <azure.devops.v4_1.test.models.RunCreateModel>` test_run:
        :param str project: Project ID or project name
        :rtype: :class:`<TestRun> <azure.devops.v4_1.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_run, 'RunCreateModel')
        response = self._send(http_method='POST',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def delete_test_run(self, project, run_id):
        """DeleteTestRun.
        :param str project: Project ID or project name
        :param int run_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        self._send(http_method='DELETE',
                   location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                   version='4.1',
                   route_values=route_values)

    def get_test_run_by_id(self, project, run_id):
        """GetTestRunById.
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestRun> <azure.devops.v4_1.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        response = self._send(http_method='GET',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('TestRun', response)

    def get_test_runs(self, project, build_uri=None, owner=None, tmi_run_id=None, plan_id=None, include_run_details=None, automated=None, skip=None, top=None):
        """GetTestRuns.
        :param str project: Project ID or project name
        :param str build_uri:
        :param str owner:
        :param str tmi_run_id:
        :param int plan_id:
        :param bool include_run_details:
        :param bool automated:
        :param int skip:
        :param int top:
        :rtype: [TestRun]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if build_uri is not None:
            query_parameters['buildUri'] = self._serialize.query('build_uri', build_uri, 'str')
        if owner is not None:
            query_parameters['owner'] = self._serialize.query('owner', owner, 'str')
        if tmi_run_id is not None:
            query_parameters['tmiRunId'] = self._serialize.query('tmi_run_id', tmi_run_id, 'str')
        if plan_id is not None:
            query_parameters['planId'] = self._serialize.query('plan_id', plan_id, 'int')
        if include_run_details is not None:
            query_parameters['includeRunDetails'] = self._serialize.query('include_run_details', include_run_details, 'bool')
        if automated is not None:
            query_parameters['automated'] = self._serialize.query('automated', automated, 'bool')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        response = self._send(http_method='GET',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRun]', self._unwrap_collection(response))

    def query_test_runs(self, project, min_last_updated_date, max_last_updated_date, state=None, plan_ids=None, is_automated=None, publish_context=None, build_ids=None, build_def_ids=None, branch_name=None, release_ids=None, release_def_ids=None, release_env_ids=None, release_env_def_ids=None, run_title=None, top=None, continuation_token=None):
        """QueryTestRuns.
        Query Test Runs based on filters.
        :param str project: Project ID or project name
        :param datetime min_last_updated_date: Minimum Last Modified Date of run to be queried (Mandatory).
        :param datetime max_last_updated_date: Maximum Last Modified Date of run to be queried (Mandatory, difference between min and max date can be atmost 7 days).
        :param str state: Current state of the Runs to be queried.
        :param [int] plan_ids: Plan Ids of the Runs to be queried, comma seperated list of valid ids.
        :param bool is_automated: Automation type of the Runs to be queried.
        :param str publish_context: PublishContext of the Runs to be queried.
        :param [int] build_ids: Build Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] build_def_ids: Build Definition Ids of the Runs to be queried, comma seperated list of valid ids.
        :param str branch_name: Source Branch name of the Runs to be queried.
        :param [int] release_ids: Release Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] release_def_ids: Release Definition Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] release_env_ids: Release Environment Ids of the Runs to be queried, comma seperated list of valid ids.
        :param [int] release_env_def_ids: Release Environment Definition Ids of the Runs to be queried, comma seperated list of valid ids.
        :param str run_title: Run Title of the Runs to be queried.
        :param int top: Number of runs to be queried. Limit is 100
        :param str continuation_token: continuationToken received from previous batch or null for first batch.
        :rtype: [TestRun]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        query_parameters = {}
        if min_last_updated_date is not None:
            query_parameters['minLastUpdatedDate'] = self._serialize.query('min_last_updated_date', min_last_updated_date, 'iso-8601')
        if max_last_updated_date is not None:
            query_parameters['maxLastUpdatedDate'] = self._serialize.query('max_last_updated_date', max_last_updated_date, 'iso-8601')
        if state is not None:
            query_parameters['state'] = self._serialize.query('state', state, 'str')
        if plan_ids is not None:
            plan_ids = ",".join(map(str, plan_ids))
            query_parameters['planIds'] = self._serialize.query('plan_ids', plan_ids, 'str')
        if is_automated is not None:
            query_parameters['isAutomated'] = self._serialize.query('is_automated', is_automated, 'bool')
        if publish_context is not None:
            query_parameters['publishContext'] = self._serialize.query('publish_context', publish_context, 'str')
        if build_ids is not None:
            build_ids = ",".join(map(str, build_ids))
            query_parameters['buildIds'] = self._serialize.query('build_ids', build_ids, 'str')
        if build_def_ids is not None:
            build_def_ids = ",".join(map(str, build_def_ids))
            query_parameters['buildDefIds'] = self._serialize.query('build_def_ids', build_def_ids, 'str')
        if branch_name is not None:
            query_parameters['branchName'] = self._serialize.query('branch_name', branch_name, 'str')
        if release_ids is not None:
            release_ids = ",".join(map(str, release_ids))
            query_parameters['releaseIds'] = self._serialize.query('release_ids', release_ids, 'str')
        if release_def_ids is not None:
            release_def_ids = ",".join(map(str, release_def_ids))
            query_parameters['releaseDefIds'] = self._serialize.query('release_def_ids', release_def_ids, 'str')
        if release_env_ids is not None:
            release_env_ids = ",".join(map(str, release_env_ids))
            query_parameters['releaseEnvIds'] = self._serialize.query('release_env_ids', release_env_ids, 'str')
        if release_env_def_ids is not None:
            release_env_def_ids = ",".join(map(str, release_env_def_ids))
            query_parameters['releaseEnvDefIds'] = self._serialize.query('release_env_def_ids', release_env_def_ids, 'str')
        if run_title is not None:
            query_parameters['runTitle'] = self._serialize.query('run_title', run_title, 'str')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if continuation_token is not None:
            query_parameters['continuationToken'] = self._serialize.query('continuation_token', continuation_token, 'str')
        response = self._send(http_method='GET',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestRun]', self._unwrap_collection(response))

    def update_test_run(self, run_update_model, project, run_id):
        """UpdateTestRun.
        :param :class:`<RunUpdateModel> <azure.devops.v4_1.test.models.RunUpdateModel>` run_update_model:
        :param str project: Project ID or project name
        :param int run_id:
        :rtype: :class:`<TestRun> <azure.devops.v4_1.test.models.TestRun>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if run_id is not None:
            route_values['runId'] = self._serialize.url('run_id', run_id, 'int')
        content = self._serialize.body(run_update_model, 'RunUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='cadb3810-d47d-4a3c-a234-fe5f3be50138',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestRun', response)

    def add_test_cases_to_suite(self, project, plan_id, suite_id, test_case_ids):
        """AddTestCasesToSuite.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :param str test_case_ids:
        :rtype: [SuiteTestCase]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'str')
        route_values['action'] = 'TestCases'
        response = self._send(http_method='POST',
                              location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

    def get_test_case_by_id(self, project, plan_id, suite_id, test_case_ids):
        """GetTestCaseById.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :param int test_case_ids:
        :rtype: :class:`<SuiteTestCase> <azure.devops.v4_1.test.models.SuiteTestCase>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'int')
        route_values['action'] = 'TestCases'
        response = self._send(http_method='GET',
                              location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('SuiteTestCase', response)

    def get_test_cases(self, project, plan_id, suite_id):
        """GetTestCases.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :rtype: [SuiteTestCase]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        route_values['action'] = 'TestCases'
        response = self._send(http_method='GET',
                              location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('[SuiteTestCase]', self._unwrap_collection(response))

    def remove_test_cases_from_suite_url(self, project, plan_id, suite_id, test_case_ids):
        """RemoveTestCasesFromSuiteUrl.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :param str test_case_ids:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        if test_case_ids is not None:
            route_values['testCaseIds'] = self._serialize.url('test_case_ids', test_case_ids, 'str')
        route_values['action'] = 'TestCases'
        self._send(http_method='DELETE',
                   location_id='a4a1ec1c-b03f-41ca-8857-704594ecf58e',
                   version='4.1',
                   route_values=route_values)

    def create_test_suite(self, test_suite, project, plan_id, suite_id):
        """CreateTestSuite.
        :param :class:`<SuiteCreateModel> <azure.devops.v4_1.test.models.SuiteCreateModel>` test_suite:
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :rtype: [TestSuite]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(test_suite, 'SuiteCreateModel')
        response = self._send(http_method='POST',
                              location_id='7b7619a0-cb54-4ab3-bf22-194056f45dd1',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('[TestSuite]', self._unwrap_collection(response))

    def delete_test_suite(self, project, plan_id, suite_id):
        """DeleteTestSuite.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        self._send(http_method='DELETE',
                   location_id='7b7619a0-cb54-4ab3-bf22-194056f45dd1',
                   version='4.1',
                   route_values=route_values)

    def get_test_suite_by_id(self, project, plan_id, suite_id, expand=None):
        """GetTestSuiteById.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :param int expand:
        :rtype: :class:`<TestSuite> <azure.devops.v4_1.test.models.TestSuite>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'int')
        response = self._send(http_method='GET',
                              location_id='7b7619a0-cb54-4ab3-bf22-194056f45dd1',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('TestSuite', response)

    def get_test_suites_for_plan(self, project, plan_id, expand=None, skip=None, top=None, as_tree_view=None):
        """GetTestSuitesForPlan.
        :param str project: Project ID or project name
        :param int plan_id:
        :param int expand:
        :param int skip:
        :param int top:
        :param bool as_tree_view:
        :rtype: [TestSuite]
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        query_parameters = {}
        if expand is not None:
            query_parameters['$expand'] = self._serialize.query('expand', expand, 'int')
        if skip is not None:
            query_parameters['$skip'] = self._serialize.query('skip', skip, 'int')
        if top is not None:
            query_parameters['$top'] = self._serialize.query('top', top, 'int')
        if as_tree_view is not None:
            query_parameters['$asTreeView'] = self._serialize.query('as_tree_view', as_tree_view, 'bool')
        response = self._send(http_method='GET',
                              location_id='7b7619a0-cb54-4ab3-bf22-194056f45dd1',
                              version='4.1',
                              route_values=route_values,
                              query_parameters=query_parameters)
        return self._deserialize('[TestSuite]', self._unwrap_collection(response))

    def update_test_suite(self, suite_update_model, project, plan_id, suite_id):
        """UpdateTestSuite.
        :param :class:`<SuiteUpdateModel> <azure.devops.v4_1.test.models.SuiteUpdateModel>` suite_update_model:
        :param str project: Project ID or project name
        :param int plan_id:
        :param int suite_id:
        :rtype: :class:`<TestSuite> <azure.devops.v4_1.test.models.TestSuite>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if plan_id is not None:
            route_values['planId'] = self._serialize.url('plan_id', plan_id, 'int')
        if suite_id is not None:
            route_values['suiteId'] = self._serialize.url('suite_id', suite_id, 'int')
        content = self._serialize.body(suite_update_model, 'SuiteUpdateModel')
        response = self._send(http_method='PATCH',
                              location_id='7b7619a0-cb54-4ab3-bf22-194056f45dd1',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('TestSuite', response)

    def get_suites_by_test_case_id(self, test_case_id):
        """GetSuitesByTestCaseId.
        :param int test_case_id:
        :rtype: [TestSuite]
        """
        query_parameters = {}
        if test_case_id is not None:
            query_parameters['testCaseId'] = self._serialize.query('test_case_id', test_case_id, 'int')
        response = self._send(http_method='GET',
                              location_id='09a6167b-e969-4775-9247-b94cf3819caf',
                              version='4.1',
                              query_parameters=query_parameters)
        return self._deserialize('[TestSuite]', self._unwrap_collection(response))

    def create_test_settings(self, test_settings, project):
        """CreateTestSettings.
        :param :class:`<TestSettings> <azure.devops.v4_1.test.models.TestSettings>` test_settings:
        :param str project: Project ID or project name
        :rtype: int
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        content = self._serialize.body(test_settings, 'TestSettings')
        response = self._send(http_method='POST',
                              location_id='8133ce14-962f-42af-a5f9-6aa9defcb9c8',
                              version='4.1',
                              route_values=route_values,
                              content=content)
        return self._deserialize('int', response)

    def delete_test_settings(self, project, test_settings_id):
        """DeleteTestSettings.
        :param str project: Project ID or project name
        :param int test_settings_id:
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_settings_id is not None:
            route_values['testSettingsId'] = self._serialize.url('test_settings_id', test_settings_id, 'int')
        self._send(http_method='DELETE',
                   location_id='8133ce14-962f-42af-a5f9-6aa9defcb9c8',
                   version='4.1',
                   route_values=route_values)

    def get_test_settings_by_id(self, project, test_settings_id):
        """GetTestSettingsById.
        :param str project: Project ID or project name
        :param int test_settings_id:
        :rtype: :class:`<TestSettings> <azure.devops.v4_1.test.models.TestSettings>`
        """
        route_values = {}
        if project is not None:
            route_values['project'] = self._serialize.url('project', project, 'str')
        if test_settings_id is not None:
            route_values['testSettingsId'] = self._serialize.url('test_settings_id', test_settings_id, 'int')
        response = self._send(http_method='GET',
                              location_id='8133ce14-962f-42af-a5f9-6aa9defcb9c8',
                              version='4.1',
                              route_values=route_values)
        return self._deserialize('TestSettings', response)

