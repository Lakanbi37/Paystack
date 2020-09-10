import paystack
from paystack.gateways.split_gateway import TransactionSplit
from paystack.gateways.transaction_gateway import TransactionGateway


class PaystackGateway:

    def __init__(self, secret_key, public_key, **kwargs):
        self.config = paystack.configuration.Configuration(
            secret_key=secret_key,
            public_key=public_key
        )
        print(kwargs)
        self.Transaction = TransactionGateway(self)
        self.Split = TransactionSplit(self)
