import requests, os, json
from datetime import datetime

# Proxy in case in corp network
def use_proxy():
    proxy = 'http://aht:MindenFasza69@10.220.40.138:3128'
    os.environ['http_proxy'] = proxy
    os.environ['https_proxy'] = proxy

#use_proxy()

# Start main
startTime = datetime.now()
print('Start time {}'.format(str(startTime)))

# Call Azure Function
headers = {'Content-Type': 'application/json', 'x-functions-key': 'ShfuEG6THFXywj6jhohfaoGmzRc2z6SZyYdJ18FHHo1pwaJivuHTTw=='}
body = {
    "readings": [
        {
            "driveGearId": 1,
            "timestamp": 1534263995,
            "temperature": 23
        },
        {
            "driveGearId": 3,
            "timestamp": 1534264048,
            "temperature": 45
        },
        {
            "driveGearId": 18,
            "timestamp": 1534264050,
            "temperature": 55
        }
    ]
}

body = json.dumps(body)

response = requests.post('https://escalator-functions-sbl78.azurewebsites.net/api/DriveGearTemperatureService', headers=headers, data=body)
print(response.json())
