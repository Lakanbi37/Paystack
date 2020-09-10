from exceptions.paystack_error import paystackError

class TestOperationPerformedInProductionError(paystackError):
    """
    Raised when an operation that should be used for testing is used in a production environment
    """
    pass
