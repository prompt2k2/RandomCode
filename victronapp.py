import requests
import json
import ast
import pandas as pd
import csv, os
base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'
username = os.environ.get('VRM_USER')
password = os.environ.get('VRM_PASS')

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
