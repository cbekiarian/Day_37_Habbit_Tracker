import requests
import datetime as dt
USERNAME = ""
TOKEN = ""
GRAPH_ID =""
URL="https://pixe.la/v1/users"
user_params={
    "token" : TOKEN ,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor":"yes",

}

# response = requests.post(url=URL,json=user_params)
# print(response.text)
graph_config={
    "id" : GRAPH_ID,
    "name" : "Thesis counter",
    "unit" : "Days",
    "type" : "int",
    "color" : "ajisai",
}
headers ={
    "X-USER-TOKEN": TOKEN
}
# URL1 = f"{URL}/{USERNAME}/graphs"
# response1 = requests.post(url=URL1,json=graph_config,headers=headers)
# print(response1.text)
URL2 = f"{URL}/{USERNAME}/graphs/{GRAPH_ID}"
now= dt.datetime.now()

x="".join([now.strftime("%Y"),now.strftime("%m"),now.strftime("%d")])
print(x)
# token_params ={
#     "date" : "20231015",
#     "quantity" : "6",
# }
#
# response2 = requests.post(url=URL2,json=token_params,headers=headers)
# print(response2.text)
URL3 = f"{URL}/{USERNAME}/graphs/{GRAPH_ID}/{x}"
token_params2 ={
    "quantity" : "3",
}
response3 = requests.put(url=URL3,json=token_params2,headers=headers)
print(response3.text)

response4 = requests.delete(url=URL3,headers=headers)
print(response4.text)