from datetime import date, timedelta
import os
from dotenv import load_dotenv

import streamlit as st
import pandas as pd
import numpy as np

import FinanceDataReader as fdr
from googleapiclient.discovery import build
import market_data as md
from utils import create_candlestick

def render_right_side():
    # Stock Market
    st.markdown("#### ")

    col1, col2, col3 = st.columns([1, 12, 12]) # co1은 여백

    with col2:
        container = st.container(border=True)
        snp_df = md.snp_df.copy()
        snp_df = snp_df.head(250)
        snp_df.sort_index(ascending=True, inplace=True)
        snp_canldes = create_candlestick(snp_df, title='S&P 500', yaxis_title='S&P 500', xaxis_title='Date')
        container.plotly_chart(snp_canldes, use_container_width=True)

        container = st.container(border=True)
        usd_kr_df = md.usd_kr_df.copy()
        usd_kr_df = usd_kr_df.head(250)
        usd_kr_df.sort_index(ascending=True, inplace=True)
        usd_kr_canldes = create_candlestick(usd_kr_df, title='USD/KRW', yaxis_title='USD/KRW', xaxis_title='Date')
        container.plotly_chart(usd_kr_canldes, use_container_width=True)

    with col3:
        container = st.container(border=True)
        nasdaq_df = md.nasdaq_df.copy()
        nasdaq_df = nasdaq_df.head(250)
        nasdaq_df.sort_index(ascending=True, inplace=True)
        nasdaq_canldes = create_candlestick(nasdaq_df, title='NASDAQ', yaxis_title='NASDAQ', xaxis_title='Date')
        container.plotly_chart(nasdaq_canldes, use_container_width=True)

        container = st.container(border=True)
        gold_df = md.gold_df.copy()
        gold_df = gold_df.head(250)
        gold_df.sort_index(ascending=True, inplace=True)
        gold_canldes = create_candlestick(gold_df, title='Gold', yaxis_title='Gold', xaxis_title='Date')
        container.plotly_chart(gold_canldes, use_container_width=True)