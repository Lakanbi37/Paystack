from exceptions.paystack_error import paystackError

class ServiceUnavailableError(paystackError):
    """
    Raised when the gateway is unavailable.
    """
    pass
