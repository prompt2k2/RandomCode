
import requests
import json
import ast
import pandas as pd
import csv
base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'
username = 'remotemonitoring@starsightlimited.com'
password = 'Spulmonitoring'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.eyJ1aWQiOiIxOTk2NSIsInRva2VuX3R5cGUiOiJkZWZhdWx0IiwiaXNzIjoidnJtYXBpLnZpY3Ryb25lbmVyZ3kuY29tIiwiYXVkIjoiaHR0cHM6XC9cL3ZybWFwaS52aWN0cm9uZW5lcmd5LmNvbVwvIiwiaWF0IjoxNjM0NTc2NDIxLCJleHAiOjE2MzQ2NjI4MjEsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.sE4rRr5JODlc-XJAINw27R39u55YRN2TwEH3XiF18WjlWU7EacyDw4iiv9inZq_y8ByPIbfCNOKtVt0E77kjPMzoxkxIZhdLt7PAs2WOhPaJeGrJolV6nak8XlQg874iwxPUSzVMGlW3jNcHJDGUGMJhO9Y1peF85t9B6AUR0loVsZXNDOvVJdcbSUOos5vk_drIqMtX6tR_UUd8p5CcUKfB99b8i-YJLUAgbX4GD3Kv0-1CKG-M_j78xJoiUK4K0Rb47a7Ff3g7UYYb3Aye1AdsEFJY5qRMzdKvtOp8qaGhp-QSAlGMKE4BV6ujim6ckpy1bdmBcPVfDr9xLk4Hjw'
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