import json
import requests

def collection_from_file():
    test_data_file = open('api_test_data.json')
    pokedata_orig = json.load(test_data_file)
    test_data_file.close()
    return pokedata_orig

def collection_from_get_request():
    url = "http://127.0.0.1:5000/api/v1/collection/"
    payload = {"Owner":"Ash","results_per_page":20}
    headers = {"accept": "application/json"}
    get_request_with_owner = requests.get(url, payload, headers = headers)
    json_response = get_request_with_owner.json()
    return json_response
    # print(json_response)

def add_new_item():
    url = "http://127.0.0.1:5000/api/v1/item/"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    test_item = { "itemName": "TestInsert",
                  "ownerId": "gui test.py",
                  "quantity": 3}
    post_request = requests.post(url, json = test_item, headers = headers)  
    return post_request

def data_scrubbing(input_json):
    displayable_collection_data = []

    print("Orig_data", input_json["response_body"])

    for item in input_json["response_body"]:
        print(";alkjdf")
        item_details = {}
        for key , value in item.items():
            if key == "_id" or key == "lastModified":
                continue
            else:
                item_details[key] = value
        displayable_collection_data.append(item_details)

    print("scrubbed data", displayable_collection_data)

def delete_by_item_name():
    url = "http://127.0.0.1:5000/api/v1/item/delete"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    test_item = { "itemName": "Cup",
                  "ownerId": "Andy"}
    post_request = requests.delete(url, json = test_item, headers = headers)  
    return post_request

def update_item_by_name():
    url = "http://127.0.0.1:5000/api/v1/item/update"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    test_item = { "itemName": "Gorebyss II",
                  "ownerId": "Ash",
                  "quantity": 4}
    post_request = requests.patch(url, json = test_item, headers = headers)  
    return post_request
    

# json = load_from_file()
# json = collection_from_get_request()
# data_scrubbing(json)
# add_new_item()
# delete_by_item_name()
update_item_by_name()

