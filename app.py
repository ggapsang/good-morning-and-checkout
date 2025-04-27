from datetime import date, timedelta
import os
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import numpy as np

import FinanceDataReader as fdr
from googleapiclient.discovery import build
from utils import render_today_market, get_latest_video_by_keyword

date_today = date.today()   
date_yesterday = date.today() - timedelta(days=1)
date_string_today = date_today.strftime("%Y-%m-%d")
date_string_yesterday = date_yesterday.strftime(("%Y-%m-%d"))

# US market Indices
nasdaq_df = fdr.DataReader('IXIC').sort_index(ascending=False).head(2)
snp_df = fdr.DataReader('S&P500').sort_index(ascending=False).head(2)
dji_df = fdr.DataReader('DJI').sort_index(ascending=False).head(2)
rut_df = fdr.DataReader('RUT').sort_index(ascending=False).head(2)
vix_df = fdr.DataReader('VIX').sort_index(ascending=False).head(2)

# Exchange Rate
usd_idx_df = fdr.DataReader('^NYICDX')
usd_kr_df = fdr.DataReader('USD/KRW').sort_index(ascending=False).head(2)
eur_kr_df = fdr.DataReader('EUR/KRW').sort_index(ascending=False).head(2)
jpy_kr_df = fdr.DataReader('JPY/KRW').sort_index(ascending=False).head(2)


st.title("Good Morning, World!")
st.markdown("---")

# Stock Market
st.markdown("#### US Stock Market")
col1, col2, col3, col4, col5 = st.columns(5)

with col1 :
    container = st.container(border=True)
    container.markdown('###### S&P 500')
    render_today_market(snp_df, container)

with col2 : 
    container = st.container(border=True)
    container.markdown('###### NASDAQ')
    render_today_market(nasdaq_df, container)

with col3 :
    container = st.container(border=True)
    container.markdown('###### Dow')
    render_today_market(dji_df, container)

with col4 :
    container = st.container(border=True)
    container.markdown('###### Russell')
    render_today_market(rut_df, container)

with col5 :
    container = st.container(border=True)
    container.markdown('###### VIX')
    render_today_market(vix_df, container)

st.markdown("---")

# Exchange Rate
st.markdown("#### Exchange Rate")
col1, col2, col3, col4 = st.columns(4)

with col1 :
    container = st.container(border=True)
    container.markdown('###### USD Index')
    render_today_market(usd_idx_df, container)

with col2 :
    container = st.container(border=True)
    container.markdown('###### USD/KRW')
    render_today_market(usd_kr_df, container)

with col3 :
    container = st.container(border=True)
    container.markdown('###### EUR/KRW')
    render_today_market(eur_kr_df, container)

with col4 :
    container = st.container(border=True)
    container.markdown('###### JPY/KRW')
    render_today_market(jpy_kr_df, container, jpy_100=True)

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

# streamlit cloud
# API_KEY = st.secrets["API_KEY"]

youtube = build('youtube', 'v3', developerKey=API_KEY)

channel_id = "UCIipmgxpUxDmPP-ma3Ahvbw" # 매경 월가월부
search_query = "홍장원의 불앤베어"
video_search_result = get_latest_video_by_keyword(youtube, channel_id, search_query, is_handle=False)

if video_search_result :
    st.write(f"{video_search_result['published_at']}")
    st.video(f"{video_search_result['url']}")

st.markdown("---")