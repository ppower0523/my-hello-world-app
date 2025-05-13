import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Request Till Support")
st.header('', divider='rainbow')


df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['Daydif', 'Amount'])
mean_col1 = df['Daydif'].mean()
df = df.groupby(['Daydif']).size().reset_index(name='Amount')
df = df.sort_values('Amount', ascending=False)

st.header("Average Days From Approved To Payment:")
st.header(mean_col1)



#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="Daydif", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(df, hide_index=True, height=400, width=1800)
with col2:
    st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)
