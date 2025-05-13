import streamlit as st

import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Remaining Balance")
st.header('Patients With A Remaining Balance', divider='rainbow')


df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['PmtSub_BalMoreThan0_Approved', 'Amount'])
df = df.groupby(['PmtSub_BalMoreThan0_Approved']).size().reset_index(name='Amount')
df = df.sort_values('Amount', ascending=False)





#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="PmtSub_BalMoreThan0_Approved", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(df, hide_index=True, height=400, width=1800)
with col2:
    st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)



##############################################################################################



