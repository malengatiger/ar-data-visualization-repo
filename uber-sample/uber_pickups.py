import streamlit as st
import pandas as pd
import numpy as np
st.title('Uber Pickups - New York City')
st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40],
    'third column': [1000, 2000, 3000, 40000]
}))
DATE_COLUMN = 'date/time'
DATA_URL = ('https://s3-us-west-2.amazonaws.com/'
            'streamlit-demo-data/uber-raw-data-sep14.csv.gz')

@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    def lowercase(x): return str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data


# Create a text element and let the reader know the data is loading.
data_load_state = st.text(' 🔵 Loading data...  🔵 🔵 🔵 🔵 🔵 🔵 🔵')
# Load 10,000 rows of data into the dataframe.
data = load_data(10000)
# Notify the reader that the data was successfully loaded.
data_load_state.text('🔆 Loading data...done! 🔆 🔆 🔆 🔆 🔆 ')
st.write('🧡 💛 💚 Done! (using st.cache) 🧡 💛 💚')
st.subheader(' 🔴 🔴 Raw data will be listed hereunder  🔴 🔴')
st.write(data)
