from exceptions.paystack_error import paystackError

class UpgradeRequiredError(paystackError):
    """
    Raised for unsupported client library versions.
    """
    pass
