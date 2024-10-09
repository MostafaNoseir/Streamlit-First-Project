# Import Libraries
import streamlit as st 
import pandas as pd 
import numpy as np 
import plotly.express as px


st.set_page_config(page_title="Tips dashboard",
                   page_icon=None,
                   layout="wide",  # to fill screen
                   initial_sidebar_state="expanded")


# Import dataset
df = pd.read_csv("tips.csv")
st.write("Hello")

# Sidebar
st.sidebar.header("Tips Dashboard")

st.sidebar.image("C:/Users/User/Pictures/Saved Pictures/positive_smileicon_emoticon_positivo_1553.png")

st.sidebar.write('This Dashboard is using tips dataset from seaborn')
st.sidebar.write('')

st.sidebar.markdown('made with :heart_eyes: by ENG. [Mostafa](http://localhost:8502)')
st.sidebar.write('')

# Body
st.sidebar.write('filter your data')

colr_filt = st.sidebar.selectbox("Color filters", [None,"sex","smoker","day","time"])
size_filt = st.sidebar.selectbox("Size filters", [None,"tip","total_bill"])
row_filt = st.sidebar.selectbox("row filters", [None,"sex","smoker","day","time"])
col_filt = st.sidebar.selectbox("column filters", [None,"sex","smoker","day","time"])


a1,a2,a3,a4 = st.columns(4)  # to make them in same row
a1.metric("max total Bill", df["total_bill"].max())
a2.metric("min total Bill", df["total_bill"].min())
a3.metric("max tip", df["tip"].max())
a4.metric("min tip", df["tip"].min())
st.sidebar.write('')

fig = px.scatter(data_frame=df, x="total_bill", y="tip",
                 color=colr_filt,  # color must be categorical
                 size=size_filt,  # size -> must be numerical
                 facet_col=col_filt,
                 facet_row=row_filt)
st.plotly_chart(fig, use_container_width=True)  # use_container_width=True -> to make this with customizable to screen

c1, c2, c3 = st.columns((4,3,3))
# fisr column take '40%' , second and third take '30%' from row
with c1:
    st.text("Sex vs. Total Bills")
    fig = px.bar(data_frame=df, x="sex", y="total_bill",
                 color=colr_filt)
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.text("Smoker vs. Tips")
    fig = px.pie(data_frame=df, names="smoker", values="tip",
                 color=colr_filt)
    st.plotly_chart(fig, use_container_width=True)
with c3:
    st.text("Day vs. Tips")
    fig = px.pie(data_frame=df, names="day", values="tip",
                 color=colr_filt,
                 hole=0.3)
    st.plotly_chart(fig, use_container_width=True)