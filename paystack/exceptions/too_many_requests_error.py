from exceptions.paystack_error import paystackError

class TooManyRequestsError(paystackError):
    """
    Raised when the rate limit api threshold is exceeded.
    """
    pass
