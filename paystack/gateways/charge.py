from paystack.gateways.gateway import BaseGateway
from paystack.exceptions.card_error import CardError
from paystack.exceptions.bank_error import BankError
from paystack.exceptions.invalid_parameter import InvalidParameters


class Charge(BaseGateway):
    gateway_path = "/charge"
    """
    The Charge API allows you to configure payment channel of your choice when initiating a payment.\n The charge 
    API allows you to pass details of any payment instrument directly to Paystack, along with the transaction details 
    (email, amount, etc). We cover all the different payment methods in detail below, but in this section, 
    we want to discuss how to handle responses from the charge API. Here is a sample payload to the Charge API 
    containing transaction details and an object for a payment instrument.\n When you call the Charge API, 
    the response contains a data.status which tells you what the next step in the process. Depending on the value in 
    the data.status, you may need to prompt the user for an input as indicated in the response message (like OTP or 
    pin or date of birth), or display an action that the user needs to complete on their device - like scanning a QR 
    code or dialling a USSD code or redirecting to a 3DSecure page. So you follow the prompt on the data.status until 
    there is no more user input required, then you can call the verify endpoint to confirm payment. For the steps 
    that prompt for user input, you will be required to display a form to the user to collect the requested input and 
    send it to the relevant endpoint as shown in the table below. For the steps that require the user to complete an 
    action on their device, we recommend that you display a button for the user to confirm the payment after they 
    have performed that action so that you can call the verify endpoint to confirm the payment. 
    """

    def submit(self, url, params, obj):
        payload = dict(**params)
        ref = payload.get("reference", None)
        _obj = payload.get(obj, None)
        if not ref:
            raise InvalidParameters("Transaction reference cannot be null")
        if not _obj:
            raise InvalidParameters(f"{obj} cannot be null")
        return self.post(url, payload)

    def charge(self, params):
        """
        Send card details or bank details or authorization code to start a charge. Simple guide to charging cards
        directly \n
        :param params: email (required) - Customer's email address amount (required) - Amount in kobo
        card (required) - Card number card.number (required) - Card to tokenize card.cvv (required) - Card security
        code card.expiry_month (required) - Expiry month of card card.expiry_year (required) - Expiry year of card
        bank - Bank account to charge (don't send if charging an authorization code or card) bank.code (required) - A
        code for the bank (check banks for the banks supported). Only the ones for which paywithbank is true will
        work. bank.account_number (required) - 10 digit nuban for the account to charge authorization_code - An
        authorization code to charge (don't send if charging a card or bank account) pin - 4-digit PIN (send with a
        non-reusable authorization code) metadata - A JSON object \n
        :return:
        """
        return self.post(self.gateway_path, params)

    def charge_card(self, params):
        """
        Directly charge a bank card.\n We strongly discourage passing card information directly to the API to avoid
        transmitting card data through systems that are not PCI compliant. If you are PCI-DSS certified and would
        like to be able to send cardholder information directly to our APIs from your servers, reach out to us!.\n
        :param params:
        :return:
        """
        payload = dict(**params)
        if len(payload) == 0:
            raise InvalidParameters("Parameters cannot be empty")
        card = payload["card"]
        if len(card) == 0:
            raise CardError("Bank card have not been provided")
        if card["cvv"] == "":
            raise CardError("Invalid cvv")
        if card["expiry_year"] == "":
            raise CardError("Invalid expiry")
        return self.charge(payload)

    def bank_charge(self, params):
        """
        The Pay with Bank feature allows customers pay through internet banking portal or by providing their bank
        account number and authenticating using an OTP sent to their phone or email. This is different from Bank
        Transfers where customers transfer money into a bank account.\n To collect bank details, you would need to
        prompt the user to select their bank and enter their account number. To fetch the list of supported banks,
        make a GET request to the List BanksAPI endpoint, with the additional filter pay_with_bank=true. The banks
        can be listed in a dropdown or any other format that allows the user to easily pick their bank of choice.\n
        :param params:
        :return:
        """
        payload = dict(**params)
        bank = payload["bank"]
        if len(bank) == 0:
            raise BankError("Bank details not provided")
        if bank["code"] and bank["account_number"] == "":
            raise BankError("Invalid bank details")
        if bank["code"] or bank["account_number"] == "":
            raise BankError("Invalid bank details")
        return self.charge(payload)

    def ussd_charge(self, params):
        """
        This Payment method is specifically for Nigerian customers. Nigerian Banks provide USSD services that
        customers use to perform transactions, and we've integrated with some of them to enable customers complete
        payments. The Pay via USSD channel allows your Nigerian customers to pay you by dialling a USSD code on their
        mobile device. This code is usually in the form of * followed by some code and ending with #. The user is
        prompted to authenticate the transaction with a PIN and then it is confirmed. All you need to initiate a USSD
        charge is the customer email and the amount to charge. When the user pays, a response will be sent to your
        webhook. Hence, for this to work properly as expected, webhooks must be set up on your Paystack Dashboard.
        :param params:
        :return:
        """
        payload = dict(**params)
        code = payload["code"]
        if len(code) == 0 or code["ussd"] == "":
            raise InvalidParameters("Invalid ussd parameter")
        return self.charge(payload)

    def qr_code(self, params):
        """
        The QR option generates a QR code which allows customers to use their bank's mobile app to complete payments.
        We currently have only Visa QR option available. We'll have more options later. When the customer scans the
        code, they authenticate on their bank app to complete the payment. When the user pays, a response will be
        sent to your webhook. This means that you need to have webhooks set up on your Paystack Dashboard.
        :param params:
        :return:
        """
        payload = dict(**params)
        return self.charge(payload)

    def submit_otp(self, params):
        """
        otp (required) - OTP submitted by user
        reference (required) - reference for ongoing transaction.\n
        :param params:
        :return:
        """
        return self.submit(self.gateway_path + "/submit_otp", params, "otp")

    def submit_pin(self, params):
        return self.submit(self.gateway_path + "/submit_pin", params, "pin")

    def submit_phone(self, params):
        return self.submit(self.gateway_path + "/submit_phone", params, "phone")

    def submit_dob(self, params):
        return self.submit(self.gateway_path + "/submit_birthday", params, "birthday")

    def submit_address(self, params):
        payload = dict(**params)
        return self.post(self.gateway_path + "/submit_address", payload)

    def check_charge_status(self, reference):
        return self.get(self.gateway_path+"/"+reference)
