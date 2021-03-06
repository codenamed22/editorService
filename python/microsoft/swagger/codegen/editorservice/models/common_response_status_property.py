# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommonResponseStatusProperty(Model):
    """CommonResponseStatusProperty.

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
    """

    _attribute_map = {
        'response_status': {'key': 'ResponseStatus', 'type': 'str'},
    }

    def __init__(self, response_status="Success"):
        super(CommonResponseStatusProperty, self).__init__()
        self.response_status = response_status
