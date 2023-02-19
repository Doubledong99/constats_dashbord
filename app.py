
import pandas as pd
import streamlit as st 

# PANDAS DATABASE CREATION
st.set_page_config(
  page_title="Constats Dashboard",
  page_icon=":bar_chart:",
  layout="wide"                 
)

# MAINPAGE
st.title(":bar_chart: Constats Dashboard")
st.markdown("##")

df=pd.read_csv("data.csv")
st.dataframe(df)
