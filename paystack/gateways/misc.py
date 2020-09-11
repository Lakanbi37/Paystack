from paystack.gateways.gateway import BaseGateway


class Misc(BaseGateway):
    gateway_path = "/bank"

    def list_banks(self, query_params=None):
        return self.get(self.gateway_path, query_params)

    def providers(self):
        query = {"pay_with_bank_transfer": True}
        return self.get(self.gateway_path, query_params=query)