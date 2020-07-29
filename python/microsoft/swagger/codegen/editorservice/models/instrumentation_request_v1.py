# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InstrumentationRequestV1(Model):
    """Instrumentation API request definition.

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
    :param language_id: Editing language identifier with variants (e.g. en-us,
     en-gb, de-de-1996), see
     http://www.i18nguy.com/unicode/language-identifiers.html
    :type language_id: str
    :param descriptors: List of descriptors that define the calling
     application instance properties.
    :type descriptors:
     list[~microsoft.swagger.codegen.editorservice.models.Descriptor]
    :param trace_id: Id of the critique actioned by the user.
    :type trace_id: str
    :param critique_generation_time: Time taken for server to generate
     critique in miliseconds.
    :type critique_generation_time: int
    :param critique_priority: Error priority level to be shown to the client
     app which will be interpreted as different squiggle colors (or not
     squiggle):
     * High = 0, // The highest priority (must be fixed). Example: Spelling
     * Medium = 1, // Can be fixed or may not be a problem. Example: Grammar
     * Low = 2, // Can be completely ignored and the content will still be OK.
     Example: Consistency, Style, etc.
     * Informational = 3, // Informational critique, not an error
    :type critique_priority: int
    :param critique_type_id: Id of the critique type which generated the
     critique.
    :type critique_type_id: str
    :param event_id: One of:
     * 0 = Ignore
     * 1 = IgnoreAll
     * 2 = AddToDictionary
     * 3 = Delete
     * 4 = ChangeSugg0
     * 5 = ChangeSugg1
     * 6 = ChangeSugg2
     * 7 = ChangeSuggOther
     * 8 = ChangeAllSugg0
     * 9 = ChangeAllSugg1
     * 10 = ChangeAllSugg2
     * 11 = ChangeAllSuggOther
     * 12 = ClickNoAction,
     * 13 = DoNotCheckThisIssue
     . Possible values include: 'Ignore', 'IgnoreAll', 'AddToDictionary',
     'Delete', 'ChangeSugg0', 'ChangeSugg1', 'ChangeSugg2', 'ChangeSuggOther',
     'ChangeAllSugg0', 'ChangeAllSugg1', 'ChangeAllSugg2',
     'ChangeAllSuggOther', 'ClickNoAction', 'DoNotCheckThisIssue'
    :type event_id: str or
     ~microsoft.swagger.codegen.editorservice.models.enum
    :param flagged_text: The text actioned by the user.
    :type flagged_text: str
    :param original_text: The original text in which error exists.
    :type original_text: str
    :param pre_context_begin: Start index of context within original text
    :type pre_context_begin: int
    :param post_context_end: End index of context within original text
    :type post_context_end: int
    :param suggestions: List of suggestions for the error
    :type suggestions: list[str]
    :param suggestion_text: The suggestion text selected by the user.
    :type suggestion_text: str
    """

    _validation = {
        'app_id': {'required': True},
        'language_id': {'required': True},
        'trace_id': {'required': True},
        'critique_priority': {'required': True},
        'critique_type_id': {'required': True},
        'event_id': {'required': True},
        'flagged_text': {'required': True, 'max_length': 20000, 'min_length': 1},
        'suggestion_text': {'max_length': 20000},
    }

    _attribute_map = {
        'app_id': {'key': 'AppId', 'type': 'str'},
        'language_id': {'key': 'LanguageId', 'type': 'str'},
        'descriptors': {'key': 'Descriptors', 'type': '[Descriptor]'},
        'trace_id': {'key': 'TraceId', 'type': 'str'},
        'critique_generation_time': {'key': 'CritiqueGenerationTime', 'type': 'int'},
        'critique_priority': {'key': 'CritiquePriority', 'type': 'int'},
        'critique_type_id': {'key': 'CritiqueTypeId', 'type': 'str'},
        'event_id': {'key': 'EventId', 'type': 'str'},
        'flagged_text': {'key': 'FlaggedText', 'type': 'str'},
        'original_text': {'key': 'OriginalText', 'type': 'str'},
        'pre_context_begin': {'key': 'PreContextBegin', 'type': 'int'},
        'post_context_end': {'key': 'PostContextEnd', 'type': 'int'},
        'suggestions': {'key': 'Suggestions', 'type': '[str]'},
        'suggestion_text': {'key': 'SuggestionText', 'type': 'str'},
    }

    def __init__(self, app_id, language_id, trace_id, critique_priority, critique_type_id, event_id, flagged_text, descriptors=None, critique_generation_time=None, original_text=None, pre_context_begin=None, post_context_end=None, suggestions=None, suggestion_text=None):
        super(InstrumentationRequestV1, self).__init__()
        self.app_id = app_id
        self.language_id = language_id
        self.descriptors = descriptors
        self.trace_id = trace_id
        self.critique_generation_time = critique_generation_time
        self.critique_priority = critique_priority
        self.critique_type_id = critique_type_id
        self.event_id = event_id
        self.flagged_text = flagged_text
        self.original_text = original_text
        self.pre_context_begin = pre_context_begin
        self.post_context_end = post_context_end
        self.suggestions = suggestions
        self.suggestion_text = suggestion_text
