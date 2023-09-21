from gettext import Catalog
import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
import pyodbc
from  PIL import Image

SERVER='azure-sql-db-server-ptlib.database.windows.net'
DATABASE='sql-db-ptlib'
USERNAME='azureuser'
PASSWORD='AZpwd123123123'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
#conn = pyodbc.connect(connectionString)

#cursor = conn.cursor()


#read csv
df = pd.read_csv("./client.csv")
im = Image.open("sslogo.png")
st.set_page_config(
    page_title = 'State Street FGSP',
    page_icon = im,
    layout = 'wide'
)

st.title('State Street Client Information')

#job_filter = st.selectbox("Select the Job", pd.unique(df['job']))
demission = st.selectbox("Dimension", pd.unique(df.columns))

# creating a single-element container.
placeholder = st.empty()

# dataframe filter 

#df = df[df['job']==job_filter]

# near real-time / live feed simulation 

#cursor = conn.cursor()
#cursor.execute('select * from dbo.test_tb')
#records = cursor.fetchall()
#for r in records:
#    st.write(f"{r[0]} has a : {r[1]}")

for seconds in range(200):
#while True: 
    


    with placeholder.container():
        st.header("Assets Summary data view")
        fig_col1, fig_col2 = st.columns(2)
        with fig_col1:
            st.dataframe(df)
        with fig_col2:
            st.markdown("Pie Chart: " + demission)
            scale_count = df[demission].value_counts()
            scale_count = pd.DataFrame({demission: scale_count.index, "count": scale_count.values})
            fig = px.pie(scale_count, values = 'count', names = demission)
            st.write(fig)
        
        

        time.sleep(1)
    #placeholder.empty()
