from datetime import date, timedelta
import os
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import numpy as np

import FinanceDataReader as fdr
from googleapiclient.discovery import build
import market_data as md
from utils import render_today_market, get_latest_video_by_keyword
from render_left_side import render_left_side
from render_right_side import render_right_side

st.set_page_config(layout="wide")

st.title("Good Morning, World!")
st.markdown("---")

col1, col2 = st.columns([1, 1.73])

with col1:
    render_left_side()

with col2:
    render_right_side()