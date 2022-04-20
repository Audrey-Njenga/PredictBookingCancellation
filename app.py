import streamlit as st
import pandas as pd
import pickle

model = pickle.load(open('prediction_model.sav','rb'))
st.title('Predict booking cancellation')
st.write("""
 ##### This application helps you predict whether a booking will be cancelled or not based on the features that correlate highest to cancellation
""")

lead = st.number_input('Enter lead time', min_value=0, max_value=800)
st.markdown("""---""")
requests = st.number_input('Enter number of special requests', min_value=0, max_value=5)
st.markdown("""---""")
parking = st.number_input('Enter number of required parking spaces', min_value=0, max_value=8)
st.markdown("""---""")
changes = st.number_input('Enter number of booking changes', min_value=0, max_value=21)
st.markdown("""---""")
adults = st.number_input('Enter number of adults', min_value=1, max_value=55)
st.markdown("""---""")
option = st.selectbox('Are they a repeated guest?', ('Yes', 'No'))
st.markdown("""---""")
waiting = st.number_input('Enter number of days in waiting list', min_value=0, max_value=400)


run = st.button('run')
if run:
    if option == 'Yes':
        opt = 1
    else:
        opt = 0
    fd = pd.DataFrame( columns =['index', 'adults', 'required_parking_spaces', 'days_in_waiting_list', 'booking_changes', 'lead_time', 'is_repeated_guest', 'total_of_special_requests'])
    fd.loc[-1] = [0,adults, parking, waiting, changes, lead, opt, requests]
    fd.index = fd.index + 1  
    fd = fd.sort_index()
    pred = model.predict(fd.iloc[0].values.reshape(1,-1))
    if pred > 1:
        st.write("""

        ## Predicted Cancellation: Yes
        """)
    else:
        st.write("""

        ## Predicted Cancellation: No
        """)