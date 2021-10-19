import requests
api_url = 'http://jsonplaceholder.typicode.com/todos/10'  #url to get the already existing data in server
api_url_post = "https://jsonplaceholder.typicode.com/todos" #url to post new todo data in to the server
todo = {"userID":1, "title": "Buy Salad", "completed":False}
todo2 = {"title": "Throw Thrash"}
response = requests.get(api_url) #call the api_url to view its content
response2 = requests.post(api_url_post, json=todo) #post the todo content into the api_url_post 
response3 = requests.patch(api_url, json=todo2) #updated/replaced the api_url content
result=response.json()
result2=response2.json()
result3=response3.json()


print(result, 'Status =', response.status_code)
print(result2, 'Status =', response.status_code)
print(result3, 'Status =', response.status_code)
