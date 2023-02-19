#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import streamlit as st 

# PANDAS DATABASE CREATION
st.set_page_config(
  page_title="Constats Dashboard",
  page_icon=":bar_chart:",
  layout="wide"                 
)

df= pd.read_excel(
      io='Data_constats.xlsx',
      engine='openpyxl',
      sheet_name='Constats_compilation',
      skiprows=3,
      usecols='B:R',
      nrows=1000,
    )


# SIDEBAR
st.sidebar.header("Please Filter Here:")

Etat= st.sidebar.multiselect(
  "Select the state:",
  options=df["Etat constat"].unique(),
  default=df["Etat constat"].unique()
)

Thème= st.sidebar.multiselect(
  "Select the Thème:",
  options=df["Thème"].unique(),
  default=df["Thème"].unique()
)

Lot= st.sidebar.multiselect(
  "Select the Lot:",
  options=df["Lot"].unique(),
  default=df["Lot"].unique()
)

df_selection=df.query(
  "Etat Constat== @Etat & Thème== @Thème & Lot == @Lot"
)

st.dataframe(df_selection)

