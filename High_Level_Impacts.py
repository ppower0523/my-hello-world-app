import streamlit as st
import pandas as pd
import numpy as np
import time

st.set_page_config(
    page_title="Multipage App",
    page_icon=":)"
)

st.title("High Level Impacts")     
st.sidebar.success("Select a page above.")

st.markdown("This is some text with markdown")

df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope_UTF_File.csv")
#("https://raw.githubusercontent.com/ppower0523/codespaces-blank/refs/heads/main/Hope_UTF_File.csv?token=GHSAT0AAAAAADCJVTWV54KQ2XNUZ4CU4Y2K2A773VQ")
#("https://raw.githubusercontent.com/ppower0523/codespaces-blank/refs/heads/main/Hope_Text_File.csv.txt?token=GHSAT0AAAAAADCJVTWVMVKVL44HIQO427TM2A77WIA")
#("https://raw.githubusercontent.com/ppower0523/my-hello-world-app/refs/heads/master/TestTestTest")
#('C:\Users\PPowe\Downloads\HopeFoundationData.csv')

st.dataframe(df, height=1500)

#############################################################################################################


import streamlit as st


import plotly.express as px


import streamlit as st
import pandas as pd


#st.write("Average Support Given By Race")
df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['Grant Req Date', 'Amount'])
#df = df.groupby(['Grant Req Date']).size().reset_index(name='Amount')
df.index = pd.to_datetime(df['Grant Req Date'],format='mixed')
df.groupby(by=[df.index.month, df.index.year])
df = df.sort_values('Amount', ascending=False)
#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="Grant Req Date", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)
st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)


#st.write("Average Support Given By Race")
df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['Household Size', 'Amount'])
df = df.groupby(['Household Size']).size().reset_index(name='Amount')
df = df.sort_values('Amount', ascending=False)
#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="Household Size", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(df, hide_index=True, height=400, width=1800)
with col2:
    st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)
 




#b = pd.read_csv('b.dat')
#b.index = pd.to_datetime(b['date'],format='%m/%d/%y %I:%M%p')
#b.groupby(by=[b.index.month, b.index.year])

#Request Status
