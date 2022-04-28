import requests
import json
import ast
import pandas as pd
<<<<<<< HEAD
import csv
import os
base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'

username = os.environ['VICTRON_USERNAME']
password = os.environ['VICTRON_PASSWORD']

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.eyJ1aWQiOiIxOTk2NSIsInRva2VuX3R5cGUiOiJkZWZhdWx0IiwiaXNzIjoidnJtYXBpLnZpY3Ryb25lbmVyZ3kuY29tIiwiYXVkIjoiaHR0cHM6XC9cL3ZybWFwaS52aWN0cm9uZW5lcmd5LmNvbVwvIiwiaWF0IjoxNjM0NTc2NDIxLCJleHAiOjE2MzQ2NjI4MjEsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.sE4rRr5JODlc-XJAINw27R39u55YRN2TwEH3XiF18WjlWU7EacyDw4iiv9inZq_y8ByPIbfCNOKtVt0E77kjPMzoxkxIZhdLt7PAs2WOhPaJeGrJolV6nak8XlQg874iwxPUSzVMGlW3jNcHJDGUGMJhO9Y1peF85t9B6AUR0loVsZXNDOvVJdcbSUOos5vk_drIqMtX6tR_UUd8p5CcUKfB99b8i-YJLUAgbX4GD3Kv0-1CKG-M_j78xJoiUK4K0Rb47a7Ff3g7UYYb3Aye1AdsEFJY5qRMzdKvtOp8qaGhp-QSAlGMKE4BV6ujim6ckpy1bdmBcPVfDr9xLk4Hjw'
=======
import csv, os
base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'
username = os.environ.get('VRM_USER')
password = os.environ.get('VRM_PASS')

>>>>>>> ffadd30c22935ce627d5a66993fe68101145293d
endpoint = 'https://vrmapi.victronenergy.com/v2/users/19965/installations'

details = {'username':username, 'password':password}
response = requests.post(login_url, json=details)


session = requests.Session()
session.headers['X-Authorization'] = 'Bearer ' + response.json()['token']
session.headers['Accept'] = '*/*'
session.headers['Content-Type'] = 'application/json'
session.headers['Connection'] ='Keep-Alive'


payload = session.get(endpoint)
x = payload.json() #output is in disctionary
y = json.dumps(x, indent =4) #converts the dictionary (x) to Json

val1 = json.loads(json.dumps(x)) 
val2 = val1["records"]

abc = pd.DataFrame(val2, columns=[
            "idSite",
            "accessLevel",
            "owner",
            "is_admin",
            "name",
            "identifier",
            "idUser",
            "pvMax",
            "timezone",
            "phonenumber",
            "notes",
            "geofence",
            "geofenceEnabled",
            "realtimeUpdates",
            "hasMains",
            "hasGenerator",
            "noDataAlarmTimeout",
            "alarmMonitoring",
            "invalidVRMAuthTokenUsedInLogRequest",
            "syscreated",
            "grafanaEnabled",
            "shared",
            "device_icon",
            "datesubmited"])

output = abc.to_csv('data_file.csv') #Saves the csv file to directory.

print(val2)
print('Job Completed')
