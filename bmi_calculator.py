import streamlit as st
import numpy as np

st.title('Body Mass Index Advisor for Indians 🇮🇳')
st.write('Traditional BMI ranges do not apply to people of Indian ethnicity. This calculator uses the revised guidelines for India.')
st.markdown("***")

st.write('**Enter height**')
ft_selector = st.selectbox('ft', options=[0, 1, 2, 3, 4, 5, 6, 7, 8])
in_selector = st.selectbox('in', options=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])



if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True

if 'bmi_color_dict' not in st.session_state:
    st.session_state.bmi_color_dict = {'Underweight':'blue', 'Normal':'green', 'Overweight':'orange', 'Obese':'red'}

submit_height_button = st.button('Submit Height', on_click=click_button)

if st.session_state.clicked:
    height_m = (ft_selector*12 + in_selector)*2.54/100
    st.markdown("***")


    if height_m != 0:
        text_placeholder = st.empty()
        st.write('')
        st.write('**Select weight**')
        initial_weight = np.round(((21*height_m**2)*2)/2)
        kg_selector = st.slider('kg', min_value=20., max_value=150., step=0.5, value=initial_weight, key='kg_selector')
        bmi = np.round(st.session_state.kg_selector/(height_m**2), 1)

        if bmi < 18.5:
            bmi_category = 'Underweight'
        if bmi >= 18.5 and bmi < 23:
            bmi_category = 'Normal'
        if bmi >= 23 and bmi < 25:
            bmi_category = 'Overweight'            
        if bmi >= 25:
            bmi_category = 'Obese'

        bmi_text_color = st.session_state.bmi_color_dict[bmi_category]
        text_placeholder.write(f":{bmi_text_color}[**BMI: {bmi} - {bmi_category}**]")

