from exceptions.paystack_error import paystackError

class TooManyRequestsError(paystackError):
    """
    Raised when the rate limit request threshold is exceeded.
    """
    pass
