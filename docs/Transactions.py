import paystack


test_secret_key = "sk_test_8351c0a7076231250c0b44f713ab30aa6e67443d"
test_public_key = "pk_test_b24460600bf11c0d091f06f9ed1b2a3d348f8179"

gateway = paystack.PaystackGateway(secret_key=test_secret_key, public_key=test_public_key)
reference = "gaqd39d2id"
access_code = "zgtvz9fzbv1d6s6"
auth_code = "AUTH_vbczob5t51"

# initiate a charge
initiate_charge = gateway.Transaction.initiate({
    "email": "lakanbi63@gmail.com",
    "amount": "15000000",
    "metadata": {
        "reason": "testing paystack api",
        "user": "Lekan Akanbi",
        "date": "10-09-2020"
    }
})

# verify a charge
gateway.Transaction.verify(reference)

# authorize a previous user saved on the system
charge = gateway.Transaction.authorize({
    "authorization_code": auth_code,
    "amount": "2000000",
    "email": "lakanbi63@gmail.com",
})

check = gateway.Transaction.check_authorization({
    "authorization_code": auth_code,
    "amount": "2000000",
    "email": "lakanbi63@gmail.com",
})