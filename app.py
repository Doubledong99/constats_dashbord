
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

df=pd.read_csv('data.csv', sep=';' ,encoding='latin-1')
st.dataframe(df)


import plotly.express as px

constats_par_thème=(
  df.groupby(by=["Thème"]).count()
)

fig_product_sales = px.bar(
    constats_par_thème,
    x="Total",
    y=constats_par_thème.index,
    orientation="h",
    title="<b>Sales by Product Line</b>",
    color_discrete_sequence=["#205295"] * len(constats_par_thème),
    template="plotly_white",
)

fig_product_sales.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)
