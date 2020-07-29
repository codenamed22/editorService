# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CritiqueCategoryInfo(Model):
    """Critique type information of a particular critique category.

    :param id: CritiqueCategoryInfo ID (Guids for Grammar or styles, Speller,
     CSS).
    :type id: str
    :param name: Display name for a particular CritiqueCategoryInfo: Grammar,
     Clarity and Conciseness, Speller, CSS, etc.
    :type name: str
    :param critique_type_info_list: List of critique types.
    :type critique_type_info_list:
     list[~microsoft.swagger.codegen.editorservice.models.CritiqueTypeInfo]
    """

    _validation = {
        'id': {'required': True},
        'name': {'required': True},
    }

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
        'critique_type_info_list': {'key': 'CritiqueTypeInfoList', 'type': '[CritiqueTypeInfo]'},
    }

    def __init__(self, id, name, critique_type_info_list=None):
        super(CritiqueCategoryInfo, self).__init__()
        self.id = id
        self.name = name
        self.critique_type_info_list = critique_type_info_list
