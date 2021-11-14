import requests
import json
import ast
import pandas as pd
import csv

base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'

username = 'remotemonitoring@starsightlimited.com'
password = 'Spulmonitoring'

token = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0' \
        '.eyJ1aWQiOiIxOTk2NSIsInRva2VuX3R5cGUiOiJkZWZhdWx0IiwiaXNzIjoidnJtYXBpLnZpY3Ryb25lbmVyZ3kuY29tIiwiYXVkIjoiaHR0cHM6XC9cL3ZybWFwaS52aWN0cm9uZW5lcmd5LmNvbVwvIiwiaWF0IjoxNjM0NTc2NDIxLCJleHAiOjE2MzQ2NjI4MjEsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.sE4rRr5JODlc-XJAINw27R39u55YRN2TwEH3XiF18WjlWU7EacyDw4iiv9inZq_y8ByPIbfCNOKtVt0E77kjPMzoxkxIZhdLt7PAs2WOhPaJeGrJolV6nak8XlQg874iwxPUSzVMGlW3jNcHJDGUGMJhO9Y1peF85t9B6AUR0loVsZXNDOvVJdcbSUOos5vk_drIqMtX6tR_UUd8p5CcUKfB99b8i-YJLUAgbX4GD3Kv0-1CKG-M_j78xJoiUK4K0Rb47a7Ff3g7UYYb3Aye1AdsEFJY5qRMzdKvtOp8qaGhp-QSAlGMKE4BV6ujim6ckpy1bdmBcPVfDr9xLk4Hjw '

endpoint = 'https://vrmapi.victronenergy.com/v2/installations/77157/stats?type=kwh&start=1609462800&end=1636491600' \
           '&interval=days '

ER = base_url + 'users/19965/diagnostics?attributeCodes[]=Gc&attributeCodes[]=Bc&attributeCodes[' \
                ']=dH21&attributeCodes[]=dH22&attributeCodes[]=Gb&attributeCodes[]=Pc&attributeCodes[' \
                ']=Pb&attributeCodes[]=Pg&attributeCodes[]=gc&attributeCodes[]=gb&attributeCodes[' \
                ']=kwh&start=1609462800&end=1635721200&interval=days '

details = {'username': username, 'password': password}
response = requests.post(login_url, json=details)

# Get all the installation ids for the user.

installation_url = base_url + 'users/19965/installations'

'''
start = 1633046400
end= 1635724800
interval = 'days' #You can change this to seconds, minutes, hours, days, weeks
attrs = "attributesCodes"
attributes = 'S'
response = requests.post(login_url, json=details)
'''
session = requests.Session()
session.headers['X-Authorization'] = 'Bearer ' + response.json()['token']
session.headers['Accept'] = '*/*'
session.headers['Content-Type'] = 'application/json'
session.headers['Connection'] = 'Keep-Alive'

payload = session.get(installation_url)
x = payload.json()  # output is in disctionary
y = json.dumps(x['records'], indent=4)  # converts the dictionary (x) to Json

# val1 = json.loads(json.dumps(x['records'])) #Dictionary
# r1 = val1.items() #List
# r2 = list(r1)

# df = pd.DataFrame(r2, columns = ["Attribute", "Reading"])
###################################################################################################################
# Don't delete the line below. NEVER!!!!!!!!!!
# dfT = pd.DataFrame.from_dict(x['records'], orient='index').T.reset_index(drop=True)  # Transposed the DataFrame
# df = pd.DataFrame.from_dict(x['records'], orient='index').reset_index(drop=True)  # Untransposed the DataFrame

###################################################################################################################

# output = df.to_csv('c:\\Users\\Enigma\\Downloads\\EnergyReading2021.csv')
print(y)
# print(dfT)


# for i in df['Attribute']:
#     for j in df['Reading']:


#         print(i, j[0][0], j[0][1])
