import streamlit as st
import requests
import json
from PIL import Image

st.set_page_config(page_title="Star Wars weather Aarhus", page_icon=":flag_denmark:", layout="wide")

st.subheader("Star Wars weather Aarhus")

response = requests.get("https://api.weatherapi.com/v1/current.json?key=36fec4787ae4493db02202139232005&q=Aarhus&aqi=no")

def jprint(obj):
    text = json.dumps(obj, sort_keys=True, indent=4)
    return text

if response.status_code == 200:
    data = response.json()
    text = jprint(data)  # Print the JSON data and get the text variable

elif response.status_code == 404:
    print("Unable to reach URL.")
else:
    print("Unable to connect to API or retrieve data.")

def getdata(text):
    y = json.loads(text)
    temp = y["current"]["temp_c"]
    return temp

if response.status_code == 200:
    temperature = getdata(text)
    if temperature < -10:
        page_bg_img = """
        <style>
        [data-testid="stHeader"] {
        background-image: url("https://lumiere-a.akamaihd.net/v1/images/Hoth_d074d307.jpeg?region=248%2C0%2C900%2C675"):
        background-size: cover;
        }
        </style>
        """
        st.markdown("",unsafe_allow_html=True)
        st.title("Feels like Hoth")
        st.write(str(temperature) + "°C. Weather like on Hoth")
        st.write("Better put on a jacket")
    if -10 <= temperature <= 43:
        page_bg_img = """
        <style>
        [data-testid="stHeader"] {
        background-image: url("data:image/jpeg;base64,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"):
        background-size: cover;
        }
        </style>
        """
        st.markdown("", unsafe_allow_html=True)
        st.title("Feels like Tatooine")
        st.write(str(temperature) + "°C. Tatooine-like weather.")
