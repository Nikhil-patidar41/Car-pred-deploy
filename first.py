import streamlit as st
import pickle as p
import pandas as pd
import numpy as np

# Load Model
st.title("Car Price Prediction App")

model_path = "LinearRegressionModel.pkl"
model = p.load(open(model_path, 'rb'))

# User Inputs
f_fn = st.text_input("Enter car name")  # Not used in prediction but kept for UI
f_fc = st.text_input("Enter car company")
f_fy = st.number_input("Enter car year", min_value=1900, max_value=2025, step=1)
f_fkm = st.number_input("Enter car km driven", min_value=0, step=100)
f_ff = st.text_input("Enter car fuel type")

# Ensure all inputs are valid
if st.button("Predict Price"):
    # Creating DataFrame for model prediction
    input_p_f = pd.DataFrame([[f_fn, f_fc, f_fy, f_fkm, f_ff]], columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    # input_p_f = pd.DataFrame(np.array([f_fn, f_fc, f_fy, f_fkm, f_ff]).reshape(1,5), columns=['name', 'company', 'year', 'kms_driven', 'fuel_type'])
    # Model Prediction
    r = model.predict(input_p_f)
    # Display Result
    st.write(f"Predicted Price: ₹{r}")



# python -m streamlit run first.py