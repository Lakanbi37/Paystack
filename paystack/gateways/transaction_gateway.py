class TransactionGateway:

    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def _post(self, url, params=None):
        if params is None:
            params = {}
        response = self.config.http().post(url, params)
        print(response)
        return response

    def _get(self, url, params=None):
        if params is None:
            params = {}
        response = self.config.http().get(url, params)
        print(response)
        return response

    def initiate(self, params):
        return self._post("/transaction/initialize", params)

    def verify(self, reference):
        response = self._get(f"/transaction/verify/{reference}")
        return response

    def list(self, params=None):
        response = self._get("/transaction", params)
        return response

    def retrieve(self, txn_id):
        response = self._get(f"/transaction/{txn_id}")
        return response

    def authorize(self, params):
        """
        All authorizations marked as reusable can be charged with this endpoint whenever you need to recieve payments.
        :param params:
        :return:
        """
        response = self._post("/transaction/charge_authorization", params)
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
        response = self._post("/transaction/check_authorization", params)
        return response

    def get_transaction_history(self, txn_id_or_ref):
        """
        View the timeline of a transaction
        :param txn_id_or_ref: Transaction id or reference
        :return:
        """
        response = self._get(f"/transaction/timeline/{txn_id_or_ref}")
        return response

    def get_transaction_totals(self, params=None):
        """
        Returns total amount received on your account
        :param params:
        :return: {
              "status": true,
              "message": "Transaction totals",
              "data": {
                "total_transactions": 10,
                "unique_customers": 3,
                "total_volume": 14000,
                "total_volume_by_currency": [
                  {
                    "currency": "NGN",
                    "amount": 14000
                  }
                ],
                "pending_transfers": 24000,
                "pending_transfers_by_currency": [
                  {
                    "currency": "NGN",
                    "amount": 24000
                  }
                ]
              }
            }
        """
        return self._get("/transaction/totals", params)

    def export_transactions(self, params=None):
        """
        Generates a report of all transactions carried out on your account
        :param params: Url query params to filter by, Check the documentation for more details on the available url parameters
        :return: {
              "status": true,
              "message": "Export successful",
              "data": {
                "path": "https://files.paystack.co/exports/100032/1460290758207.csv"
              }
            }
        """
        return self._get("/transaction/export", params)

    def partial_charge(self, params):
        """
        Retrieve part of a payment from a customer
        :param params: '{ authorization: "AUTH_72btv547", currency: "NGN", amount: "20000" }'
        :return: '
                {
                  "status": true,
                  "message": "Charge attempted",
                  "data": {
                    "amount": 2000,
                    "currency": "NGN",
                    "transaction_date": "2020-01-23T14:39:37.000Z",
                    "status": "success",
                    "reference": "REF_0000000001",
                    "domain": "test",
                    "metadata": "",
                    "gateway_response": "Approved",
                    "message": null,
                    "channel": "card",
                    "ip_address": null,
                    "log": null,
                    "fees": 30,
                    "authorization": {
                      "authorization_code": "AUTH_4edwayn8k4",
                      "bin": "408408",
                      "last4": "0409",
                      "exp_month": "12",
                      "exp_year": "2020",
                      "channel": "card",
                      "card_type": "visa DEBIT",
                      "bank": "Test Bank",
                      "country_code": "NG",
                      "brand": "visa",
                      "reusable": true,
                      "signature": "SIG_GfJIf2Dg1N1BwN5ddXmh"
                    },
                    "customer": {
                      "id": 16702,
                      "first_name": "",
                      "last_name": "",
                      "email": "testuser@paystack.com",
                      "customer_code": "CUS_096t7vsogztygg4",
                      "phone": "",
                      "metadata": null,
                      "risk_action": "default"
                    },
                    "plan": 0,
                    "amount": 2000
                  }
                }
            '
        """
        return self._post("/transaction/partial_debit", params)
