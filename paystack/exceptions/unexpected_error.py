from exceptions.paystack_error import paystackError

class UnexpectedError(paystackError):
    """ Raised for unknown or unexpected errors. """
    pass
