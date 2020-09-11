from paystack.exceptions.invalid_parameter import InvalidParameters
from paystack.gateways.gateway import BaseGateway


class Subaccount(BaseGateway):
    """
    The Subaccounts API allows you create and manage subaccounts on your integration. Subaccounts can be used to
    split payment between two accounts (your main account and a sub account)
    """

    gateway_path = "/subaccount"

    def create(self, params):
        """
        Create a subacount on your integration
        :param params: business_name (required) - Name of business for subaccount settlement_bank (required) - Name
        of Bank (see list of accepted names by calling List Banks account_number (required) - NUBAN Bank Account
        Number percentage_charge (required) - What is the default percentage charged when receiving on behalf of this
        subaccount? primary_contact_email - A contact email for the subaccount primary_contact_name - A name for the
        contact person for this subaccount primary_contact_phone - A phone number to call for this subaccount
        metadata - Stringified JSON object settlement_schedule - Any of auto, weekly, monthly, manual. Auto means
        payout is T+1 and manual means payout to the subaccount should only be made when requested.
        :return:
        """
        payload = dict(**params)
        if "business_name" not in payload:
            raise InvalidParameters("Business name required")
        if "settlement_bank" not in payload:
            raise InvalidParameters("Settlement bank needs to be provided")
        if "account_number" not in payload:
            raise InvalidParameters("Account number required")
        if "percentage_charge" not in payload:
            raise InvalidParameters("Percentage charge must be fixed")
        return self.post(self.gateway_path, payload)

    def list(self, query_params=None):
        """
        List subaccounts available on your integration.
        :param query_params: perPage - Specify how many records you want to retrieve per page page - Specify exactly
        what page you want to retrieve - from A timestamp from which to start listing subaccounts e.g.
        2016-09-24T00:00:05.000Z, 2016-09-21 - to A timestamp at which to stop listing subaccounts e.g.
        2016-09-24T00:00:05.000Z, 2016-09-21
        :return:
        """
        return self.get(self.gateway_path, query_params)

    def retrieve(self, id_or_code):
        """
        Get details of a subaccount on your integration.
        :param id_or_code: Subaccount id or code
        :return:
        """
        return self.get(f"{self.gateway_path}/{id_or_code}")

    def update(self, id_or_code, params):
        """
        Update a subaccount details on your integration
        :param id_or_code: Subaccount id or code
        :param params: params for create method (update fields based on your needs)
        :return:
        """
        return self.put(f"{self.gateway_path}/{id_or_code}", params)
