from gettext import Catalog
import streamlit as st
import numpy as np
import pandas as pd
import time
import plotly.express as px
import recommendation as r
import pyodbc
from  PIL import Image

SERVER='azure-sql-db-server-ptlib.database.windows.net'
DATABASE='sql-db-ptlib'
USERNAME='azureuser'
PASSWORD='AZpwd123123123'

connectionString = f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={SERVER};DATABASE={DATABASE};UID={USERNAME};PWD={PASSWORD}'
# conn = pyodbc.connect(connectionString) 



#read csv
df = pd.read_csv("./client.csv")
transdata = pd.read_csv("./transaction.csv")

# im = Image.open("./sslogo.png")
st.set_page_config(
    page_title = 'State Street FGSP',
    page_icon = '⛵',
    layout = 'wide'
)

st.title('State Street Client Information')

#job_filter = st.selectbox("Select the Job", pd.unique(df['job']))
selectCol1, selectCol2 = st.columns(2)
with selectCol1:
    demission = st.selectbox("Dimension", pd.unique(df.columns))
with selectCol2:
    clientId = st.selectbox("Client", pd.unique(df['clientId']))
placeholder = st.empty()

# dataframe filter 

#df = df[df['job']==job_filter]

# near real-time / live feed simulation 


# cursor = conn.cursor()
# cursor.execute('select client, t_bis_mon, ts_amt  from dbo.trancation_data')    
# records = cursor.fetchall()

#transdata=pd.DataFrame(records)
#transdata.columns=transdata.keys()

# col1 = [];
# col2 = [];
# col3 = [];
# for row in records:
#     print(f'{row[0]} == {clientId}')
#     print(row[0] == clientId)
#     if row[0].strip() == clientId:
#         col1.append(row[0].strip());
#         col2.append(row[1].strip());
#         col3.append(row[2].strip());
# transdata=pd.DataFrame(
#     {'clientId': col1, 'bis_mon': col2, 'trans_amt': col3},
#     columns=['clientId', 'bis_mon', 'trans_amt']
# )
# print(transdata)

click = st.button('Get Recommendations')


clientTransData = transdata[transdata['client']==clientId]

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

        
        fig_col3, fig_col4 = st.columns(2)
        with fig_col3:
            st.dataframe(clientTransData)
        with fig_col4:
            st.markdown("Monthly Transaction: ")
            st.line_chart(clientTransData, y='ts_amt', x = 't_bis_mon')

                
        if click:
                with st.spinner('Recommending...'):
                    df_train = r.get_data()
                    for clientId in df['clientId']:
                        st.write(clientId, ' is recommended: ',
                                r.recommend(clientId, r.df_mb(df_train),r.mixed_recommend(clientId, df_train, r.df_mb(df_train))))
        
        time.sleep(1)
    #placeholder.empty()
