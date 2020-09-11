from paystack.gateways.gateway import BaseGateway


class Settlements(BaseGateway):
    gateway_path = "/settlement"

    def load(self, query_params=None):
        """
        :param query_params: from - Lower bound of date range. Leave undefined to export settlement from day one. to
        - Upper bound of date range. Leave undefined to export settlements till date. subaccount - Provide a
        subaccount code to export only settlements for that subaccount. Set to none to export only transactions for
        the account
        """
        return self.get(self.gateway_path, query_params)

    def fetch_for_transactions(self, sid, query_params=None):
        """
        :param sid: settlement ID.\n
       :param query_params: from - Lower bound of date range. Leave undefined to export settlement from day one. to
       - Upper bound of date range. Leave undefined to export settlements till date. subaccount - Provide a
       subaccount code to export only settlements for that subaccount. Set to none to export only transactions for
       the account
       """
        return self.get(f"{self.gateway_path}/{sid}/transactions", query_params)
