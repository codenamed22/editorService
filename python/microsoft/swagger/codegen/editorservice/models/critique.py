# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Critique(Model):
    """Critique.

    :param trace_id: A unique identifier for the critique returned to the
     caller: this is used for the feedback/instrumentation loop.
    :type trace_id: str
    :param type_id: Id of the critique type which generated the critique.
    :type type_id: str
    :param category_title: The title of the critique category.
    :type category_title: str
    :param start: Critique flag start index. Default value: 0 .
    :type start: int
    :param length: Critique flag length. Default value: 0 .
    :type length: int
    :param priority: Error priority level to be shown to the client app which
     will be interpreted as different squiggle colors (or not squiggle):
     * High = 0, // The highest priority (must be fixed). Example: Spelling
     * Medium = 1, // Can be fixed or may not be a problem. Example: Grammar
     * Low = 2, // Can be completely ignored and the content will still be OK..
     Example: Consistency, Style, etc.
     * Informational = 3, // Informational critique, not an error
    :type priority: int
    :param paragraph_id: Unique identifier of paragraph within a document.
     NOTE: This is going to be deprecated -> use more generic TileId instead.
    :type paragraph_id: str
    :param paragraph_revision_id: Number that is changed whenever a paragraph
     is changed. NOTE: This is going to be deprecated -> use more generic
     RevisionId instead.
    :type paragraph_revision_id: str
    :param tile_id: Request: Unique identifier of tile within a document.
     Response: Id of the tile the critique belongs to
    :type tile_id: str
    :param revision_id: Request: Number that is changed whenever a tile is
     changed. Response: Revision id of the tile critique belongs to
    :type revision_id: str
    :param supported_actions: Actions that a critique supports, expressed as
     flags that can be combined:
     * NotificationOnly = 0x00, // In case of readability for example, we just
     show a notification but we don't provide actions to choose from
     * Delete = 0x01, // Delete some portion of the text (Can be a repeated
     word for example)
     * Ignore = 0x02, // Ignore the current instance of the error
     * IgnoreAll = 0x04, // Ignore all the instances of the error
     * IgnoreCritiqueType = 0x08, // Ignore a whole critique type
     * AddToDictionary = 0x10, // Add to dictionary
     * ShowDetails = 0x20, // Show a pane with details
    :type supported_actions: int
    :param explanation_title: The title of the explanation.
    :type explanation_title: str
    :param explanation_label: The label of the explanation (only support on
     specific critique types)
    :type explanation_label: str
    :param explanation: The explanation of the critique type.
    :type explanation: str
    :param is_document_level_critique: Indicates whether a critique applies to
     the whole document. It is used to inform user to flash all critiques from
     the same bucket if one changed. Default value: False .
    :type is_document_level_critique: bool
    :param suggestions:
    :type suggestions:
     list[~microsoft.swagger.codegen.editorservice.models.Suggestion]
    """

    _validation = {
        'trace_id': {'required': True},
        'type_id': {'required': True},
        'category_title': {'required': True},
        'start': {'required': True},
        'length': {'required': True},
        'priority': {'required': True},
        'suggestions': {'required': True},
    }

    _attribute_map = {
        'trace_id': {'key': 'TraceId', 'type': 'str'},
        'type_id': {'key': 'TypeId', 'type': 'str'},
        'category_title': {'key': 'CategoryTitle', 'type': 'str'},
        'start': {'key': 'Start', 'type': 'int'},
        'length': {'key': 'Length', 'type': 'int'},
        'priority': {'key': 'Priority', 'type': 'int'},
        'paragraph_id': {'key': 'ParagraphId', 'type': 'str'},
        'paragraph_revision_id': {'key': 'ParagraphRevisionId', 'type': 'str'},
        'tile_id': {'key': 'TileId', 'type': 'str'},
        'revision_id': {'key': 'RevisionId', 'type': 'str'},
        'supported_actions': {'key': 'SupportedActions', 'type': 'int'},
        'explanation_title': {'key': 'ExplanationTitle', 'type': 'str'},
        'explanation_label': {'key': 'ExplanationLabel', 'type': 'str'},
        'explanation': {'key': 'Explanation', 'type': 'str'},
        'is_document_level_critique': {'key': 'IsDocumentLevelCritique', 'type': 'bool'},
        'suggestions': {'key': 'Suggestions', 'type': '[Suggestion]'},
    }

    def __init__(self, trace_id, type_id, category_title, priority, suggestions, start=0, length=0, paragraph_id=None, paragraph_revision_id=None, tile_id=None, revision_id=None, supported_actions=None, explanation_title=None, explanation_label=None, explanation=None, is_document_level_critique=False):
        super(Critique, self).__init__()
        self.trace_id = trace_id
        self.type_id = type_id
        self.category_title = category_title
        self.start = start
        self.length = length
        self.priority = priority
        self.paragraph_id = paragraph_id
        self.paragraph_revision_id = paragraph_revision_id
        self.tile_id = tile_id
        self.revision_id = revision_id
        self.supported_actions = supported_actions
        self.explanation_title = explanation_title
        self.explanation_label = explanation_label
        self.explanation = explanation
        self.is_document_level_critique = is_document_level_critique
        self.suggestions = suggestions
