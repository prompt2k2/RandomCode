#https://stackoverflow.com/questions/51812123/python-connect-to-api-using-username-password-and-api-key?rq=1

import requests

base_url = 'https://vrmapi.victronenergy.com/v2/'
login_url = base_url + 'auth/login'
API_KEY = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJSUzI1NiIsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.eyJ1aWQiOiIxOTk2NSIsInRva2VuX3R5cGUiOiJkZWZhdWx0IiwiaXNzIjoidnJtYXBpLnZpY3Ryb25lbmVyZ3kuY29tIiwiYXVkIjoiaHR0cHM6XC9cL3ZybWFwaS52aWN0cm9uZW5lcmd5LmNvbVwvIiwiaWF0IjoxNjM0NTc2NDIxLCJleHAiOjE2MzQ2NjI4MjEsImp0aSI6ImFmMjkxY2EyNTNhYjM1YzFmZWFmNzBmNTQ0NWMyYTBjIn0.sE4rRr5JODlc-XJAINw27R39u55YRN2TwEH3XiF18WjlWU7EacyDw4iiv9inZq_y8ByPIbfCNOKtVt0E77kjPMzoxkxIZhdLt7PAs2WOhPaJeGrJolV6nak8XlQg874iwxPUSzVMGlW3jNcHJDGUGMJhO9Y1peF85t9B6AUR0loVsZXNDOvVJdcbSUOos5vk_drIqMtX6tR_UUd8p5CcUKfB99b8i-YJLUAgbX4GD3Kv0-1CKG-M_j78xJoiUK4K0Rb47a7Ff3g7UYYb3Aye1AdsEFJY5qRMzdKvtOp8qaGhp-QSAlGMKE4BV6ujim6ckpy1bdmBcPVfDr9xLk4Hjw'
username = 'remotemonitoring@starsightlimited.com'
password = 'Spulmonitoring'

session = requests.Session()
# these are sent along for all requests
session.headers['X-Authorization'] = API_KEY
# not strictly needed, but the documentation recommends it.
session.headers['Accept'] = "application/json; charset=UTF-8"

# log in first, to get the tokens
response = session.post(
    url + '/session',
    json={'identifier': username, 'password': password},
    headers={'VERSION': '2'},
)
response.raise_for_status()  # if not a 2xx response, raise an exception
# copy across the v1/v2 tokens
session.headers['CST'] = response.headers['CST']
session.headers['X-SECURITY-TOKEN'] = response.headers['X-SECURITY-TOKEN']

session = requests.Session()
# these are sent along for all requests
session.headers['X-IG-API-KEY'] = API_KEY

# log in first, to get the tokens
response = session.post(
    url + '/session',
    json={'identifier': username, 'password': password},
    headers={'VERSION': '3'},
)
response.raise_for_status()  # if not a 2xx response, raise an exception
response_data = response.json()
oauth_tokens = response_data['oauthToken']

session.headers['Authorization'] = 'Bearer ' + oauth_tokens['access_token']
session.headers['IG-ACCOUNT-ID'] = response_data['accountId']

#https://stackoverflow.com/questions/51812123/python-connect-to-api-using-username-password-and-api-key?rq=1