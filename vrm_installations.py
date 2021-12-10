import vrmlogin 
import requests
import pandas as pd
#from vrmlogin import Session as session
import json, os

username = os.environ.get('VRM_USER')
password = os.environ.get('VRM_PASS')

details={'username':username, 'password':password}

base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'
endpoint = 'https://vrmapi.victronenergy.com/v2/users/19965/installations'

start = 1633046400
end= 1635724800
interval = 'days' #You can change this to seconds, minutes, hours, days, weeks
attrs = "attributesCodes"
attributes = 'S'
response = requests.post(login_url, json=details)

vrmlogin.response()
session = requests.Session()
session.headers['X-Authorization'] = 'Bearer ' + response.json()['token']
session.headers['Accept'] = '*/*'
session.headers['Content-Type'] = 'application/json'
session.headers['Connection'] ='Keep-Alive'
payload = session.get(endpoint)
x = payload.json() #output is in disctionary


val1 = json.loads(json.dumps(x)) #converts the dictionary (x) to Json
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

print(abc)
print('Job Completed')
