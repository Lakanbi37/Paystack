from paystack.gateways.gateway import BaseGateway
from paystack.exceptions.invalid_parameter import InvalidParameters


class TransferControl(BaseGateway):
    gateway_path = "/balance"
    control_path = "/transfer"

    def check_balance(self):
        return self.get(self.gateway_path)

    def balance_ledger(self):
        return self.get(f"{self.gateway_path}/ledger")

    def resend_otp(self, params):
        """
        Creates a new recipient. An duplicate account number will lead to the retrieval of the existing record.
        :param params: transfer_code (required) - Transfer code
        reason (required) - either resend_otp or transfer
        """
        payload = dict(**params)
        self.validate(params)
        if "transfer_code" not in payload:
            raise InvalidParameters("Transfer code is required")
        if "reason" not in payload or payload["reason"] == "":
            payload["reason"] = "resend_otp"
        return self.post(f"{self.control_path}/resend_otp", payload)

    def disable_otp(self):
        """
        In the event that you want to be able to complete transfers programmatically without use of OTPs,
        this endpoint helps disable that….with an OTP. No arguments required. You will get an OTP. In the event that
        you want to be able to complete transfers programmatically without use of OTPs, this endpoint helps disable
        that….with an OTP. No arguments required. An OTP is sent to you on your business phone.
        """
        return self.post(f"{self.control_path}/disable_otp", params=None)

    def finalize_disable(self, params):
        """
        :param params: otp (required) - OTP sent to business phone to verify disabling OTP requirement
        """
        payload = dict(**params)
        if "otp" not in payload:
            raise InvalidParameters("Otp not provided")
        if len(payload) > 1:
            raise InvalidParameters("This endpoint only accepts one body parameters")
        return self.post(f"{self.control_path}/disable_otp_finalize", payload)

    def enable_otp(self):
        """
        In the event that a customer wants to stop being able to complete transfers programmatically, this endpoint
        helps turn OTP requirement back on. No arguments required.
        """
        return self.post(f"{self.control_path}/enable_otp", params=None)