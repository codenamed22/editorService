# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class MetadataContent(Model):
    """Metadata values and types.

    :param metadata_type: Content metadata type. Possible values include:
     'IsResume'
    :type metadata_type: str or
     ~microsoft.swagger.codegen.editorservice.models.enum
    :param value: Metadata field value.
    :type value: str
    :param type_id: Id of the metadata type which generated the metadata.
    :type type_id: str
    """

    _attribute_map = {
        'metadata_type': {'key': 'MetadataType', 'type': 'str'},
        'value': {'key': 'Value', 'type': 'str'},
        'type_id': {'key': 'TypeId', 'type': 'str'},
    }

    def __init__(self, metadata_type=None, value=None, type_id=None):
        super(MetadataContent, self).__init__()
        self.metadata_type = metadata_type
        self.value = value
        self.type_id = type_id
