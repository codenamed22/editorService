# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import ServiceClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from msrest.pipeline import ClientRawResponse
from msrest.exceptions import HttpOperationError
from . import models


class EditorServiceConfiguration(Configuration):
    """Configuration for EditorService
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param x_correlation_id: Generated by the client and checked for validity.
     If non empty and valid, use as the telemetry log Correlation ID. Else,
     generate a new GUID (use this instead of the RequestId).
    :type x_correlation_id: str
    :param x_user_session_id: Generated by the client to track the user
     session Id.
    :type x_user_session_id: str
    :param x_user_id: Generated by the client to track the user Id.
    :type x_user_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, x_correlation_id=None, x_user_session_id=None, x_user_id=None, base_url=None):

        if not base_url:
            base_url = 'https://nleditor.osi.office.net/NLEditor'

        super(EditorServiceConfiguration, self).__init__(base_url)

        self.add_user_agent('editorservice/{}'.format(VERSION))

        self.x_correlation_id = x_correlation_id
        self.x_user_session_id = x_user_session_id
        self.x_user_id = x_user_id


class EditorService(object):
    """The Editor service leverages state of the art natural language components, such as spelling and grammar, to provide advanced proofing support through different REST APIs using the Azure infrastructure. You can find out more about editor service at [http://aka.ms/editorservice](http://aka.ms/editorservice).
    Explore this specification through a user-friendly UI [here](http://aka.ms/editorservice/swagger).
    ### Environments
     | Type       | Link                                 |
     |------------|--------------------------------------|
     | Int        | https://nleditor.osi.office-int.net/ |
     | EDog       | https://nleditor.osi.officeppe.net   |
     | Production | https://nleditor.osi.office.net      |

    :ivar config: Configuration for client.
    :vartype config: EditorServiceConfiguration

    :param x_correlation_id: Generated by the client and checked for validity.
     If non empty and valid, use as the telemetry log Correlation ID. Else,
     generate a new GUID (use this instead of the RequestId).
    :type x_correlation_id: str
    :param x_user_session_id: Generated by the client to track the user
     session Id.
    :type x_user_session_id: str
    :param x_user_id: Generated by the client to track the user Id.
    :type x_user_id: str
    :param str base_url: Service URL
    """

    def __init__(
            self, x_correlation_id=None, x_user_session_id=None, x_user_id=None, base_url=None):

        self.config = EditorServiceConfiguration(x_correlation_id, x_user_session_id, x_user_id, base_url)
        self._client = ServiceClient(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '1.0.0'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)


    def post_check(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Check text not previously tagged; can provide better suggestions
        (CloudSuggest).

        :param body: Check API request V1
        :type body:
         ~microsoft.swagger.codegen.editorservice.models.CheckRequestV1
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckResponseV1 or ClientRawResponse if raw=true
        :rtype:
         ~microsoft.swagger.codegen.editorservice.models.CheckResponseV1 or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.post_check.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.x_correlation_id is not None:
            header_parameters['X-CorrelationId'] = self._serialize.header("self.config.x_correlation_id", self.config.x_correlation_id, 'str')
        if self.config.x_user_session_id is not None:
            header_parameters['X-UserSessionId'] = self._serialize.header("self.config.x_user_session_id", self.config.x_user_session_id, 'str')
        if self.config.x_user_id is not None:
            header_parameters['X-UserId'] = self._serialize.header("self.config.x_user_id", self.config.x_user_id, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'CheckRequestV1')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('CheckResponseV1', response)
            header_dict = {
                'X-CorrelationId': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    post_check.metadata = {'url': '/Check/V1'}

    def get_check(
            self, app_id, text, language_id, app_version=None, descriptors0_name=None, descriptors0_value=None, descriptors1_name=None, descriptors1_value=None, language_ux_id=None, run_on_profile_id=None, length=None, start=None, request_id=None, text_unit=None, custom_headers=None, raw=False, **operation_config):
        """Check text not previously tagged; can provide better suggestions
        (CloudSuggest).

        Documented for the sake of completeness. Using the GET method is not
        recommended as it is very cumbersome to describe arrays of complex
        objects such as Descriptors or CliengSuggestions in the query string.
        .

        :param app_id: Id of the calling app, the supported ones are the
         following:
         * LinkedIn
         * NLServiceTestAutomation - Id used by automated tests
         * OAM - Id used by the probes
         * OneNote_Online, PowerPoint_Online, Word_Online - WAC
         * Testing_Client - Use for testing and prototyping
         . Possible values include: 'LinkedIn', 'NLServiceTestAutomation',
         'OAM', 'OneNote_Online', 'Testing_Client', 'PowerPoint_Online',
         'Word_Online'
        :type app_id: str
        :param text: Text to be checked.
        :type text: str
        :param language_id:
        :type language_id: str
        :param app_version: Version of the calling application.
        :type app_version: str
        :param descriptors0_name: Name of descriptor at index 0.
        :type descriptors0_name: str
        :param descriptors0_value: Value of descriptor at index 0.
        :type descriptors0_value: str
        :param descriptors1_name: Name of descriptor at index 1.
        :type descriptors1_name: str
        :param descriptors1_value: Value of descriptor at index 1.
        :type descriptors1_value: str
        :param language_ux_id: User current UX language ISO ID. Example: fr-fr
         for French (France) Default: the LanguageId (Not supported yet!)."
        :type language_ux_id: str
        :param run_on_profile_id: Profile ID assigned by NLX team. The default
         is the one selected for the specified AppID. Contact NLX team for more
         details.
        :type run_on_profile_id: str
        :param length: Length of the text to be checked. Default: The entire
         content of Text.
        :type length: int
        :param start: Init index for the text to be checked.
        :type start: int
        :param request_id: Unique call identifier generated by the caller.
         Deprecated - use X-CorrelationId instead.
        :type request_id: str
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
        :type text_unit: str
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: CheckResponseV1 or ClientRawResponse if raw=true
        :rtype:
         ~microsoft.swagger.codegen.editorservice.models.CheckResponseV1 or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.get_check.metadata['url']

        # Construct parameters
        query_parameters = {}
        query_parameters['AppId'] = self._serialize.query("app_id", app_id, 'str')
        query_parameters['Text'] = self._serialize.query("text", text, 'str')
        query_parameters['LanguageId'] = self._serialize.query("language_id", language_id, 'str')
        if app_version is not None:
            query_parameters['AppVersion'] = self._serialize.query("app_version", app_version, 'str')
        if descriptors0_name is not None:
            query_parameters['Descriptors[0].Name'] = self._serialize.query("descriptors0_name", descriptors0_name, 'str')
        if descriptors0_value is not None:
            query_parameters['Descriptors[0].Value'] = self._serialize.query("descriptors0_value", descriptors0_value, 'str')
        if descriptors1_name is not None:
            query_parameters['Descriptors[1].Name'] = self._serialize.query("descriptors1_name", descriptors1_name, 'str')
        if descriptors1_value is not None:
            query_parameters['Descriptors[1].Value'] = self._serialize.query("descriptors1_value", descriptors1_value, 'str')
        if language_ux_id is not None:
            query_parameters['LanguageUXId'] = self._serialize.query("language_ux_id", language_ux_id, 'str')
        if run_on_profile_id is not None:
            query_parameters['RunOnProfileId'] = self._serialize.query("run_on_profile_id", run_on_profile_id, 'str')
        if length is not None:
            query_parameters['Length'] = self._serialize.query("length", length, 'int')
        if start is not None:
            query_parameters['Start'] = self._serialize.query("start", start, 'int')
        if request_id is not None:
            query_parameters['RequestId'] = self._serialize.query("request_id", request_id, 'str')
        if text_unit is not None:
            query_parameters['TextUnit'] = self._serialize.query("text_unit", text_unit, 'str')

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.x_correlation_id is not None:
            header_parameters['X-CorrelationId'] = self._serialize.header("self.config.x_correlation_id", self.config.x_correlation_id, 'str')
        if self.config.x_user_session_id is not None:
            header_parameters['X-UserSessionId'] = self._serialize.header("self.config.x_user_session_id", self.config.x_user_session_id, 'str')
        if self.config.x_user_id is not None:
            header_parameters['X-UserId'] = self._serialize.header("self.config.x_user_id", self.config.x_user_id, 'str')

        # Construct and send request
        request = self._client.get(url, query_parameters)
        response = self._client.send(request, header_parameters, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('CheckResponseV1', response)
            header_dict = {
                'X-CorrelationId': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    get_check.metadata = {'url': '/Check/V1'}

    def post_tile_check(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Checks a part of document represented as list of tiles.

        "Can provide additional analyses on higher than paragraph level in
        comparison with Check api; In the same way as check api it can provide
        better suggestions (CloudSuggest)"
        .

        :param body: TileCheck API request V1
        :type body:
         ~microsoft.swagger.codegen.editorservice.models.TileCheckRequestV1
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: TileCheckResponseV1 or ClientRawResponse if raw=true
        :rtype:
         ~microsoft.swagger.codegen.editorservice.models.TileCheckResponseV1 or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.post_tile_check.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.x_correlation_id is not None:
            header_parameters['X-CorrelationId'] = self._serialize.header("self.config.x_correlation_id", self.config.x_correlation_id, 'str')
        if self.config.x_user_session_id is not None:
            header_parameters['X-UserSessionId'] = self._serialize.header("self.config.x_user_session_id", self.config.x_user_session_id, 'str')
        if self.config.x_user_id is not None:
            header_parameters['X-UserId'] = self._serialize.header("self.config.x_user_id", self.config.x_user_id, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'TileCheckRequestV1')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('TileCheckResponseV1', response)
            header_dict = {
                'X-CorrelationId': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    post_tile_check.metadata = {'url': '/TileCheck/V1'}

    def config_v1(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Fetch all the available profiles and critique categories and types for
        a particular language.

        This API is designed to fetch all the available profiles and critique
        categories types for a particular language and some factors defined in
        the Descriptors (i.e. haveSubscriptionLicense, audience).
        * The Config API only supports fetching the information for only one
        language at a time. If it is required to pre-fetch critique type
        information for multiple languages, it is recommended to send multiple
        calls in parallel.
        * All Available critique type values are inherited from Win32
        Grammar&More writing styles. Please contact us to modify the default
        behaviors.
        ### Scenarios
        * Whenever the client wants to draw the proofing option dialog with a
        drop down menu with the supported profiles, where the customer can turn
        on/off critique types, the Config API would be called to fetch all the
        required info to draw the dialog.
        * Once the customer changes the proofing language from one to another,
        another Config API would be required for the new language, if it is not
        pre-fetched and cached.
        .

        :param body: Config API request V1
        :type body:
         ~microsoft.swagger.codegen.editorservice.models.ConfigRequestV1
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ConfigResponseV1 or ClientRawResponse if raw=true
        :rtype:
         ~microsoft.swagger.codegen.editorservice.models.ConfigResponseV1 or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.config_v1.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.x_correlation_id is not None:
            header_parameters['X-CorrelationId'] = self._serialize.header("self.config.x_correlation_id", self.config.x_correlation_id, 'str')
        if self.config.x_user_session_id is not None:
            header_parameters['X-UserSessionId'] = self._serialize.header("self.config.x_user_session_id", self.config.x_user_session_id, 'str')
        if self.config.x_user_id is not None:
            header_parameters['X-UserId'] = self._serialize.header("self.config.x_user_id", self.config.x_user_id, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'ConfigRequestV1')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('ConfigResponseV1', response)
            header_dict = {
                'X-CorrelationId': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    config_v1.metadata = {'url': '/Config/V1'}

    def config_v2(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Fetch all the available critique types for a particular language and
        Profile ID.

        This API is designed to fetch all the available critique types for a
        particular language and Profile ID and some factors defined in the
        Descriptors (i.e. haveSubscriptionLicense, audience).
        * The Config API only supports fetching the information for only one
        language at a time. If it is required to pre-fetch critique type
        information for multiple languages, it is recommended to send multiple
        calls in parallel.
        * All Available critique type values are inherited from Win32
        Grammar&More writing styles. Please contact us to modify the default
        behaviors.
        ### Scenarios
        * Whenever the client wants to draw the proofing option dialog, where
        the customer can turn on/off critique types, the Config API would be
        called to fetch all the required info to draw the dialog.
        * Once the customer changes the proofing language from one to another,
        another Config API would be required for the new language, if it is not
        pre-fetched and cached.
        .

        :param body: Config API request V2
        :type body:
         ~microsoft.swagger.codegen.editorservice.models.ConfigRequestV2
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: ConfigResponseV2 or ClientRawResponse if raw=true
        :rtype:
         ~microsoft.swagger.codegen.editorservice.models.ConfigResponseV2 or
         ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.config_v2.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.x_correlation_id is not None:
            header_parameters['X-CorrelationId'] = self._serialize.header("self.config.x_correlation_id", self.config.x_correlation_id, 'str')
        if self.config.x_user_session_id is not None:
            header_parameters['X-UserSessionId'] = self._serialize.header("self.config.x_user_session_id", self.config.x_user_session_id, 'str')
        if self.config.x_user_id is not None:
            header_parameters['X-UserId'] = self._serialize.header("self.config.x_user_id", self.config.x_user_id, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'ConfigRequestV2')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('ConfigResponseV2', response)
            header_dict = {
                'X-CorrelationId': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    config_v2.metadata = {'url': '/Config/V2'}

    def languageinfo(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Load the language support for the client given the UX language.

        Load the language support for the client given the UX language. This
        API will pass all the info on the language list including the localized
        strings to render in the UI Example:
        * French (France) - Post reform
        * French (France) - Pre reform
        * French (France) - Both reforms
        ### Scenarios
        When initialized/launched, the app makes a service call requesting the
        list of available language for the current UX language ID, the selected
        editing language (if only one language is required). Service replies
        with the info on the supported languages or on the specific language.
        .

        :param body: Language Info API request V1
        :type body:
         ~microsoft.swagger.codegen.editorservice.models.LanguageInfoRequestV1
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: LanguageInfoResponseV1 or ClientRawResponse if raw=true
        :rtype:
         ~microsoft.swagger.codegen.editorservice.models.LanguageInfoResponseV1
         or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.languageinfo.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.x_correlation_id is not None:
            header_parameters['X-CorrelationId'] = self._serialize.header("self.config.x_correlation_id", self.config.x_correlation_id, 'str')
        if self.config.x_user_session_id is not None:
            header_parameters['X-UserSessionId'] = self._serialize.header("self.config.x_user_session_id", self.config.x_user_session_id, 'str')
        if self.config.x_user_id is not None:
            header_parameters['X-UserId'] = self._serialize.header("self.config.x_user_id", self.config.x_user_id, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'LanguageInfoRequestV1')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        deserialized = None
        header_dict = {}

        if response.status_code == 200:
            deserialized = self._deserialize('LanguageInfoResponseV1', response)
            header_dict = {
                'X-CorrelationId': 'str',
            }

        if raw:
            client_raw_response = ClientRawResponse(deserialized, response)
            client_raw_response.add_headers(header_dict)
            return client_raw_response

        return deserialized
    languageinfo.metadata = {'url': '/LanguageInfo/V1'}

    def instrumentation(
            self, body, custom_headers=None, raw=False, **operation_config):
        """Report the user action on a critique.

        ### Scenarios
        * User ignores the critique
        * User accepts the critique suggestion
        .

        :param body: Instrumentation API request V1
        :type body:
         ~microsoft.swagger.codegen.editorservice.models.InstrumentationRequestV1
        :param dict custom_headers: headers that will be added to the request
        :param bool raw: returns the direct response alongside the
         deserialized response
        :param operation_config: :ref:`Operation configuration
         overrides<msrest:optionsforoperations>`.
        :return: None or ClientRawResponse if raw=true
        :rtype: None or ~msrest.pipeline.ClientRawResponse
        :raises:
         :class:`HttpOperationError<msrest.exceptions.HttpOperationError>`
        """
        # Construct URL
        url = self.instrumentation.metadata['url']

        # Construct parameters
        query_parameters = {}

        # Construct headers
        header_parameters = {}
        header_parameters['Content-Type'] = 'application/json; charset=utf-8'
        if custom_headers:
            header_parameters.update(custom_headers)
        if self.config.x_correlation_id is not None:
            header_parameters['X-CorrelationId'] = self._serialize.header("self.config.x_correlation_id", self.config.x_correlation_id, 'str')
        if self.config.x_user_session_id is not None:
            header_parameters['X-UserSessionId'] = self._serialize.header("self.config.x_user_session_id", self.config.x_user_session_id, 'str')
        if self.config.x_user_id is not None:
            header_parameters['X-UserId'] = self._serialize.header("self.config.x_user_id", self.config.x_user_id, 'str')

        # Construct body
        body_content = self._serialize.body(body, 'InstrumentationRequestV1')

        # Construct and send request
        request = self._client.post(url, query_parameters)
        response = self._client.send(
            request, header_parameters, body_content, stream=False, **operation_config)

        if response.status_code not in [200, 400, 500]:
            raise HttpOperationError(self._deserialize, response)

        if raw:
            client_raw_response = ClientRawResponse(None, response)
            client_raw_response.add_headers({
                'X-CorrelationId': 'str',
            })
            return client_raw_response
    instrumentation.metadata = {'url': '/Instrumentation/V1'}
