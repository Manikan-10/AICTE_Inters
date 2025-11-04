import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("⚡ EV Range Prediction Demo")

df = pd.read_csv("../data/ev_data.csv")
st.write("### EV Dataset Preview")
st.dataframe(df.head())

X = df[['Efficiency_WhKm','TopSpeed_KmH','Seats']]
y = df['Range_Km']

model = LinearRegression().fit(X, y)

eff = st.slider("Efficiency (Wh/km)", 100, 400, 200)
speed = st.slider("Top Speed (km/h)", 80, 250, 150)
seats = st.slider("Seats", 2, 7, 5)

prediction = model.predict([[eff, speed, seats]])[0]

st.success(f"Estimated Driving Range: **{prediction:.2f} km**")
