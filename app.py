import streamlit as st

import requests

import os

def main():
    st.title("Dodgy Weather App")
    api_key = os.environ['api_key']
    location = st.text_input('select your location', 'lisbon')
    # input("What location would you like the current weather for: ")
    request_string = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    weather_result = requests.get(request_string)
    weather_result = weather_result.json()
    st.json(weather_result)

if __name__ == "__main__":
    main()
