import requests, os

# API auth vars
clientId = "649122f0-859f-487c-ad09-75528470c6df"
clientSecret = "nofAneTFsGyr/z/d98Ul9sFM+aJ4myLmWg7Lg3cDdgg="
tenantId = "3d08d325-47e1-4822-89e2-07ec9997b68e"


# Proxy in case in corp network
def use_proxy():
    proxy = 'http://aht:MindenFasza69@10.220.40.138:3128'
    os.environ['http_proxy'] = proxy
    os.environ['https_proxy'] = proxy


# Getting authentication header
requestHeader = {}
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
body = {'grant_type': 'client_credentials', 'resource': 'https://management.azure.com/', 'client_id': clientId,
        'client_secret': clientSecret, }
response = requests.post('https://login.windows.net/' + str(tenantId) + '/oauth2/token?api-version=1.0', headers=headers, data=body)
if response.status_code != 200:
    print("[AUTH] -- HTTP Error:", response.status_code)
else:
    print("[AUTH] -- Access token acquired")
    auth_key = (response.json().get("access_token"))
    requestHeader = {
        "Authorization": "Bearer " + auth_key,
        "content-type": "application/json",
    }

# Parameters
vmName = "cf-core03"
rgpName = "MCSEW-RGP-CFW-DEV"
subId = "19625c0d-007e-48a2-8e0d-e64f68a02ce0"
vmLocation = "westeurope"
uriPrefix = "https://management.azure.com/subscriptions/"

uri = str(
    uriPrefix + subId + "/resourceGroups/" + rgpName + "/providers/Microsoft.Compute/virtualMachines/" + vmName + "/extensions/joindomain?api-version=2018-06-01")
extCheck = (requests.get(uri, headers=requestHeader))
print(extCheck.json().get("properties").get("provisioningState"))
