# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class CommonAppVersionProperty(Model):
    """CommonAppVersionProperty.

    :param app_version: Version of the calling application.
    :type app_version: str
    """

    _attribute_map = {
        'app_version': {'key': 'AppVersion', 'type': 'str'},
    }

    def __init__(self, app_version=None):
        super(CommonAppVersionProperty, self).__init__()
        self.app_version = app_version
