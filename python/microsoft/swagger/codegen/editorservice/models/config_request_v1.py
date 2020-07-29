# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ConfigRequestV1(Model):
    """Config API V1 request definition.

    :param app_id: Id of the calling app, the supported ones are the
     following:
     * LinkedIn
     * NLServiceTestAutomation - Id used by automated tests
     * OAM - Id used by the probes
     * OneNote_Online, PowerPoint_Online, Word_Online - WAC
     * Testing_Client - Use for testing and prototyping
     . Possible values include: 'LinkedIn', 'NLServiceTestAutomation', 'OAM',
     'OneNote_Online', 'Testing_Client', 'PowerPoint_Online', 'Word_Online'
    :type app_id: str or ~microsoft.swagger.codegen.editorservice.models.enum
    :param app_version: Version of the calling application.
    :type app_version: str
    :param descriptors: List of descriptors that define the calling
     application instance properties.
    :type descriptors:
     list[~microsoft.swagger.codegen.editorservice.models.Descriptor]
    :param language_id: Editing language identifier with variants (e.g. en-us,
     en-gb, de-de-1996), see
     http://www.i18nguy.com/unicode/language-identifiers.html
    :type language_id: str
    :param language_ux_id: User current UX language ISO ID. Example: fr-fr for
     French (France) Default: the LanguageId (Not supported yet!)."
    :type language_ux_id: str
    :param request_id: Unique call identifier generated by the caller (GUID)
    :type request_id: str
    :param run_on_profile_id: Profile ID assigned by NLX team - please contact
     us for more information. The default is the one selected for the specified
     AppID.
    :type run_on_profile_id: str
    """

    _validation = {
        'app_id': {'required': True},
        'language_id': {'required': True},
    }

    _attribute_map = {
        'app_id': {'key': 'AppId', 'type': 'str'},
        'app_version': {'key': 'AppVersion', 'type': 'str'},
        'descriptors': {'key': 'Descriptors', 'type': '[Descriptor]'},
        'language_id': {'key': 'LanguageId', 'type': 'str'},
        'language_ux_id': {'key': 'LanguageUXId', 'type': 'str'},
        'request_id': {'key': 'RequestId', 'type': 'str'},
        'run_on_profile_id': {'key': 'RunOnProfileId', 'type': 'str'},
    }

    def __init__(self, app_id, language_id, app_version=None, descriptors=None, language_ux_id=None, request_id=None, run_on_profile_id=None):
        super(ConfigRequestV1, self).__init__()
        self.app_id = app_id
        self.app_version = app_version
        self.descriptors = descriptors
        self.language_id = language_id
        self.language_ux_id = language_ux_id
        self.request_id = request_id
        self.run_on_profile_id = run_on_profile_id
