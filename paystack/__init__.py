import paystack.configuration
import paystack.exceptions
import paystack.exceptions.http
import paystack.api.http
from paystack.gateways.transactions import TransactionGateway
from paystack.gateways.payment_splits import TransactionSplit
from paystack.gateways.subaccounts import Subaccount
from paystack.gateways.customers import Customer
from paystack.gateways.payment_plans import Plans
from paystack.gateways.Subscriptions import Subscriptions
from paystack.gateways.charge import Charge
from paystack.gateways.refund import Refunds
from paystack.gateways.transfer import Transfers
from paystack.gateways.controls import TransferControl
from paystack.gateways.misc import Misc
from paystack.gateways.settlements import Settlements


class PaystackGateway:

    def __init__(self, secret_key, public_key, **kwargs):
        self.config = paystack.configuration.Configuration(
            secret_key=secret_key,
            public_key=public_key
        )
        self.Transaction = TransactionGateway(self)
        self.Split = TransactionSplit(self)
        self.Customer = Customer(self)
        self.Subaccount = Subaccount(self)
        self.Plans = Plans(self)
        self.Subscriptions = Subscriptions(self)
        self.Charge = Charge(self)
        self.Refunds = Refunds(self)
        self.Transfers = Transfers(self)
        self.Control = TransferControl(self)
        self.Misc = Misc(self)
        self.Settlements = Settlements(self)