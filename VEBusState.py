import requests
import json
import ast
import pandas as pd
import csv
import re
base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'
username = 'remotemonitoring@starsightlimited.com'
password = 'Spulmonitoring'
token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.eyJ1aWQiOiIxOTk2NSIsInRva2VuX3R5cGUiOiJkZWZhdWx0IiwiaXNzIjoidnJtYXBpLnZpY3Ryb25lbmVyZ3kuY29tIiwiYXVkIjoiaHR0cHM6XC9cL3ZybWFwaS52aWN0cm9uZW5lcmd5LmNvbVwvIiwiaWF0IjoxNjM0NTc2NDIxLCJleHAiOjE2MzQ2NjI4MjEsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.sE4rRr5JODlc-XJAINw27R39u55YRN2TwEH3XiF18WjlWU7EacyDw4iiv9inZq_y8ByPIbfCNOKtVt0E77kjPMzoxkxIZhdLt7PAs2WOhPaJeGrJolV6nak8XlQg874iwxPUSzVMGlW3jNcHJDGUGMJhO9Y1peF85t9B6AUR0loVsZXNDOvVJdcbSUOos5vk_drIqMtX6tR_UUd8p5CcUKfB99b8i-YJLUAgbX4GD3Kv0-1CKG-M_j78xJoiUK4K0Rb47a7Ff3g7UYYb3Aye1AdsEFJY5qRMzdKvtOp8qaGhp-QSAlGMKE4BV6ujim6ckpy1bdmBcPVfDr9xLk4Hjw'
start = 16330000000
end= 1635700000
interval = 'days' #You can change this to seconds, minutes, hours, days, weeks
attrs = "attributesCodes"
attributes = 'S'


details = {'username':username, 'password':password}
response = requests.post(login_url, json=details)


session = requests.Session()
session.headers['X-Authorization'] = 'Bearer ' + response.json()['token']
session.headers['Accept'] = '*/*'
session.headers['Content-Type'] = 'application/json'
session.headers['Connection'] ='Keep-Alive'

params = {attrs:attributes,'start': start, 'end':end, 'interval':interval}
endpoint = 'https://vrmapi.victronenergy.com/v2/users/19965/diagnostics'
ep_dated = 'https://vrmapi.victronenergy.com/v2/users/19965/diagnostics?attributeCodes[]=S&start=1633046400&end=1635724800&interval=minutes'

checkers = requests.get(endpoint, params=params)


'''
payload = session.get(ep_dated)
x = payload.json() #output is in disctionary


val1 = json.loads(json.dumps(x, indent=4)) #converts the dictionary (x) to Json
val2 = val1["records"] #This is a dictionary
val3 = val2.items()
val4 = list(val3) #Working List
df = pd.DataFrame(val4, columns = ["Sites", "Values"])

all_ = []

for i in df.index:
    w = pd.DataFrame(df["Values"][i], columns = ["timestamp", "Device", "instance", "idDataAttribute", "description", "code", "formattedValue", "rawValue"])
    for j in w.index:
        
        data = df["Sites"][i], w["timestamp"][j], w["Device"][j], w["instance"][j], w["idDataAttribute"][j], w['description'][j], w['code'][j], w['formattedValue'][j], w['rawValue'][j]
        all_.append(data) #converts all tuples to list
        
        
    


frame = pd.DataFrame(all_, columns=[
    "SiteID", "timestamp", "Device", "instance", "idDataAttribute", "description", "code", "formattedValue", "rawValue"
])

print(frame)

output = frame.to_csv('DownloadFile.csv') #Saves the csv file to directory.
'''

print(checkers.url)


