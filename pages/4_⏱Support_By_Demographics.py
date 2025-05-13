import streamlit as st




import streamlit as st
import pandas as pd

st.title("Support By Demographics")
st.header('Average Support by Demographic', divider='rainbow')




#df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope_UTF_File.csv")
#st.dataframe(df)
#st.line_chart(df)
#st.bar_chart(df, x="Race", y="Amount")

import streamlit as st
import pandas as pd
import plotly.express as px

#st.write("Average Support Given By Race")
df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['Race', 'Amount'])
df = df.groupby(['Race']).size().reset_index(name='Amount')
df = df.sort_values('Amount', ascending=False)
#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="Race", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    st.dataframe(df, hide_index=True, height=400, width=1800)
with col2:
    st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)





#st.write("Average Support Given By Insurance Type")
df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['Insurance Type', 'Amount'])
df = df.groupby(['Insurance Type']).size().reset_index(name='Amount')
df = df.sort_values('Amount', ascending=False)
#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="Insurance Type", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)


#########################################################################################################################



#st.subheader("st.column")
col1, col2 = st.columns(2)

with col1:
    st.dataframe(df, hide_index=True, height=400, width=1800)
with col2:
    st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)



#########################################################################################################################


df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['Gender', 'Amount'])
df = df.groupby(['Gender']).size().reset_index(name='Amount')
df = df.sort_values('Amount', ascending=False)



#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="Gender", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)

with col1:
    st.dataframe(df, hide_index=True, height=400, width=1800)
with col2:
    st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)


###########################################################################################################################






df = pd.read_csv("https://github.com/ppower0523/my-hello-world-app/raw/refs/heads/master/Hope%20UTF%2020250511_1356.csv")
df = df.filter(items = ['Total Household Gross Monthly Income', 'Amount'])
df = df.groupby(['Total Household Gross Monthly Income']).size().reset_index(name='Amount')
df = df.sort_values('Amount', ascending=False)



#st.dataframe(df, hide_index=True, height=400, width=1800)
fig = px.bar(df, x="Total Household Gross Monthly Income", y="Amount") 
#st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)


st.plotly_chart(fig, theme="streamlit", orientation='h', use_container_width=True)
