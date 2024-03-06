import streamlit as st
import numpy as np
import pickle
import json
import base64
import os

# @st.cache_data
# def get_img_as_base64(file):
#     with open(file, "rb") as f:
#         data = f.read()
#     return base64.b64encode(data).decode()


# img = get_img_as_base64(
#     r"C:\Users\91948\Documents\VS Code Files\RealEstate Valuation System\model\Valuation Pic.png"
# )

# For Local Checks (Using Relative paths)

# def load_model():
#     with open(
#         r"C:\Users\91948\Documents\VS Code Files\RealEstate Valuation System\model\House Price Prediction_Pickle.pickle",
#         "rb",
#     ) as f:
#         return pickle.load(f)

# For Deployment (Using Abosulte path)

def load_model():
    root_directory = os.path.dirname(__file__)
    file_path = os.path.join(root_directory, "model", "House Price Prediction_Pickle.pickle")

    try:
        with open(file_path, "rb") as f:
            return pickle.load(f)
    except Exception as e:
        print(f"Error loading model: {e}")
        return None

# For Local Checks (Using Relative paths)

# def load_prediction_input():
#     with open(
#         r"C:\Users\91948\Documents\VS Code Files\RealEstate Valuation System\model\prediction_input.json",
#         "rb",
#     ) as f:
#         return json.load(f)

# For Deployment (Using Abosulte path)

def load_prediction_input():
    root_directory = os.path.dirname(__file__)
    file_path = os.path.join(root_directory, "model", "model/prediction_input.json")

    try:
        with open(file_path, "rb") as f:
            return json.load(f)
    except Exception as e:
        print(f"Error loading model: {e}")
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

    st.title("RealEstate Valuation System")
    st.write("""### Provide input for the prediction""")

    ip_location = st.selectbox("Choose a Location", locations)
    ip_bath = st.radio("Number of Bathrooms", [i for i in range(1, 6)], horizontal=True)
    ip_bhk = st.radio("Number of Bedrooms", [i for i in range(1, 6)], horizontal=True)
    ip_area = st.number_input("Area (in sqft)", key=int, step=1)
    ip_ok = st.button(
        "Estimate",
    )

    if ip_ok and ip_area > 0:
        predicted_value = load_predicted_values(
            ip_location, ip_bath, ip_bhk, ip_area, all_columns, model
        )
        st.subheader(
            f"The property's estimated worth is {int(predicted_value)} lakh rupees."
        )
    elif ip_ok and ip_area == 0:
        st.markdown(
            """<p style='color: red;'>Please Enter the Area!!</p>""",
            unsafe_allow_html=True,
        )
