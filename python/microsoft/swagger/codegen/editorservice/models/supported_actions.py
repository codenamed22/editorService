# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class SupportedActions(Model):
    """SupportedActions.

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
    """

    _attribute_map = {
        'supported_actions': {'key': 'SupportedActions', 'type': 'int'},
    }

    def __init__(self, supported_actions=None):
        super(SupportedActions, self).__init__()
        self.supported_actions = supported_actions