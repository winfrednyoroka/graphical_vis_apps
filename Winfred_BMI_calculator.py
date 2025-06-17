import streamlit as st
import math

with st.sidebar:
	user = st.text_input('Enter your name here','type here')

st.info('Winfred BMI_calc and Classifier')

# Step 1, ask the user to enter weight in Kgs

weight = st.number_input('Please enter your weight in Kgs')

# Step 2, ask the user to enter their height
height = st.number_input('Please enter your height in cms, metres or feet and inches')

# Step 3, ask the user to choose units of height measurement

unit = st.radio('Please select the units of the height',['cms','metres','feet'])
st.write(unit)

# Actual calculation

# BMI = weight/height**2
# st.text('Your BMI is {}'.format(BMI))

if unit=='cms':

	try:
		BMI = weight/(height/100)**2
	except:
		st.text('The entries must be integers')
elif unit=='metres':
	try:
		BMI = weight/height**2
	except:
		exp=ZeroDivisionError('Dividing by zero check that height is not zero')
		st.exception(exp)

else:
	BMI = weight/(height*0.3048)**2
	


# Provide proper interpretation
button =st.button('Calculate my BMI')
if button:
	st.text('The BMI of {} is {} Kg/m2'.format(user,BMI))

	if (BMI < 16):
		st.error('You are extremely underweight you need to gain some weight')
	elif (BMI >=16 and BMI<18):
		st.warning('You are underweight')
	elif BMI >=18.5 and BMI<=25:
		st.success('Your BMI is normal')
	elif BMI >25 and BMI<=30:
		st.warning('You are overweight')
	elif BMI >30 and BMI<=35:
		st.warning('You are obese')
	elif BMI >35:
		st.error('You are extremely obese watch your weight to be safe')








