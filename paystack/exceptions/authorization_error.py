from exceptions.paystack_error import paystackError


class AuthorizationError(paystackError):
    """
    Raised when the user does not have permission to complete the requested operation.
    """
    pass
