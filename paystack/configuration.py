import paystack
from paystack.exceptions import ConfigurationError
import paystack.paystack_gateway
import paystack.request.http_request


class Configuration:

    def __init__(self, secret_key, public_key, **kwargs):
        if secret_key == "":
            raise ConfigurationError("Missing Secret key")
        if public_key == "":
            raise ConfigurationError("Missing Public key")
        self.secret_key = secret_key
        self.public_key = public_key
        self.timeout = kwargs.get("timeout", 60)

    @staticmethod
    def configure(secret_key, public_key, **kwargs):
        Configuration.secret_key = secret_key
        Configuration.public_key = public_key
        Configuration.timeout = kwargs.get("timeout", 60)

    @staticmethod
    def instantiate():
        return Configuration(
            secret_key=Configuration.secret_key,
            public_key=Configuration.public_key,
            timeout=Configuration.timeout
        )

    @staticmethod
    def gateway():
        return paystack.paystack_gateway.PaystackGateway(config=Configuration.instantiate())

    def http(self):
        return paystack.request.http_request.Http(secret_key=self.secret_key, timeout=self.timeout)
