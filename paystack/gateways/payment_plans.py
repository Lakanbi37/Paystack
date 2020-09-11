from paystack.gateways.gateway import BaseGateway


class Plans(BaseGateway):
    gateway_path = "/plan"
    """
    The Plans API allows you create and manage installment payment options on your integration
    """

    def create(self, params):
        """
        Create a plan on your integration
        :param params: name (required) - Name of plan description - Short description of plan amount (required) -
        Amount to be charged in kobo interval (required) - Interval in words. Valid intervals are hourly, daily,
        weekly, monthly, annually. send_invoices - Set to false if you don't want invoices to be sent to your
        customers currency - Currency in which amount is set invoice_limit - Number of invoices to raise during
        subscription to this plan. Can be overridden by specifying an invoice_limit while subscribing.
        :return:
        """
        return self.post(self.gateway_path, params)

    def list(self, query_params=None):
        """
        List plans available on your integration.
        :param query_params: query params for filtering of results
        :return:
        """
        return self.get(self.gateway_path, query_params)

    def retrieve(self, id_or_code):
        """
        Get details of a plan on your integration.
        :param id_or_code: Plan ID or Code
        :return:
        """
        return self.get(f"{self.gateway_path}/{id_or_code}")

    def update(self, id_or_code, params):
        """
        Update a plan details on your integration
        :param id_or_code: Plan ID or Code
        :param params: same as with Plans.create(**params) method - update fields based on your needs
        :return:
        """
        return self.put(f"{self.gateway_path}/{id_or_code}", params)
