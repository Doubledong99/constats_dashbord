
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


import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
plt.figure(figsize=(20,10))
ax=sns.countplot(y='Thème',data=df)
ax.set_title('Nombre des constats par Thème')
