import http.client
import json
import base64


class PaymentWithPayaza:
    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base64_key = base64.b64encode(bytes(self.api_key, 'utf-8'))

    def createVirtualAccount(self) -> str:
 
        conn = http.client.HTTPSConnection("router-live.78financials.com")
        payload = json.dumps({
            "service_type": "Account",
            "service_payload": {
                "request_application": "Payaza",
                "application_module": "USER_MODULE",
                "application_version": "1.0.0",
                "request_class": "MerchantCreateVirtualAccount",
                "customer_first_name": "Abraham",
                "customer_last_name": "Audu",
                "customer_email": "ab6ril@gmail.com",
                "customer_phone": "08137474667",
                "virtual_account_provider": "Premiumtrust",
                "payment_amount": 102,
                "payment_reference": "RCO1322XLINE"
            }
        })
        headers = {
            'Authorization': f'Payaza {self.base64_key.decode()}',
            'Content-Type': 'application/json'
        }
        conn.request(
            "POST",
            "/api/request/secure/payloadhandler",
            payload,
            headers
        )
        res = conn.getresponse()
        data = res.read()
        
        return data.decode("utf-8")
    
    def accountStatus(self):
        conn = http.client.HTTPSConnection("router-live.78financials.com")
        payload = json.dumps({
            "service_type": "Account",
            "service_payload": {
                "request_application": "Payaza",
                "application_module": "USER_MODULE",
                "application_version": "1.0.0",
                "request_class": "GetAccountDetailsStaticAndDynamic",
                "virtual_account_number": "4030754610"
            }
        })
        headers = {
            'Authorization': f'Payaza {self.base64_key.decode()}',
            'Content-Type': 'application/json'
        }
        conn.request(
            "POST",
            "/api/request/secure/payloadhandler",
            payload,
            headers
        )
        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")

    def creatReservedAccount(self):
        conn = http.client.HTTPSConnection("router-live.78financials.com")
        payload = json.dumps({
            "service_type": "Account",
            "service_payload": {
                "request_application": "Payaza",
                "application_module": "USER_MODULE",
                "application_version": "1.0.0",
                "request_class": "CreateReservedAccountForCustomers",
                "customer_first_name": "Abraham",
                "customer_last_name": "Audu",
                "customer_email": "ab6ril@gmail.com",
                "customer_phone": "08137474667",
                "virtual_account_provider": "Premiumtrust"
            }
        })
        headers = {
            'Authorization': f'Payaza {self.base64_key.decode()}',
            'Content-Type': 'application/json'
        }
        conn.request(
            "POST",
            "/api/request/secure/payloadhandler",
            payload,
            headers
        )
        res = conn.getresponse()
        data = res.read()

        return data.decode("utf-8")

