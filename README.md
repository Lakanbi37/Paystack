# Paystack Python library

The Paystack Python library provides integration access to the Paystack Payments.

## Dependencies

* [requests](http://docs.python-requests.org/en/latest/)

The Paystack Python SDK is tested against Python version 3.8

_The Python core development community has released [End-of-Life branches](https://devguide.python.org/devcycle/#end-of-life-branches) for Python versions 2.7 - 3.4, and are no longer receiving [security updates](https://devguide.python.org/#branchstatus). As a result, Paystack may not supports these versions of Python._

## Documentation

 * [Official paystack documentation](https://paystack.com/docs/api/)
 * [Official paystack python documentation](https://docs.readthedocs.io/en/stable/intro/getting-started-with-paystack-python.html)

## Quick Start Example

```python
import paystack

test_secret_key = "sk_test_<YOUR_SECRET_KEY>"
test_public_key = "pk_test_<YOUR_PUBLIC_KEY>"


gateway = paystack.paystack_gateway.PaystackGateway(
    secret_key=test_secret_key,
    public_key=test_public_key,
)

charge = gateway.Transaction.initiate({ 
    "email": "example@domain.com",
    "amount": "200000",
  })

# print the response to the terminal
print(charge)

# url to finalize the charge
url = charge.data.authorization_url

# verify a transaction with the response reference_key
gateway.Transaction.verify(charge.data.reference)

# check docs module for more intergration examples

```

## Developing
 ## using Virtualenv

  1. Create a [virtualenv](https://virtualenv.pypa.io/) called `venv`:

       ```
       virtualenv venv
       ```

  2. Start the virtualenv:

       ```
       source venv/bin/activate
       ```

  3. Install dependencies:

       ```
       pip3 install -r dev_requirements.txt
       ```
   
 ## Using pipenv
  
   1. install pipenv:
 
        ```
        pip3 install pipenv
        ```
     
   2. create a folder:
 
        ```
        mkdir <folder_name> && cd <folder_name>
        ```
   3. activate pipenv environment in new folder:
 
        ```
        pipenv .
        ```
    
   4. activate the virtual environment:
 
        ```
        pipenv shell
        ```
    
   5. install dependencies:
 
        ```
        pipenv install -r requirements.txt
        ```
     

See the [LICENSE](LICENSE) file for more info.
