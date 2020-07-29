# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class Suggestion(Model):
    """Suggestion that is part of a critique.

    :param text: Suggestion string. If Action == None this field contains the
     message to show to the user if no suggestions are available.
    :type text: str
    :param description: Description text for the suggestion.
    :type description: str
    :param confidence_level: Suggestion confidence level:
     * High = 0
     * Medium = 1
     * Low = 2
     . Possible values include: 'High', 'Medium', 'Low'
    :type confidence_level: str or
     ~microsoft.swagger.codegen.editorservice.models.enum
    :param source: Suggestion source, mainly for telemetry: MainLex, UserLex,
     Cloud, serviceItCameFrom:
     * None = 0, // Suggestion source manually set by Editor for empty
     Suggestion
     * OfficeOrthospeller, // Suggestion from the Office orthospeller
     * BingOneSpeller, // Suggestion from OneSpeller
     * ContextSpeller, // Suggestion from the Office contextual speller
     * Grammar // Suggestion from the Grammar microservice
     . Possible values include: 'None', 'OfficeOrthospeller', 'BingOneSpeller',
     'ContextSpeller', 'Grammar'
    :type source: str or ~microsoft.swagger.codegen.editorservice.models.enum
    :param action: Action for the suggestion combined as flags:
     * None = 0x00 // No action for the suggestion: information (should be
     selectable by the user)
     * ChangeOnce = 0x01, // Change the error with the selected suggestion once
     * ChangeAll = 0x02, // Change all the instances of the error with the
     selected suggestion in the whole existing text
     * AutoCorrect = 0x04, // Automatically change the error to this suggestion
     * ReadAloud = 0x08, // Reads the suggestion to the user
    :type action: int
    :param bucket_id: Bucket id that can be used to group same suggestions
     inside one bucket of critiques. This field is used only for consistency
     critiques-suggestions. It can be a negative number.
    :type bucket_id: int
    :param number_of_instances: Number of instances of this suggestion that
     are already present in the doc as edited by the user. This field is used
     only for consistency critiques-suggestions.
    :type number_of_instances: int
    """

    _validation = {
        'text': {'required': True},
        'action': {'required': True},
    }

    _attribute_map = {
        'text': {'key': 'Text', 'type': 'str'},
        'description': {'key': 'Description', 'type': 'str'},
        'confidence_level': {'key': 'ConfidenceLevel', 'type': 'str'},
        'source': {'key': 'Source', 'type': 'str'},
        'action': {'key': 'Action', 'type': 'int'},
        'bucket_id': {'key': 'BucketId', 'type': 'int'},
        'number_of_instances': {'key': 'NumberOfInstances', 'type': 'int'},
    }

    def __init__(self, text, action, description=None, confidence_level=None, source=None, bucket_id=None, number_of_instances=None):
        super(Suggestion, self).__init__()
        self.text = text
        self.description = description
        self.confidence_level = confidence_level
        self.source = source
        self.action = action
        self.bucket_id = bucket_id
        self.number_of_instances = number_of_instances
