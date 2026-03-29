import streamlit as st
st.title("BMI Calculator")

weight=st.number_input("Enter your weight in kg")
status=st.radio("Select your height format:",('cms','meters','feet'))
try:
    if status=='cms':
        height=st.number_input("Enter your height in cms")
        bmi=weight/(height/100)**2
    elif status=='meters':
        height=st.number_input("Enter your height in meters")
        bmi=weight/height**2
    elif status=='feet':
        height=st.number_input("Enter your height in feet")
        bmi=weight/(height/3.28084)**2
except:
    print("zero division error")

if(st.button("Calculate BMI")):
    st.write("Your BMI is: ", round(bmi,2))
    if bmi<18.5:
        st.warning("You are underweight")
    elif bmi>=18.5 and bmi<24.9:
        st.success("You are normal weight")       
    elif bmi>=24.9 and bmi<29.9:
        st.info("You are overweight")
    else:
        st.warning("You are obese")
st.balloons()