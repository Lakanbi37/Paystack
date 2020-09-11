from exceptions.invalid_parameter import InvalidParameters
from paystack.gateways.gateway import BaseGateway


class Subscriptions(BaseGateway):
    gateway_path = "/subscription"

    """
    The Subscriptions API allows you create and manage recurring payment on your integration
    """

    def create(self, params):
        """
        Create a subscription on your integration \n
        :param params: customer (required) - Customer's email address or customer code
        plan (required) - Plan code
        authorization - If customer has multiple authorizations, you can set the desired authorization you wish to use for this subscription here. If this is not supplied, the customer's most recent authorization would be used
        start_date - Set the date for the first debit. (ISO 8601 format) \n
        Note the email_token attribute for the subscription object. We create one on each subscription so customers can
        cancel their subscriptions from within the invoices sent to their mailboxes. Since they are not authorized,
        the email tokens are what we use to authenticate the requests over the API.
        :return:
        """
        payload = dict(**params)
        if "customer" not in payload:
            raise InvalidParameters("Customer required")
        if "plan" not in payload:
            raise InvalidParameters("Plan required")
        return self.post(self.gateway_path, payload)

    def activate(self, params):
        """
        Enable a subscription on your integration \n
        :param params: code (required) - Subscription code
        token (required) - Email token

        :return:
        """
        payload = dict(**params)
        if "code" not in payload:
            raise InvalidParameters("Subscription code required")
        if "token" not in payload:
            raise InvalidParameters("Token required")
        return self.post(self.gateway_path + "/enable", payload)

    def deactivate(self, params):
        """
        Enable a subscription on your integration \n
        :param params: code (required) - Subscription code
        token (required) - Email token
        :return:
        """
        if "code" not in params:
            raise InvalidParameters("Subscription code required")
        if "token" not in params:
            raise InvalidParameters("Email token required")
        return self.post(self.gateway_path + "/disable", params)

    def list(self, query_params=None):
        """
        Disable a subscription on your integration \n
        :param query_params: perPage - Specify how many records you want to retrieve per page
        page - Specify exactly what page you want to retrieve
        customer - Filter by Customer ID
        plan - Filter by Plan ID
        :return:
        """
        return self.get(self.gateway_path, query_params)

    def retrieve(self, id_or_code):
        """
        Get details of a subscription on your integration. \n
        :param id_or_code: The subscription ID or code you want to fetch
        :return:
        """
        return self.get(f"{self.gateway_path}/{id_or_code}")
