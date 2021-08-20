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

pickup_lon = f'-73.{pickup_lon}'
dropoff_lon = f'-73.{dropoff_lon}'

pickup_lat = f'40.{pickup_lat}'
dropoff_lat = f'40.{dropoff_lat}'

people = st.sidebar.selectbox(
    'How many people?',
    (1, 2, 3))



url = f'https://taxifare.lewagon.ai/predict?pickup_datetime={day}%2017:18:00&pickup_longitude={pickup_lon}&pickup_latitude={pickup_lat}&dropoff_longitude={dropoff_lon}&dropoff_latitude={dropoff_lat}&passenger_count={people}'
st.write(f'{url}')
response = requests.get(url, params='prediction')
jsonResponse = response.json()
st.write(f'It is going to be {int(jsonResponse["prediction"])} Bucks')

df = pd.DataFrame({'lon': [float(pickup_lon), float(dropoff_lon)],
                   'lat': [float(pickup_lat), float(dropoff_lat)]})
st.map(df)

