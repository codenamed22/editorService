# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommonOverriddenCritiqueTypeOptions(Model):
    """CommonOverriddenCritiqueTypeOptions.

    :param overridden_critique_type_options: List of critique types overrides
     from the default values.
    :type overridden_critique_type_options:
     list[~microsoft.swagger.codegen.editorservice.models.CritiqueTypeOption]
    """

    _attribute_map = {
        'overridden_critique_type_options': {'key': 'OverriddenCritiqueTypeOptions', 'type': '[CritiqueTypeOption]'},
    }

    def __init__(self, overridden_critique_type_options=None):
        super(CommonOverriddenCritiqueTypeOptions, self).__init__()
        self.overridden_critique_type_options = overridden_critique_type_options
