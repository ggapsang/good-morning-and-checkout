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

with col1:
    
    # Youtue Link
    st.markdown("#### Youtube Link")

    # # at local env, set GOOGLE_API_KEY in .env file
    # if not os.getenv("GOOGLE_API_KEY"):
    #     load_dotenv()
    # API_KEY = os.getenv("GOOGLE_API_KEY")

    # streamlit cloud
    API_KEY = st.secrets["API_KEY"]

    youtube = build('youtube', 'v3', developerKey=API_KEY)

    channel_id = "UCIipmgxpUxDmPP-ma3Ahvbw" # 매경 월가월부
    search_query = "홍장원의 불앤베어"
    video_search_result = get_latest_video_by_keyword(youtube, channel_id, search_query, is_handle=False)

    if video_search_result :
        st.write(f"{video_search_result['published_at']}")
        st.video(f"{video_search_result['url']}")

    st.markdown("---")