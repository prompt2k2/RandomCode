import requests
api_url = 'http://jsonplaceholder.typicode.com/todos/1'  #url to get the already existing data in server
api_url_post = "https://jsonplaceholder.typicode.com/todos" #url to post new todo data in to the server
todo = {"userID":1, "title": "Buy Salad", "completed":False}
response = requests.get(api_url)
response2 = requests.post(api_url_post, json=todo)
result=response.json()
result2=response2.json()


print(result, 'Status =', response.status_code)
print(result2, 'Status =', response.status_code)
