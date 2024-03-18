import streamlit as st

st.title(':red[Moses BMI calculator]')

from PIL import Image
bmi = Image.open("passport.jpg")
st.image(bmi)

st.markdown('What is a BMI')
st.text('BMI is a measurement of a person\'s leanness or \ncorpulence based on their height and weight, \
and is intended to quantify tissue mass.\nIt is widely used as a general indicator of \nwhether a person \
has a healthy body weight \nfor their height. Specifically, the value \nobtained from the calculation of \
BMI is used to categorize \nwhether a person is underweight, normal weight, \noverweight, or obese \
depending on what range the value \nfalls between.\nThese ranges of BMI vary based on factors s')

Weight = st.number_input('Enter weight in (kg)')
status=st.radio('Select your unit format: ',  ('cms', 'Feet', 'meters'))

if (status == 'cms'):
    height = st.number_input('Centimeters')

    try:
        bmi = Weight / ((height / 100) ** 2)

    except:
        st.exception('Enter some value of height')

elif  (status == 'meters'):
    height = st.number_input('meters')

    try:
        bmi = Weight / (height ** 2)

    except:
        st.exception('Enter some value of height')

else:
    height = st.number_input('Feet')

    try:
        bmi = Weight / ((height/3.28) ** 2)

    except:
        st.exception('Enter some value of height')

if (st.button('Calculate BMI')):
    # print the BMI INDEX
    st.text("Your Body Mass Index is {}.".format(bmi))
