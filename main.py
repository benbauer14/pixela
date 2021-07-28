import requests

pixela_endpoint = "https://pixe.la/v1/users"

pixela_parameters = {
    "token":"ABIOCIAKSDML15124mk", 
    "username":"bbauer", 
    "agreeTermsOfService":"yes", 
    "notMinor":"yes"
}

#Create account
# response = requests.post(url=pixela_endpoint, json=pixela_parameters)

pixela_graph_parameters = {
    "id": "graph1",
    "name": "Step Count",
    "unit": "steps",
    "type": "int",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": "ABIOCIAKSDML15124mk", 
}

#Create graph
response = requests.post(url="https://pixe.la/v1/users/bbauer/graphs",json=pixela_graph_parameters, headers=headers)
print(response.text)