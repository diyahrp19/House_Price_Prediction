import streamlit as st
import pickle

model = pickle.load(open("model.pkl", "rb"))

st.title("House Price Prediction")

size = st.number_input("Enter House Size (sqft)", min_value=100, max_value=10000, value=500)

if st.button("Predict"):
    prediction = model.predict([[size]])[0]
    st.success(f"Estimated Price: ₹ {round(prediction, 2)}")