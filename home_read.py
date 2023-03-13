print("hi python")
#import requests
#Test Request
# BASE_URL = 'https://fakestoreapi.com'#
# response = requests.get('{}/products'.format(BASE_URL))
# print(response.json())

#Test post
# import json
# api_url = "https://jsonplaceholder.typicode.com/todos"
# todo = {"userId": 1, "title": "Buy milk", "completed": False}
# headers =  {"Content-Type":"application/json"}
# response = requests.post(api_url, data=json.dumps(todo), headers=headers)
#response = requests.put(api_url, json=todo)
#response = requests.patch(api_url, json=todo)
#response = requests.delete(api_url)
# response.json()
# response.status_code
#--------------------- Api
#https://docs.coinapi.io/#timeseries-periods-get
#list all exchanges icon
#type_output = 'assets'
#list all asset icon
#type_output = 'symbols'

#list all exchanges
# import coin
# import json
#
# type_output = 'exchanges'
# result_all_list_exchange = coin.list_all(type_output)
# result_str = json.dumps(result_all_list_exchange)
#
# with open("list_coin.txt","w",encoding="utf-8") as my_file:
#    my_file.write(result_str)
# print(my_file.closed)