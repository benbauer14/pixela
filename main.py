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
# response = requests.post(url="https://pixe.la/v1/users/bbauer/graphs",json=pixela_graph_parameters, headers=headers)

#post activity to graph

pixela_activity_post = {
    "date": "20210728",
    "quantity": "4",
}

# response = requests.post("https://pixe.la/v1/users/bbauer/graphs/graph1", json=pixela_activity_post, headers=headers)


#update a pixel
pixela_update = {
    "quantity": "50",
}

# response = requests.put(url="https://pixe.la/v1/users/bbauer/graphs/graph1/20210728", json=pixela_update, headers=headers)

#delete a pixel
response = requests.delete(url="https://pixe.la/v1/users/bbauer/graphs/graph1/20210728", headers=headers)

print(response.text)