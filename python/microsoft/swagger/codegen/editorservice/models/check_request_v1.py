# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CheckRequestV1(Model):
    """Check API V1 request definition.

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
    :param run_on_profile_id: Profile ID assigned by NLX team - please contact
     us for more information. The default is the one selected for the specified
     AppID.
    :type run_on_profile_id: str
    :param text_unit: Unit(s) of text flags:
     * Default = 0x0000, // Default value
     * Word = 0x0001, // Unigram
     * Phrase = 0x0002, // 7-gram
     * Sentence = 0x0004, // Linguistically accurate sentence
     * Paragraph = 0x0008, // Text terminated by paragraph marker(s)
     * Page = 0x0010, // A visible page, slide, equivalent unit.
     * Section = 0x0020, // Section of document/presentation
     * Chapter = 0x0040, // Chapter if such a concept exists in model
     * Document = 0x0100, // Full document contents.
     * RawChars = 0x4000, // Special purpose for scenarios that need raw
     content access
     . Possible values include: 'Default', 'Word', 'Phrase', 'Sentence',
     'Paragraph', 'Page', 'Section', 'Chapter', 'Document', 'RawChars'
    :type text_unit: str or
     ~microsoft.swagger.codegen.editorservice.models.enum
    :param overridden_critique_type_options: List of critique types overrides
     from the default values.
    :type overridden_critique_type_options:
     list[~microsoft.swagger.codegen.editorservice.models.CritiqueTypeOption]
    :param client_suggestions: Client suggestions passed on the server side.
     Default: do not use client suggestions.
    :type client_suggestions:
     list[~microsoft.swagger.codegen.editorservice.models.ClientSuggestion]
    :param length: Length of the text to be checked. Default: The entire
     content of Text. Default value: 0 .
    :type length: int
    :param request_id: Unique call identifier generated by the caller.
     Deprecated - use X-CorrelationId instead.
    :type request_id: str
    :param start: Init index for the text to be checked. Default value: 0 .
    :type start: int
    :param text: Text to be checked.
    :type text: str
    :param document_structure_metadata: Optional information about the
     document that contains the text to be checked. At the moment, this is
     leveraged only for paragraph level checking.
    :type document_structure_metadata:
     ~microsoft.swagger.codegen.editorservice.models.DocumentStructureMetadata
    """

    _validation = {
        'app_id': {'required': True},
        'language_id': {'required': True},
        'text': {'required': True},
    }

    _attribute_map = {
        'app_id': {'key': 'AppId', 'type': 'str'},
        'app_version': {'key': 'AppVersion', 'type': 'str'},
        'descriptors': {'key': 'Descriptors', 'type': '[Descriptor]'},
        'language_id': {'key': 'LanguageId', 'type': 'str'},
        'language_ux_id': {'key': 'LanguageUXId', 'type': 'str'},
        'run_on_profile_id': {'key': 'RunOnProfileId', 'type': 'str'},
        'text_unit': {'key': 'TextUnit', 'type': 'str'},
        'overridden_critique_type_options': {'key': 'OverriddenCritiqueTypeOptions', 'type': '[CritiqueTypeOption]'},
        'client_suggestions': {'key': 'ClientSuggestions', 'type': '[ClientSuggestion]'},
        'length': {'key': 'Length', 'type': 'int'},
        'request_id': {'key': 'RequestId', 'type': 'str'},
        'start': {'key': 'Start', 'type': 'int'},
        'text': {'key': 'Text', 'type': 'str'},
        'document_structure_metadata': {'key': 'DocumentStructureMetadata', 'type': 'DocumentStructureMetadata'},
    }

    def __init__(self, app_id, language_id, text, app_version=None, descriptors=None, language_ux_id=None, run_on_profile_id=None, text_unit=None, overridden_critique_type_options=None, client_suggestions=None, length=0, request_id=None, start=0, document_structure_metadata=None):
        super(CheckRequestV1, self).__init__()
        self.app_id = app_id
        self.app_version = app_version
        self.descriptors = descriptors
        self.language_id = language_id
        self.language_ux_id = language_ux_id
        self.run_on_profile_id = run_on_profile_id
        self.text_unit = text_unit
        self.overridden_critique_type_options = overridden_critique_type_options
        self.client_suggestions = client_suggestions
        self.length = length
        self.request_id = request_id
        self.start = start
        self.text = text
        self.document_structure_metadata = document_structure_metadata
