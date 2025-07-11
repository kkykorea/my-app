# app.py
import streamlit as st
from datetime import datetime
import time

st.set_page_config(page_title="네이버 시계", page_icon="🕒", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; font-size: 64px;'>🕒 네이버 시계</h1>
    <p style='text-align: center; font-size: 18px;'>실시간 디지털 시계</p>
    """,
    unsafe_allow_html=True
)

# 스타일을 위한 CSS
st.markdown(
    """
    <style>
    .clock-box {
        font-size: 80px;
        font-weight: bold;
        text-align: center;
        color: #2c3e50;
        padding: 20px;
        border: 3px solid #2c3e50;
        border-radius: 15px;
        background-color: #ecf0f1;
        width: 100%;
        margin-top: 20px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# 시계 표시
clock_placeholder = st.empty()

while True:
    now = datetime.now().strftime("%H:%M:%S")
    clock_placeholder.markdown(f"<div class='clock-box'>{now}</div>", unsafe_allow_html=True)
    time.sleep(1)
