from paystack.exceptions.invalid_parameter import InvalidParameters
from paystack.gateways.gateway import BaseGateway


class Customer(BaseGateway):
    """
    The Customers API allows you create and manage customers on your integration.
    """

    def create(self, params):
        """
        Creates a customer
        :param params: name, first_name, last_name, phone, meta_data
        :return: response
        """
        return self.post("/customer", params)

    def list(self, query_params=None):
        """
        Returns the list of customers on your account
        :param query_params:
        :return:
        """
        return self.get("/customer", query_params)

    def fetch(self, email_or_code):
        """
        Get details of a customer on your integration.
        :param email_or_code: An email or customer code for the customer you want to fetch
        :return:
        """
        return self.get(f"/customer/{email_or_code}")

    def update(self, code, params):
        """
        Update a customer's details on your integration
        :param code: Customer's code
        :param params: first_name, last_name, phone, metadata
        :return:
        """
        return self.put(f"/customer/{code}", params)

    def set_risk_action(self, params):
        """
        Whitelist or blacklist a customer on your integration
        :param params: customer, risk_action - One of the possible risk actions [ default, allow, deny ]. allow to
        whitelist. deny to blacklist. Customers start with a default risk action.
        :return:
        """
        return self.post("/customer/set_risk_action", params)

    def deactivate_card(self, params):
        """
        Deactivate an authorization when the card needs to be forgotten
        :params: authorization_code - customer authorization code
        :return:
        """
        payload = dict(**params)
        if "authorization_code" not in payload:
            raise InvalidParameters("Customer authorization code is required")
        return self.post("/customer/deactivate_authorization", params)
