import requests
payload = {'username': 'remotemonitoring@starsightlimited.com', 'password':'Spulmonitoring'}
username= 'remotemonitoring@starsightlimited.com'
password='Spulmonitoring'
r= requests.get('https://vrmapi.victronenergy.com/v2/auth/loginAsDemo')
s=requests.get('https://vrmapi.victronenergy.com/v2/auth/login', auth=(username, password))

'''
with open('google.png', 'wb') as f:
    f.write(r.content)
#code above copy the content of the url as image to file.
'''

print(s.text)
