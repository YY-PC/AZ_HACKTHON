from gettext import Catalog
import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px

#read csv
df = pd.read_csv("./client.csv")
st.set_page_config(
    page_title = 'State Street User Dashboard',
    page_icon = '⛵',
    layout = 'wide'
)

st.title('State Street Client Information')

#job_filter = st.selectbox("Select the Job", pd.unique(df['job']))


# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

#df = df[df['job']==job_filter]

# near real-time / live feed simulation 

for seconds in range(200):
#while True: 
    


    with placeholder.container():
        st.markdown("Assets Summary data view")
        st.dataframe(df)
        time.sleep(1)
    #placeholder.empty()