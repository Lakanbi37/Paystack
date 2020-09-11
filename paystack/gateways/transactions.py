from exceptions.invalid_parameter import InvalidParameters
from paystack.gateways.gateway import BaseGateway


class TransactionGateway(BaseGateway):
    gateway_path = "/transaction"

    def initiate(self, params):
        payload = dict(**params)
        if "amount" not in payload:
            raise InvalidParameters("Amount to be charged needs to be specified")
        if "email" not in payload:
            raise InvalidParameters("Customer email is required")
        if "channels" in payload and not isinstance(payload["channels"], list):
            raise InvalidParameters("Channels field needs to be an Array of strings")
        return self.post(f"{self.gateway_path}/initialize", params)

    def verify(self, reference):
        response = self.get(f"{self.gateway_path}/verify/{reference}")
        return response

    def list(self, query_params=None):
        return self.get(self.gateway_path, query_params)

    def retrieve(self, txn_id):
        response = self.get(f"{self.gateway_path}/{txn_id}")
        return response

    def authorize(self, params):
        """
        All authorizations marked as reusable can be charged with this endpoint whenever you need to recieve payments.
        :param params:
        :return:
        """
        payload = dict(**params)
        if "authorization_code" not in payload:
            raise InvalidParameters("Customer authorization code is required")
        if "email" not in payload:
            raise InvalidParameters("Customer email is required")
        if "amount" not in payload:
            raise InvalidParameters("Amount to be charged is required")
        response = self.post(f"{self.gateway_path}/charge_authorization", payload)
        return response

    def check_authorization(self, params):
        """
        All mastercard and visa authorizations can be checked with this endpoint to know if they have funds for the payment you seek.

        This endpoint should be used when you do not know the exact amount to charge a card when rendering a service. It should be used to check if a card has enough funds based on a maximum range value. It is well suited for:

        Ride hailing services
        Logistics services
        :param params: amount<required>, email<required>, authorization_code<required>, currency<optional>
        :return:
        You shouldn't use this endpoint to check a card for sufficient funds if you are going to charge the user immediately. This is because we hold funds when this endpoint is called which can lead to an insufficient funds error.
        """
        response = self.post(f"{self.gateway_path}/check_authorization", params)
        return response

    def get_transaction_history(self, txn_id_or_ref):
        """
        View the timeline of a transaction
        :param txn_id_or_ref: Transaction id or reference
        :return:
        """
        response = self.get(f"{self.gateway_path}/timeline/{txn_id_or_ref}")
        return response

    def get_transaction_totals(self, params=None):
        """
        Returns total amount received on your account
        :param params:
        """
        return self.get(f"{self.gateway_path}/totals", params)

    def export_transactions(self, query_params=None):
        """
        Generates a report of all transactions carried out on your account :param query_params: Url query params to
        filter by, Check the documentation for more details on the available url parameters
        """
        return self.get(f"{self.gateway_path}/export", query_params)

    def partial_charge(self, params):
        """
        Retrieve part of a payment from a customer
        :param params: '{ authorization: "AUTH_72btv547", currency: "NGN", amount: "20000" }'
        """
        return self.post(f"{self.gateway_path}/partial_debit", params)
