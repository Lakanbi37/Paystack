from exceptions.paystack_error import paystackError

class ServerError(paystackError):
    """
    Raised when the gateway raises an error.  Please contant support at support@getpaystack.com.

    See https://developers.paystackpayments.com/reference/general/exceptions/python#server-error
    """
    pass
