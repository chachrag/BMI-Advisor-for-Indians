import streamlit as st
import numpy as np
# from calc_h_m import *


st.write('**Enter height**')
ft_selector = st.number_input('ft', min_value=0, max_value=10, step=1)
in_selector = st.number_input('in', min_value=0, max_value=11, step=1)



if 'clicked' not in st.session_state:
    st.session_state.clicked = False


def click_button():
    st.session_state.clicked = True



submit_height_button = st.button('Submit Height', on_click=click_button)

if st.session_state.clicked:
    # height_m = calc_height_m(ft_selector, in_selector)
    height_m = (h_ft*12 + h_in)*2.54/100
    # (ft_selector*12 + in_selector)*2.54/100
    st.markdown("***")
    st.write('**Enter weight**')
    initial_weight = np.round(((21*height_m**2)*2)/2)
    kg_selector = st.slider('kg', min_value=0., max_value=200., step=0.5, value=initial_weight)
    if height_m != 0:
        bmi = np.round(kg_selector/(height_m**2), 1)
        st.write(f'**BMI = {bmi}**')



