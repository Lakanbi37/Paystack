from exceptions.paystack_error import paystackError

class NotFoundError(paystackError):
    """
    Raised when an object is not found in the gateway, such as a Transaction.find("bad_id").

    See https://developers.paystackpayments.com/reference/general/exceptions/python#not-found-error
    """
    pass
