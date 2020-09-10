from exceptions.paystack_error import paystackError


class AuthenticationError(paystackError):
    """
    Raised when the client library cannot authenticate with the gateway.  This generally means the public_key/private key are incorrect, or the user is not active.
    """
    pass
