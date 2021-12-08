import streamlit as st
import requests
import json
from PIL import Image
import requests
from io import BytesIO
from streamlit.legacy_caching.caching import _hash_func
from streamlit.type_util import Key
from pagination import paginator
from datetime import date
import base64
st.set_page_config(layout="wide")
collection_api_url = "http://127.0.0.1:5000/api/v1/collection/"
item_api_url = "http://127.0.0.1:5000/api/v1/item/"

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
        <p class="logo-text">Collect 'Em All!</p>
    </div>
    """,
    unsafe_allow_html=True
)

header = st.container() 
dataset= st.container()
features = st.container()
model_training= st.container()
col1, col2, col3  = st.columns(3)
flight_list=st.container()

# with header: 
#     st.title('Welcome to the Collect them all!')


# Before we can display or add any data 
# we need to know the owner of the collection
owner = st.text_input("Please enter your name (owner of the collection)", "Ash")
st.button("Search", key=5)
# Get the data to be displayed in the table
payload = {"Owner":owner,"results_per_page":20}
headers = {"accept": "application/json"}
get_request_with_owner = requests.get(collection_api_url, payload, headers = headers)
json_response = get_request_with_owner.json()


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

with st.expander("Collection List"):
    st.header('Collection Info:')
    st.dataframe(displayable_collection_data)


st.header('Add New Items:')
st.text('Please enter your itme info:')
item_name_field = st.empty()
item_name_txt = item_name_field.text_input("Item Name *Required",key = 0)
item_quantity_field = st.empty()
item_quantity = item_quantity_field.number_input("Item Quantity *Required", min_value = 0, step = 1, key = 1)

custom_field_name = st.empty()
custom_field_name_txt = custom_field_name.text_input("Custom Field *Optional", key=3)
custom_field_value = st.empty()
custom_field_value_txt = custom_field_value.text_input("Custom Field Value *Optional", key=4)

add_button_clicked = st.button("Add", key=2)

if add_button_clicked:

    headers = {"accept": "application/json", 
    "Content-Type": "application/json"}
    print("Adding ITem")
    if custom_field_name_txt > " ":
        print("Name",custom_field_name_txt)
        item_to_add = { "itemName": item_name_txt,
                    "quantity": item_quantity,
                    "ownerId": owner,
                    custom_field_name_txt: custom_field_value_txt
        }
    else:
        item_to_add = { "itemName": item_name_txt,
            "quantity": item_quantity,
            "ownerId": owner
        }
    post_request = requests.post(item_api_url, json = item_to_add, headers = headers)  

    # Clear entered values:
    item_name_field.text_input("Item Name")
    item_quantity_field.number_input("Item Quantity", min_value = 0, step = 1)
    custom_field_name.text_input("Custom Name")
    custom_field_value.text_input("Value")

# icon("search")
# selected = st.text_input("", "Search...")
# button_clicked = st.button("OK")
