# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class TileElement(Model):
    """Content of a tile element.

    :param language_id: Editing language identifier with variants (e.g. en-us,
     en-gb, de-de-1996), see
     http://www.i18nguy.com/unicode/language-identifiers.html
    :type language_id: str
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
    :param text: Text to be checked.
    :type text: str
    :param is_clean: True if this tile element was not changed since the last
     call. In that case some analysis should not be performed. Default: false
    :type is_clean: bool
    :param analyzer_data: Dictionary that contains additional metadata about a
     tile element.
    :type analyzer_data: object
    :param spans: List of ranges in the tile element that define the language
     and other additional info
    :type spans:
     list[~microsoft.swagger.codegen.editorservice.models.TileCheckSpan]
    """

    _validation = {
        'language_id': {'required': True},
        'text': {'required': True},
    }

    _attribute_map = {
        'language_id': {'key': 'LanguageId', 'type': 'str'},
        'text_unit': {'key': 'TextUnit', 'type': 'str'},
        'text': {'key': 'Text', 'type': 'str'},
        'is_clean': {'key': 'IsClean', 'type': 'bool'},
        'analyzer_data': {'key': 'AnalyzerData', 'type': 'object'},
        'spans': {'key': 'Spans', 'type': '[TileCheckSpan]'},
    }

    def __init__(self, language_id, text, text_unit=None, is_clean=None, analyzer_data=None, spans=None):
        super(TileElement, self).__init__()
        self.language_id = language_id
        self.text_unit = text_unit
        self.text = text
        self.is_clean = is_clean
        self.analyzer_data = analyzer_data
        self.spans = spans
