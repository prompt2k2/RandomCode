
import requests
import json
import ast
import pandas as pd
import csv, os
base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'
username = os.environ.get('VRM_USER')
password = os.environ.get('VRM_PASS')

endp1 = 'https://vrmapi.victronenergy.com/v2/users/19965/diagnostics?attributeCodes%5b%5d=OF'

details = {'username':username, 'password':password}
response = requests.post(login_url, json=details)

     
session = requests.Session()
session.headers['X-Authorization'] = 'Bearer ' + response.json()['token']
session.headers['Accept'] = '*/*'
session.headers['Content-Type'] = 'application/json'
session.headers['Connection'] ='Keep-Alive'
    
payload = session.get(endp1)
x = payload.json() #output is in disctionary
y = json.dumps(x["records"], indent=4)


'''
val1 = json.loads(json.dumps(x)) #converts the dictionary (x) to Json
val2 = val1["records"]

z = pd.DataFrame(val2, columns=[
                "ID",
                "timestamp",
                "Device",
                "instance",
                "idDataAttribute",
                "description",
                "code",
                "formattedValue",
                "rawValue"])

'''
FIELDS = ["Sites", "records.recordTimestamp", "records.Device", "records.Instance", "records.idDataAttribute", "records.Description", "records.Code", "records.formattedValue", "records.rawValue"]

df = pd.json_normalize(y)

print(df)