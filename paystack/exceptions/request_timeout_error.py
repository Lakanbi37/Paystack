from exceptions.paystack_error import paystackError

class RequestTimeoutError(paystackError):
    """
    Raised when a client request timeout occurs.
    """
    pass
