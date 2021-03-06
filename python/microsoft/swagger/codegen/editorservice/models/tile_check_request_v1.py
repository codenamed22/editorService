# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TileCheckRequestV1(Model):
    """TileCheck API V1 request definition.

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
    :param descriptors: List of descriptors that define the calling
     application instance properties.
    :type descriptors:
     list[~microsoft.swagger.codegen.editorservice.models.Descriptor]
    :param language_ux_id: User current UX language ISO ID. Example: fr-fr for
     French (France) Default: the LanguageId (Not supported yet!)."
    :type language_ux_id: str
    :param run_on_profile_id: Profile ID assigned by NLX team - please contact
     us for more information. The default is the one selected for the specified
     AppID.
    :type run_on_profile_id: str
    :param overridden_critique_type_options: List of critique types overrides
     from the default values.
    :type overridden_critique_type_options:
     list[~microsoft.swagger.codegen.editorservice.models.CritiqueTypeOption]
    :param session_id: Generated by the client to track the user session Id.
     SessionId is required for scenarios which use NL Cache. This is another
     way of sending session id if it cannot be send in header.
    :type session_id: str
    :param request_order_in_session: Number that is monotonically increasing
     in each request for the given session. This field is required for
     scenarios which use NL Cache. Value should be non negative value.
    :type request_order_in_session: int
    :param content: List of tiles provided for analyzing.
    :type content:
     list[~microsoft.swagger.codegen.editorservice.models.TileContent]
    :param topology: Topology of the document. Contains part of (or whole)
     graph of the document.
    :type topology:
     ~microsoft.swagger.codegen.editorservice.models.TopologyNode
    """

    _validation = {
        'app_id': {'required': True},
        'language_ux_id': {'required': True},
        'session_id': {'required': True},
    }

    _attribute_map = {
        'app_id': {'key': 'AppId', 'type': 'str'},
        'descriptors': {'key': 'Descriptors', 'type': '[Descriptor]'},
        'language_ux_id': {'key': 'LanguageUXId', 'type': 'str'},
        'run_on_profile_id': {'key': 'RunOnProfileId', 'type': 'str'},
        'overridden_critique_type_options': {'key': 'OverriddenCritiqueTypeOptions', 'type': '[CritiqueTypeOption]'},
        'session_id': {'key': 'SessionId', 'type': 'str'},
        'request_order_in_session': {'key': 'RequestOrderInSession', 'type': 'int'},
        'content': {'key': 'Content', 'type': '[TileContent]'},
        'topology': {'key': 'Topology', 'type': 'TopologyNode'},
    }

    def __init__(self, app_id, language_ux_id, session_id, descriptors=None, run_on_profile_id=None, overridden_critique_type_options=None, request_order_in_session=None, content=None, topology=None):
        super(TileCheckRequestV1, self).__init__()
        self.app_id = app_id
        self.descriptors = descriptors
        self.language_ux_id = language_ux_id
        self.run_on_profile_id = run_on_profile_id
        self.overridden_critique_type_options = overridden_critique_type_options
        self.session_id = session_id
        self.request_order_in_session = request_order_in_session
        self.content = content
        self.topology = topology
