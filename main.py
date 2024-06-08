import streamlit as st
import pickle
import numpy as np

pipe = pickle.load(open('..NaiveBayes.pkl','rb'))
df = pickle.load(open('..NaiveBayes.pkl','rb'))

st.title("Crop Suggestion System")

# N
nitrogen = st.number_input('Nitrogen')

# P
phosphorus = st.number_input('Phosphorus')

# K
potassium = st.number_input('Potassium')

# 'tempreature'
tempreature = st.number_input('tempreature in celcius')

# humudity
humidity = st.number_input('humidity')

# ph
ph = st.number_input('ph')

# rainfall
rainfall = st.number_input('rainfall in cm')

if st.button("Predict"):
    query = np.array([[nitrogen,phosphorus,potassium,tempreature,humidity,ph,rainfall]])
    # print(query)
    text = str(pipe.predict(query)[0])
    result = text
    st.title("The crop suggested for this demographic condition is : " + result)
