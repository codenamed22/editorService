# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class File(Model):
    """File metadata where the acronym was originally found.

    :param id: Object id.
    :type id: str
    :param name: File name.
    :type name: str
    :param extension: File extension.
    :type extension: str
    :param uri: Absolute URI to the file.
    :type uri: str
    :param instrumentation_id: Instrumentation id of this entity.
    :type instrumentation_id: str
    :param snippet: Snippet
    :type snippet: str
    """

    _attribute_map = {
        'id': {'key': 'Id', 'type': 'str'},
        'name': {'key': 'Name', 'type': 'str'},
        'extension': {'key': 'Extension', 'type': 'str'},
        'uri': {'key': 'Uri', 'type': 'str'},
        'instrumentation_id': {'key': 'InstrumentationId', 'type': 'str'},
        'snippet': {'key': 'Snippet', 'type': 'str'},
    }

    def __init__(self, id=None, name=None, extension=None, uri=None, instrumentation_id=None, snippet=None):
        super(File, self).__init__()
        self.id = id
        self.name = name
        self.extension = extension
        self.uri = uri
        self.instrumentation_id = instrumentation_id
        self.snippet = snippet