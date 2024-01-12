import numpy as np
import pandas as pd
import json
import requests
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(
    layout="wide",
)


def loading_data():
    data = requests.get("http://127.0.0.1:8000/trends").json()
    data_df = pd.read_json(data)

    return data_df


data = loading_data()
plt.figure(figsize=(20, 20))
fig, ax = plt.subplots()
ax.pie(
    data["sentiment"].value_counts().values,
    labels=data["sentiment"].value_counts().index,
)
st.pyplot(fig=fig)

fig2, ax = plt.subplots()
ax.pie(
    data["entity"].value_counts().values,
    labels=data["entity"].value_counts().index,
)
st.pyplot(fig=fig2)
