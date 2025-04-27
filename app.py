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


st.set_page_config(layout="wide")

st.title("Good Morning, World!")
st.markdown("---")

# Stock Market
st.markdown("#### US Stock Market")

col1, col2, col3, col4, col5 = st.columns(5)

with col1 :
    container = st.container(border=True)
    container.markdown('###### S&P 500')
    render_today_market(md.snp_df, container)

with col2 : 
    container = st.container(border=True)
    container.markdown('###### NASDAQ')
    render_today_market(md.nasdaq_df, container)

with col3 :
    container = st.container(border=True)
    container.markdown('###### Dow')
    render_today_market(md.dji_df, container)

with col4 :
    container = st.container(border=True)
    container.markdown('###### Russell')
    render_today_market(md.rut_df, container)

with col5 :
    container = st.container(border=True)
    container.markdown('###### VIX')
    render_today_market(md.vix_df, container)

st.markdown("---")

# Exchange Rate
st.markdown("#### Exchange Rate")
col1, col2, col3, col4 = st.columns(4)

with col1 :
    container = st.container(border=True)
    container.markdown('###### USD Index')
    render_today_market(md.usd_idx_df, container)

with col2 :
    container = st.container(border=True)
    container.markdown('###### USD/KRW')
    render_today_market(md.usd_kr_df, container)

with col3 :
    container = st.container(border=True)
    container.markdown('###### EUR/KRW')
    render_today_market(md.eur_kr_df, container)

with col4 :
    container = st.container(border=True)
    container.markdown('###### JPY/KRW')
    render_today_market(md.jpy_kr_df, container, jpy_100=True)

st.markdown("---")


# Bond, Gold
st.markdown("#### Bond and Gold")
col1, col2 = st.columns(2)

with col1 :
    container = st.container(border=True)
    container.markdown('###### 10Y US Treasury')
    render_today_market(fdr.DataReader('^TNX'), container)

with col2 :
    container = st.container(border=True)
    container.markdown('###### Gold')
    render_today_market(fdr.DataReader('GC=F'), container)

st.markdown("---")


# Youtue Link
st.markdown("#### Youtube Link")

# at local env, set GOOGLE_API_KEY in .env file
if not os.getenv("GOOGLE_API_KEY"):
    load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

# # streamlit cloud
# API_KEY = st.secrets["API_KEY"]

youtube = build('youtube', 'v3', developerKey=API_KEY)

channel_id = "UCIipmgxpUxDmPP-ma3Ahvbw" # 매경 월가월부
search_query = "홍장원의 불앤베어"
video_search_result = get_latest_video_by_keyword(youtube, channel_id, search_query, is_handle=False)

if video_search_result :
    st.write(f"{video_search_result['published_at']}")
    st.video(f"{video_search_result['url']}")

st.markdown("---")