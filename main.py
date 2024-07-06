from demo_app import PaymentWithPayaza

payment = PaymentWithPayaza("PZ78-PKLIVE-0E3EEBF6-B58B-4DD2-9C78-99D1E61945F8")

response = payment.createVirtualAccount()

print(response)