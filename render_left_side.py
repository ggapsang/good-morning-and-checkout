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

def render_left_side():

    # Stock Market
    st.markdown("#### US Stock Market")

    col1, col2, col3, col4, col5 = st.columns(5)

    with col1 :
        container = st.container(border=True)
        render_today_market(md.snp_df, container, label="S&P 500")

    with col2 : 
        container = st.container(border=True)
        render_today_market(md.nasdaq_df, container, label="NASDAQ")

    with col3 :
        container = st.container(border=True)
        render_today_market(md.dji_df, container, label="Dow Jones")

    with col4 :
        container = st.container(border=True)
        render_today_market(md.rut_df, container, label="Russell 2000")

    with col5 :
        container = st.container(border=True)
        render_today_market(md.vix_df, container, label="VIX")

    st.markdown("---")

    # Exchange Rate
    st.markdown("#### Exchange Rate")
    col1, col2, col3, col4 = st.columns(4)

    with col1 :
        container = st.container(border=True)
        render_today_market(md.usd_idx_df, container, label="USD Index")

    with col2 :
        container = st.container(border=True)
        render_today_market(md.usd_kr_df, container, label="USD/KRW")

    with col3 :
        container = st.container(border=True)
        render_today_market(md.eur_kr_df, container, label="EUR/KRW")

    with col4 :
        container = st.container(border=True)
        render_today_market(md.jpy_kr_df, container, label="JPY/KRW", jpy_100=True)

    st.markdown("---")

    # Bond, Gold
    st.markdown("#### Bond and Gold")
    col1, col2 = st.columns(2)

    with col1 :
        container = st.container(border=True)
        render_today_market(md.bond_df, container, label="Bond")

    with col2 :
        container = st.container(border=True)
        render_today_market(md.gold_df, container, label="Gold")

    st.markdown("---")

    # Youtue Link
    st.markdown("#### Youtube Link")

    if st.button("Refresh", key="refresh_youtube"):
        
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

