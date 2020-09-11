from paystack.exceptions.invalid_parameter import InvalidParameters
from paystack.gateways.gateway import BaseGateway


class Refunds(BaseGateway):
    gateway_path = "/refund"

    """A Refund is an object created on a disputed transaction requesting for a refund. Credit/Debit card originally 
    charged will be refunded """

    def refund(self, params):
        """
        This creates a refund which is then processed by the Paystack team.\n
        :param params: transaction (required): Identifier for transaction to be refunded amount (optional): How much
        in kobo to be refunded to the customer. Amount is optional(defaults to original transaction amount) and
        cannot be more than the original transaction amount. currency: Three-letter ISO currency customer_note (
        optional): customer reason merchant_note (optional): merchant reason.\n
        """
        payload = dict(**params)
        if "transaction" not in payload:
            raise InvalidParameters("Transaction ID must be included")
        return self.post(self.gateway_path, payload)

    def list(self, query_params=None):
        """
        :param query_params: transaction, currency
        :return:
        """
        return self.get(self.gateway_path, query_params)

    def fetch(self, refund_id):
        """
        :param refund_id: Identifier of the refund object
        :return:
        """
        return self.get(self.gateway_path+"/"+refund_id)
