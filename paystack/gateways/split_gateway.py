class TransactionSplit:

    """

    The Transaction Splits API enables merchants split the settlement for a transaction across their payout account,
    and one or more Subaccounts.

    """

    def __init__(self, gateway):
        self.gateway = gateway
        self.config = gateway.config

    def _post(self, url, params=None):
        if params is None:
            params = {}
        res = self.config.http().post(url, params)
        print(res)
        return res

    def _get(self, url, query_params=None):
        if query_params is None:
            query_params = {}

        res = self.config.http().get(url, params=query_params)
        print(res)
        return res

    def create(self, params):
        """
        Create a split payment on your integration
        :param params: 'name:"Name of the transaction split"' 'type: "The
        type of transaction split you want to create. You can use one of the following: percentage | flat"'
        'currency: "NGN, GHS, or USD"' 'subaccounts:"A list of object containing subaccount code and number of
        shares: [{subaccount_code: ‘ACT_xxxxxxxxxx’, share: xxx},{...}]"' 'bearer_type:"Any of subaccount | account |
        all"' 'bearer_subaccount:"Subaccount code"'
        :return: '{
                  "status": true,
                  "message": "Split created",
                  "data": {
                    "id": 142,
                    "name": "Test Doc",
                    "type": "percentage",
                    "currency": "NGN",
                    "integration": 428626,
                    "domain": "test",
                    "split_code": "SPL_e7jnRLtzla",
                    "active": true,
                    "bearer_type": "subaccount",
                    "bearer_subaccount": 40809,
                    "createdAt": "2020-06-30T11:42:29.150Z",
                    "updatedAt": "2020-06-30T11:42:29.150Z",
                    "subaccounts": [
                      {
                        "subaccount": {
                          "id": 40809,
                          "subaccount_code": "ACCT_z3x6z3nbo14xsil",
                          "business_name": "Business Name",
                          "description": "Business Description",
                          "primary_contact_name": null,
                          "primary_contact_email": null,
                          "primary_contact_phone": null,
                          "metadata": null,
                          "percentage_charge": 20,
                          "settlement_bank": "Business Bank",
                          "account_number": "1234567890"
                        },
                        "share": 20
                      },
                      {
                        "subaccount": {
                          "id": 40809,
                          "subaccount_code": "ACCT_pwwualwty4nhq9d",
                          "business_name": "Business Name",
                          "description": "Business Description",
                          "primary_contact_name": null,
                          "primary_contact_email": null,
                          "primary_contact_phone": null,
                          "metadata": null,
                          "percentage_charge": 20,
                          "settlement_bank": "Business Bank",
                          "account_number": "0123456789"
                        },
                        "share": 30
                      }
                    ],
                    "total_subaccounts": 2
                  }
                }
            '
        """
        return self._post("/split", params)

    def query(self, query_params=None):
        """
        List/search for the transaction splits available on your integration.
        :param query_params: name, active, sort_by, per_page, page, from, to
        :return: '
                {
                  "status": true,
                  "message": "Split retrieved",
                  "data": [
                    {
                      "id": 143,
                      "name": "Test Doc",
                      "split_code": "SPL_UO2vBzEqHW",
                      "integration": 428626,
                      "domain": "test",
                      "type": "percentage",
                      "active": 1,
                      "currency": "NGN",
                      "bearer_type": "subaccount",
                      "bearer_subaccount": 40809,
                      "created_at": "2020-06-30T11:52:24.000Z",
                      "updated_at": "2020-06-30T11:52:24.000Z",
                      "subaccounts": [
                        {
                          "subaccount": {
                            "id": 40809,
                            "subaccount_code": "ACCT_z3x6z3nbo14xsil",
                            "business_name": "Business Name",
                            "description": "Business Description",
                            "primary_contact_name": null,
                            "primary_contact_email": null,
                            "primary_contact_phone": null,
                            "metadata": null,
                            "percentage_charge": 80,
                            "settlement_bank": "Business Bank",
                            "account_number": "1234567890"
                          },
                          "share": 30
                        },
                        {
                          "subaccount": {
                            "id": 40811,
                            "subaccount_code": "ACCT_pwwualwty4nhq9d",
                            "business_name": "Business Name",
                            "description": "Business Description",
                            "primary_contact_name": null,
                            "primary_contact_email": null,
                            "primary_contact_phone": null,
                            "metadata": null,
                            "percentage_charge": 80,
                            "settlement_bank": "Business Bank",
                            "account_number": "0123456789"
                          },
                          "share": 20
                        }
                      ],
                      "total_subaccounts": 2
                    }
                  ],
                  "meta": {
                    "total": 1,
                    "skipped": 0,
                    "perPage": 50,
                    "page": 1,
                    "pageCount": 1
                  }
                }
        '
        """
        return self._get("/split", query_params)

    def fetch(self, split_id):
        """
        Get details of a split on your integration.
        :param split_id: split id
        :return: '
                {
                  "status": true,
                  "message": "Split retrieved",
                  "data": {
                    "id": 143,
                    "name": "Test Doc",
                    "split_code": "SPL_UO2vBzEqHW",
                    "integration": 428626,
                    "domain": "test",
                    "type": "percentage",
                    "active": 1,
                    "currency": "NGN",
                    "bearer_type": "subaccount",
                    "bearer_subaccount": 40809,
                    "created_at": "2020-06-30T11:52:24.000Z",
                    "updated_at": "2020-06-30T11:52:24.000Z",
                    "subaccounts": [
                      {
                        "subaccount": {
                          "id": 40809,
                          "subaccount_code": "ACCT_z3x6z3nbo14xsil",
                          "business_name": "Business Name",
                          "description": "Business Description",
                          "primary_contact_name": null,
                          "primary_contact_email": null,
                          "primary_contact_phone": null,
                          "metadata": null,
                          "percentage_charge": 80,
                          "settlement_bank": "Business Bank",
                          "account_number": "1234567890"
                        },
                        "share": 30
                      },
                      {
                        "subaccount": {
                          "id": 40811,
                          "subaccount_code": "ACCT_pwwualwty4nhq9d",
                          "business_name": "Business Name",
                          "description": "Business Description",
                          "primary_contact_name": null,
                          "primary_contact_email": null,
                          "primary_contact_phone": null,
                          "metadata": null,
                          "percentage_charge": 80,
                          "settlement_bank": "Business Bank",
                          "account_number": "0123456789"
                        },
                        "share": 20
                      }
                    ],
                    "total_subaccounts": 2
                  }
                }
        '
        """
        return self._get(f"/split/{split_id}")

    def update(self, split_id, params):
        """
        Update a transaction split details on your integration
        :param split_id: Split ID
        :param params: name, active -- check the documentation for optional parameters
        :return: '
            200 OK
            {
              "status": true,
              "message": "Split group updated",
              "data": {
                "id": 95,
                "name": "Updated Name",
                "type": "percentage",
                "currency": "NGN",
                "integration": 165956,
                "domain": "live",
                "split_code": "SPL_uMzcGbG5ca",
                "active": false,
                "bearer_type": "all",
                "bearer_subaccount": null,
                "createdAt": "2020-06-22T16:20:53.000Z",
                "updatedAt": "2020-06-22T17:26:59.000Z",
                "subaccounts": [
                  {
                    "subaccount": {
                      "id": 12700,
                      "subaccount_code": "ACCT_jsuq5uwf3n8la7b",
                      "business_name": "Ayobami GTB",
                      "description": "Ayobami GTB",
                      "primary_contact_name": null,
                      "primary_contact_email": null,
                      "primary_contact_phone": null,
                      "metadata": null,
                      "percentage_charge": 20,
                      "settlement_bank": "Guaranty Trust Bank",
                      "account_number": "0259198351"
                    },
                    "share": 80
                  }
                ],
                "total_subaccounts": 1
              }
            }
        '
        """
        return self._post(f"/split/{split_id}", params)