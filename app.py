import requests
import streamlit as st
from PIL import Image
import pandas as pd

st.set_page_config(page_title="NFT SALES DASHBOARD",page_icon=":bar_chart:",layout="wide")

df = pd.read_csv("https://raw.githubusercontent.com/PULI-GOKULA-KISHORE-REDDY/IBM-HACK-CHALLENGE/main/files/datasets/day_aqi_list_140000.csv")

st.sidebar.header("Please Filter Here:")

year = st.sidebar.multiselect(
    "Select the year:",
    options=df["Date"].unique(),
    default=df["Date"].unique()
)

st.title(":cyclone: NFT Sales Dashboard")
st.markdown("##")

Locations =df.count()
Average_AQI = df['AQI'].mean()


left_co, right_co = st.columns(2)
with left_co:
    st.subheader("Total Locations:")
    st.subheader(f"{Locations:,}")
with right_co:
    st.subheader("Average_AQI")
    st.subheader(f"{Average_AQI:,}")
st.markdown("---")
