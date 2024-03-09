import streamlit as st
import numpy as np
import pickle
import json
import base64
import os
import requests

# Local Checks

# @st.cache_data
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# img = get_img_as_base64(
#     r"C:\Users\91948\Documents\VS Code Files\RealEstate Valuation System\model\Valuation Pic.png"
# )

# def get_img_as_base64(file_url):
#     github_raw_url = file_url.replace("github.com", "raw.githubusercontent.com").replace("/blob/", "/")

#     response = requests.get(github_raw_url)
    
#     if response.status_code == 200:
#         data = response.content
#         return base64.b64encode(data).decode()
#     else:
#         print(f"Failed to fetch the image file. Status code: {response.status_code}")
#         return None

# img_url = "https://github.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/raw/main/model/Valuation%20Pic.png"
# img = get_img_as_base64(img_url)

# For Local Checks

# def load_model():
#     with open(
#         r"C:\Users\91948\Documents\VS Code Files\RealEstate Valuation System\model\House Price Prediction_Pickle.pickle",
#         "rb",
#     ) as f:
#         return pickle.load(f)

# For Deployment

def load_model():
    github_raw_url = "https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/main/model/House%20Price%20Prediction_Pickle.pickle"

    response = requests.get(github_raw_url)
    
    if response.status_code == 200:
        return pickle.loads(response.content)
    else:
        print(f"Failed to fetch the model file. Status code: {response.status_code}")
        return None

# For Local Checks

# def load_prediction_input():
#     with open(
#         r"C:\Users\91948\Documents\VS Code Files\RealEstate Valuation System\model\prediction_input.json",
#         "rb",
#     ) as f:
#         return json.load(f)

# For Deployment

def load_prediction_input():
    github_raw_url = "https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/main/model/prediction_input.json"

    response = requests.get(github_raw_url)
    
    if response.status_code == 200:
        return json.loads(response.content)
    else:
        print(f"Failed to fetch the prediction input file. Status code: {response.status_code}")
        return None

def load_predicted_values(location, bath, bhk, area, all_columns, model):
    column_index = (all_columns).index(location)
    x = [0] * (len(all_columns))
    x[0] = bath
    x[1] = bhk
    x[2] = area
    x[column_index] = 1
    return round(model.predict([x])[0], 0)


model = load_model()
prediction_input = load_prediction_input()

all_columns = prediction_input["all_columns"]
locations = prediction_input["locations"]
bath = prediction_input["bath"]
bhk = prediction_input["bhk"]

image_url = "https://raw.githubusercontent.com/Bharathkumar-Tamilarasu/RealEstate-Valuation-System/main/Valuation%20Pic%201.png"


def show_predict_page():

    # page_bg_img = f"""
    # <style>
    # [data-testid="stAppViewContainer"] > .main {{
    # background-image: url("data:image/png;base64,{img}");
    # background-size: cover;
    # background-position: center;
    # background-repeat: no-repeat;
    # background-attachment: local;
    # }}
    # """
    # st.markdown(page_bg_img, unsafe_allow_html=True)

    st.image(image_url)

    ip_location = st.selectbox("""#### 🌍 Choose a Location""", locations)
    ip_bath = st.radio(
        """#### 🛁 Number of Bathrooms""", [i for i in range(1, 6)], horizontal=True
    )
    ip_bhk = st.radio(
        """#### 🛏️ Number of Bedrooms""", [i for i in range(1, 6)], horizontal=True
    )
    ip_area = st.number_input("""#### 📐 Area Size (in sqft)""", key=int, step=1)
    ip_ok = st.button(
        "Estimate",
    )

    if ip_ok and ip_area > 0:
        predicted_value = load_predicted_values(
            ip_location, ip_bath, ip_bhk, ip_area, all_columns, model
        )
        st.success(
            f"The property's estimated worth is {int(predicted_value)} lakh rupees."
        )
    elif ip_ok and ip_area == 0:
        st.error("Please Enter the Area!")
