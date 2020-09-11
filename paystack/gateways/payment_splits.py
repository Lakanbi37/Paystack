from paystack.gateways.gateway import BaseGateway


class TransactionSplit(BaseGateway):
    gateway_path = "/split"
    """

    The Transaction Splits API enables merchants split the settlement for a transaction across their payout account,
    and one or more Subaccounts.

    """

    def create(self, params):
        """
        Create a split payment on your integration
        :param params: 'name:"Name of the transaction split"' 'type: "The
        type of transaction split you want to create. You can use one of the following: percentage | flat"'
        'currency: "NGN, GHS, or USD"' 'subaccounts:"A list of object containing subaccount code and number of
        shares: [{subaccount_code: ‘ACT_xxxxxxxxxx’, share: xxx},{...}]"' 'bearer_type:"Any of subaccount | account |
        all"' 'bearer_subaccount:"Subaccount code"'
        """
        return self.post(self.gateway_path, params)

    def query(self, query_params=None):
        """
        List/search for the transaction splits available on your integration.
        :param query_params: name, active, sort_by, per_page, page, from, to
        """
        return self.get(self.gateway_path, query_params)

    def fetch(self, split_id):
        """
        Get details of a split on your integration.
        :param split_id: split id
        """
        return self.get(f"{self.gateway_path}/{split_id}")

    def update(self, split_id, params):
        """
        Update a transaction split details on your integration
        :param split_id: Split ID
        :param params: name, active -- check the documentation for optional parameters
        """
        return self.put(f"{self.gateway_path}/{split_id}", params)
