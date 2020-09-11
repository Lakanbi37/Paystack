from paystack.gateways.gateway import BaseGateway
from paystack.exceptions.invalid_parameter import InvalidParameters


class Transfers(BaseGateway):
    gateway_path = "/transfer"
    recipient_path = "/transferrecipient"

    def add_beneficiary(self, params):
        """
        Creates a new recipient. A duplicate account number will lead to the retrieval of the existing record.\n
        :param params:  type (required) - Recipient Type (Only nuban at this time)
        name (required) - A name for the recipient
        metadata - Store additional information about your recipient in a structured format. JSON
        bank_code (required) - Required if type is nuban. You can find a list of bank codes at api.paystack.co/bank
        account_number (required) - Required if type is nuban
        currency - Currency for the account receiving the transfer.
        description
        """
        payload = dict(**params)
        if "type" not in payload:
            payload["type"] = "nuban"
        if "name" not in payload:
            raise InvalidParameters("Please specify the account name")
        if "account_number" not in payload:
            raise InvalidParameters("Please specify the account number")
        if "bank_code" not in payload:
            raise InvalidParameters("Bank code is required")
        return self.post(self.recipient_path, payload)

    def list_beneficiaries(self, query_params=None):
        return self.get(self.recipient_path, query_params)

    def update_beneficiary(self, code_or_id, params):
        payload = dict(**params)
        return self.put(f"{self.recipient_path}/{code_or_id}", payload)

    def remove_beneficiary(self, code_or_id):
        return self.delete(f"{self.recipient_path}/{code_or_id}")

    def initiate(self, params):
        """
        Status of transfer object returned will be ‘pending’ if OTP is disabled. In the event that an OTP is
        required, status will read ‘otp’.\n
        :param params: source (required) - Where should we transfer from? Only
        balance for now amount - Amount to transfer in kobo currency - NGN reason recipient (required) - Code for
        transfer recipient reference - If specified, the field should be a unique identifier (in lowercase) for the
        object. Only - , _ and alphanumeric characters allowed.
        """
        payload = dict(**params)
        if "source" not in payload:
            payload["source"] = "balance"
        if "amount" not in payload:
            return InvalidParameters("Please specify the amount you would like to transfer")
        if "recipient" not in payload:
            return InvalidParameters("Please include the recipient of this transfer")
        return self.post(self.gateway_path, payload)

    def list(self, query_params=None):
        return self.get(self.gateway_path, query_params)

    def verify(self, reference):
        return self.get(f"{self.gateway_path}/verify/{reference}")

    def fetch(self, id_or_code):
        return self.get(f"{self.gateway_path}/{id_or_code}")

    def finalize(self, params):
        """
        Finalizes a transfer
        :param params: transfer_code (required) - Transfer code
        otp (required) - OTP sent to business phone to verify transfer.
        """
        payload = dict(**params)
        if "transfer_code" not in payload:
            raise InvalidParameters("Transfer code is required")
        if "otp" not in payload:
            raise InvalidParameters("Otp is required")
        return self.post(f"{self.gateway_path}/finalize_transfer", payload)

    def initiate_bulk(self, params):
        """
        You need to disable the Transfers OTP requirement to use this endpoint.
        :param params: source - Where should we transfer from? Only balance for now
        transfers - Each object should contain amount, recipient, and reference
        """
        payload = dict(**params)
        self.validate(payload)
        if "source" not in payload:
            payload["source"] = "balance"
        if "transfers" not in payload:
            raise InvalidParameters("Transfers array must be provided")
        elif "transfers" in payload and not isinstance(payload["transfers"], list):
            raise InvalidParameters("Transfers must be an array of objects")
        return self.post(f"{self.gateway_path}/bulk", payload)