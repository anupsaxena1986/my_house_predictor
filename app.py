import streamlit as st
import numpy as np
import pickle
with open("house_model.pkl","rb") as file:
    model =pickle.load(file)
st.set_page_config(page_title ="House Price Predictor", page_icon="Home",layout ="centered")
st.title("House prediction app")
st.write("Please enter details of house and get predicted price of house")
st.markdown("----")
area = st.number_input("Area in square feet:",min_value = 100, max_value = 20000, value =3000)
col1,col2,col3 = st.columns(3)
with col1:
    bedrooms = st.slider("Number of bedrooms:",min_value = 1, max_value= 6, value= 3)
with col2:
    bathrooms = st.slider("Number of bothroom:", min_value =1, max_value =5, value =2)
with col3:
    stories = st.slider("Number of stories:", min_value = 1, max_value =4 ,value =2)
parking = st.slider("Place of parking(Number of vehicle)",min_value = 0, max_value =4, value=1)
st.markdown("Other facilities")
mainroad = st.checkbox("Is house at the Main road?")
guestroom = st.checkbox("Is guest room Available")
basement = st.checkbox("Is basement Available")
hotwaterheating = st.checkbox("Is hotwater heating Available")
airconditioning = st.checkbox("Is Airconditioning Available")
prefarea = st.checkbox("Is This preferred  Area")
st.markdown("Furnishing status")
furnishing = st.selectbox("Select house status:",["Fully furnished","Semi furnished", "Unfurnished"])
mainroad_yes = 1 if mainroad else 0
guestroom_yes = 1 if guestroom else 0
basement_yes = 1 if basement else 0 
hotwaterheating_yes = 1 if hotwaterheating else 0
airconditioning_yes = 1 if airconditioning else 0
prefarea_yes = 1 if prefarea else 0
furnishingstatus_semi_furnished = 1 if furnishing == "semi-furnished" else 0
furnishingstatus_unfurnished = 1 if furnishing == "Unfurnished" else 0
st.markdown("----")
if st.button("Predict Price"):
    features = np.array([[area, bedrooms, bathrooms,stories, parking,mainroad_yes, guestroom_yes,basement_yes,hotwaterheating_yes,airconditioning_yes, prefarea_yes,furnishingstatus_semi_furnished,furnishingstatus_unfurnished]])
    prediction = model.predict(features)[0]
    st.success(f"predicted price of this house is:{prediction:.2f}")