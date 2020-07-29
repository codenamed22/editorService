# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigResponseV1(Model):
    """Config API V1 response definition.

    :param response_status: Gives information about the completeness of the
     results.
     * Success = 0: All components ran and the results are complete.
     * PartialSuccess = 1: Some of the components ran successfully.
     Other components either failed or timed out. We don't have
     the complete results, but we will return the critiques we have.
     * Error = 2: All components failed or timed out, or there's a problem with
     the profile.
     * Disabled = 3: Controller or Orchestrator disabled.
     . Possible values include: 'Success', 'PartialSuccess', 'Error',
     'Disabled'. Default value: "Success" .
    :type response_status: str or
     ~microsoft.swagger.codegen.editorservice.models.enum
    :param request_id: Unique call identifier generated by the caller (GUID)
    :type request_id: str
    :param profiles: A list of profiles, which includes critique category and
     type information for a particular profile
    :type profiles:
     list[~microsoft.swagger.codegen.editorservice.models.Profile]
    """

    _validation = {
        'response_status': {'required': True},
        'request_id': {'required': True},
        'profiles': {'required': True},
    }

    _attribute_map = {
        'response_status': {'key': 'ResponseStatus', 'type': 'str'},
        'request_id': {'key': 'RequestId', 'type': 'str'},
        'profiles': {'key': 'Profiles', 'type': '[Profile]'},
    }

    def __init__(self, request_id, profiles, response_status="Success"):
        super(ConfigResponseV1, self).__init__()
        self.response_status = response_status
        self.request_id = request_id
        self.profiles = profiles
