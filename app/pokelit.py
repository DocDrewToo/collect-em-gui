import streamlit as st
import requests as req
import json
import requests
from PIL import Image
import requests
from io import BytesIO
from streamlit.legacy_caching.caching import _hash_func
from streamlit.type_util import Key
from pagination import paginator
from datetime import date
import base64
import json
import os
from datetime import datetime
import pytz
import sys

st.set_page_config(layout="wide")

def list_db_items(json_response):
    # Cleans the data to be displayed in the table
    # Removing items that we don't wish to be displayed
    displayable_collection_data = []
    for item in json_response["response_body"]:
        item_details = {}
        for key , value in item.items():
            if key == "_id" or key == "lastModified":
                continue
            else:
                item_details[key] = value
        displayable_collection_data.append(item_details)
    return displayable_collection_data

        
LOGO_IMAGE = "pokeball.jpg"

st.markdown(
    """
    <style>
    .container {
        display: flex;
    }
    .logo-text {
        font-weight:700 !important;
        font-size:50px !important;
        color: #f9a01b !important;
        padding-top: 75px !important;
    }
    .logo-img {
        float:right;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    f"""
    <div class="container">
        <img class="logo-img" src="data:image/png;base64,{base64.b64encode(open(LOGO_IMAGE, "rb").read()).decode()}" width="150" height="150">
        <p class="logo-text">Catch Em All!</p>
    </div>
    """,
    unsafe_allow_html=True
)

header = st.container() 

features = st.container()
model_training= st.container()
dataset= st.container()

with header: 
    st.title('Welcome to the Catch them all!')
    # st.text('Please enter your pokemon info:')
option = st.selectbox(
     'What would you like to do?',
     ('---Choose an Option---', 'List Items', 'Add Item','Update Item', 'Delete Item'))
    
def delete_by_item_name(test_item):
    url = "http://127.0.0.1:5000/api/v1/item/delete"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    post_request = requests.delete(url, json = test_item, headers = headers)  
    return post_request

def add_new_item(test_item):
    url = "http://127.0.0.1:5000/api/v1/item/"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    post_request = requests.post(url, json = test_item, headers = headers)  
    return post_request

def update_item_by_name(test_item):
    url = "http://127.0.0.1:5000/api/v1/item/update"
    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    post_request = requests.patch(url, json = test_item, headers = headers)  
    return post_request

def collection_from_get_request(user):
    url = "http://127.0.0.1:5000/api/v1/collection/"
    payload = {"Owner":user,"results_per_page":20}
    headers = {"accept": "application/json"}
    get_request_with_owner = requests.get(url, payload, headers = headers)
    json_response = get_request_with_owner.json()
    return json_response

if option == 'List Items':
    user_name_input = st.text_input("User")

if option== 'Add Item' or option=='Delete Item' or option=='Update Item':
    st.header('Item Info:')
    col1, col2, col3 = st.columns(3)
    
    with col1:
        user_name_input = st.text_input("User")
    with col2:
        item_name_input = st.text_input("Item Name")
    if option== 'Add Item' or option=='Update Item':
        with col3:
            quantity_input = st.number_input("Quantity", step=1)
    if option == 'Add Item':
        col4, col5 = st.columns(2)
        with col4:
            new_field_name = st.text_input("New Field Name")
        with col5:
            new_field_value = st.text_input("New Field Value")

if option != '---Choose an Option---' and st.button('Submit') :
    if option== 'List Items':
        collection_json = list_db_items(collection_from_get_request(user_name_input))
        st.dataframe(collection_json)
    elif option =="Add Item":
        test_item={'ownerId': user_name_input,
        'itemName': item_name_input,
        'quantity': quantity_input,
        new_field_name: new_field_value}
        add_new_item(test_item)
        st.write("Added Item: ", item_name_input, "for: ",user_name_input,"!" )
    elif option =="Update Item":
        test_item={'ownerId': user_name_input,
        'itemName': item_name_input,
        'quantity': quantity_input}
        update_item_by_name(test_item)
        st.write("Updated Item", item_name_input, " to new quantity: ", 
        str(quantity_input), "for ",user_name_input,"!" )
    else:
        test_item={'ownerId': user_name_input,
        'itemName': item_name_input}
        delete_by_item_name(test_item)
        # post_request = requests.delete(url, json = test_item, headers = headers)
        st.write("Deleted Item: ", item_name_input, "for: ",user_name_input,"!"  )