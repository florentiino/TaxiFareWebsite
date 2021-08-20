import streamlit as st
import requests
import datetime
import pandas as pd
import numpy as np

day = st.sidebar.date_input(
    "When's your pick up date?",
    datetime.date(2019, 7, 6))

pickup_lon = st.sidebar.slider('Pickup Lon', 0, 950000)
pickup_lat = st.sidebar.slider('Pickup Lat', 0, 950000)

dropoff_lon = st.sidebar.slider('Dropoff Lon', 0, 950000)
dropoff_lat = st.sidebar.slider('Dropoff Lat', 0, 950000)

people = st.sidebar.selectbox(
    'How many people?',
    (1, 2, 3))



url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={day}%2017:18:00&pickup_longitude=-73.{pickup_lon}&pickup_latitude=40.{pickup_lat}&dropoff_longitude=-73.{dropoff_lon}&dropoff_latitude=40.{dropoff_lat}&passenger_count={people}'
st.write(f'{url}')
response = requests.get(url, params='prediction')
jsonResponse = response.json()
st.write(f'It is going to be {int(jsonResponse["prediction"])} Bucks')

df = pd.DataFrame({'lat': [pickup_lat, dropoff_lat],
                  'lon': [pickup_lon, dropoff_lon]})
st.map(df)

