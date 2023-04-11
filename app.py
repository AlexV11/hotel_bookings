import streamlit as st
import pandas as pd
from date_counter import count_weekend_nights
from datetime import datetime
import prediction
from data_frame_selector import DataFrameSelector

st.title('Hotel bookings')

st.sidebar.title('Models')
model = st.sidebar.selectbox(
    'Select model', 
    [
        'Support Vector Machine',
        'Random Forest Classifier',
        'Extra Trees Classifier'
    ]
)
if model == 'Support Vector Machine':
    st.sidebar.info('86.15% accuracy')
elif model == 'Random Forest Classifier':
    st.sidebar.info('90.41% accuracy')
elif model == 'Extra Trees Classifier':
    st.sidebar.info('89.43% accuracy')

c1, c2, c3 = st.columns([1, 1, 1])
type_of_meal = c1.selectbox(
    'Type of meal', 
    [
        'Meal Plan 1',
        'Meal Plan 2',
        'Meal Plan 3',
        'Not selected'
    ]
)
room_type_pre = c2.number_input('Room type', min_value=1, max_value=7)
if room_type_pre == 1:
    room_type = 'Room_Type 1'
elif room_type_pre == 2:
    room_type = 'Room_Type 2'
elif room_type_pre == 3:
    room_type = 'Room_Type 3'
elif room_type_pre == 4:
    room_type = 'Room_Type 4'
elif room_type_pre == 5:
    room_type = 'Room_Type 5'
elif room_type_pre == 6:
    room_type = 'Room_Type 6'
elif room_type_pre == 7:
    room_type = 'Room_Type 7'

parking_space_pre = c3.selectbox(
    'Do you need a parking space?',
    [
        'Yes',
        'No'
    ]
)
if parking_space_pre == 'Yes':
    parking_space = 1
else:
    parking_space = 0

c1, c2 = st.columns([1, 1])
adults = c1.number_input('Number of adults', min_value=1)
children = c2.number_input('Number of children', min_value=0)

c1, c2, c3 = st.columns([1, 1, 1])
arriving_date = c1.date_input('Check-in date')
booking_date = c2.date_input('When did you book the room?')
nights = c3.number_input('Number of nights', min_value=1)

arrival_date = datetime.strptime(str(arriving_date), '%Y-%m-%d')
booking_date = datetime.strptime(str(booking_date), '%Y-%m-%d')
lead_time = arrival_date - booking_date

c1, c2 = st.columns([1, 1])
market_type = c1.selectbox(
    'Market segment', 
    [
        'Online',
        'Offline',
        'Aviation',
        'Complementary',
        'Corporate'
    ],
    key='market_segment'
)
c2.number_input('Lead time', min_value=0, key='lead_time', value = lead_time.days, disabled=True)

c1, c2 = st.columns([1, 1])
previous_cancellations = c1.number_input('Number of previous cancellations', min_value=0, key='previous_cancellations')
not_cancelled = c2.number_input('Number of times didn\'t cancel', min_value=0, key='previous_bookings_not_canceled')
repeated_guest = 0
if not_cancelled > 0 or previous_cancellations > 0:
    repeated_guest = 1

c1, c2 = st.columns([1, 1])
average_price = c1.number_input('Average price', key='average_price', min_value=0.0, max_value=500000.0, step=1.00, format = "%.2f")
special_requests = c2.number_input('Number of special requests', min_value=0, key='special_requests')

weekend_nights = count_weekend_nights(str(arriving_date), nights)
arriving_date2 = str(arriving_date).split('-')
year = arriving_date2[0]
month = arriving_date2[1]
day = arriving_date2[2]
week_nights = nights - weekend_nights

if st.button('Predict'):
    data = pd.DataFrame({
        'no_of_adults': [adults],
        'no_of_children': [children],
        'no_of_weekend_nights': [weekend_nights],
        'no_of_week_nights': [week_nights],
        'type_of_meal_plan': [type_of_meal],
        'required_car_parking_space': [parking_space],
        'room_type_reserved': [room_type],
        'lead_time': [lead_time.days],
        'arrival_year': [year],
        'arrival_month': [month],
        'arrival_date': [day],
        'market_segment_type': [market_type],
        'repeated_guest': [repeated_guest],
        'no_of_previous_cancellations': [previous_cancellations],
        'no_of_previous_bookings_not_canceled': [not_cancelled],
        'avg_price_per_room': [average_price],
        'no_of_special_requests': [special_requests],
        'number_of_days': [nights]
    })

    print(data)
    #preprocessed_data = preprocess.preprocess(data)
    result_raw = prediction.predict(data, model)
    
    if result_raw == 1:
        st.error('It\'s likely that the customer will cancel the reservation')
    else:
        st.success('It\'s likely that the customer will not cancel the reservation')