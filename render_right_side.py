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
from gnews import GNews


def stock_market_candle_chart(df, title, yaxis_title, xaxis_title):
    df = df.copy()
    df = df.head(250)
    df.sort_index(ascending=True, inplace=True)
    candlestick = create_candlestick(df, title=title, yaxis_title=yaxis_title, xaxis_title=xaxis_title)
    return candlestick


def create_stock_market_chart_with_dropdown():
    container = st.container(border=True)

    with container:
        options = ["S&P 500", "NASDAQ", "DOW JONES", "Russell", "VIX"]
        chart_type = st.selectbox("Chart Selection", options, index=0)
        if chart_type == "S&P 500":
            snp_candles = stock_market_candle_chart(md.snp_df, title='S&P 500', yaxis_title='S&P 500', xaxis_title='Date')
            container.plotly_chart(snp_candles, use_container_width=True)

        elif chart_type == "NASDAQ":
            nasdaq_candles = stock_market_candle_chart(md.nasdaq_df, title='NASDAQ', yaxis_title='NASDAQ', xaxis_title='Date')
            container.plotly_chart(nasdaq_candles, use_container_width=True)

        elif chart_type == "DOW JONES":
            dow_candles = stock_market_candle_chart(md.dow_df, title='DOW JONES', yaxis_title='DOW JONES', xaxis_title='Date')
            container.plotly_chart(dow_candles, use_container_width=True)

        elif chart_type == "Russell":
            russell_candles = stock_market_candle_chart(md.russell_df, title='Russell', yaxis_title='Russell', xaxis_title='Date')
            container.plotly_chart(russell_candles, use_container_width=True)

        elif chart_type == "VIX":
            vix_candles = stock_market_candle_chart(md.vix_df, title='VIX', yaxis_title='VIX', xaxis_title='Date')
            container.plotly_chart(vix_candles, use_container_width=True)

def create_exchange_market_chart_with_dropdown():
    container = st.container(border=True)

    with container:
        options = ["Dollar Index", "USD/KRW", "EUR/KRW", "JPY/KRW"]
        chart_type = st.selectbox("Chart Selection", options, index=0)
        if chart_type == "Dollar Index":
            dollar_index_candles = stock_market_candle_chart(md.usd_idx_df, title='Dollar Index', yaxis_title='Dollar Index', xaxis_title='Date')
            container.plotly_chart(dollar_index_candles, use_container_width=True)

        elif chart_type == "USD/KRW":
            usd_candles = stock_market_candle_chart(md.usd_kr_df, title='USD/KRW', yaxis_title='USD/KRW', xaxis_title='Date')
            container.plotly_chart(usd_candles, use_container_width=True)

        elif chart_type == "EUR/KRW":
            eur_candles = stock_market_candle_chart(md.eur_kr_df, title='EUR/KRW', yaxis_title='EUR/KRW', xaxis_title='Date')
            container.plotly_chart(eur_candles, use_container_width=True)

        elif chart_type == "JPY/KRW":
            jpy_candles = stock_market_candle_chart(md.jpy_kr_df, title='JPY/KRW', yaxis_title='JPY/KRW', xaxis_title='Date')
            container.plotly_chart(jpy_candles, use_container_width=True)

def create_safety_market_chart_with_dropdown():
    container = st.container(border=True)

    with container:
        options = ["Gold", "Bond"]
        chart_type = st.selectbox("Chart Selection", options, index=0)
        if chart_type == "Gold":
            gold_candles = stock_market_candle_chart(md.gold_df, title='Gold', yaxis_title='Gold', xaxis_title='Date')
            container.plotly_chart(gold_candles, use_container_width=True)

        elif chart_type == "Bond":
            bond_candles = stock_market_candle_chart(md.bond_df, title='Bond', yaxis_title='Bond', xaxis_title='Date')
            container.plotly_chart(bond_candles, use_container_width=True)



def render_right_side():
    # Stock Market
    st.markdown("#### ")

    col1, col2, col3 = st.columns([1, 12, 12]) # co1은 여백

    with col2:
        create_stock_market_chart_with_dropdown()
        create_exchange_market_chart_with_dropdown()
        create_safety_market_chart_with_dropdown()

    with col3:
        container = st.container(border=True)
        google_news = GNews()
        business_news_en = google_news.get_news_by_topic('BUSINESS')[0]
        finance_news_en = google_news.get_news_by_topic('FINANCE')[0]
        economy_news_en = google_news.get_news_by_topic('ECONOMY')[0]
        container.markdown(f"[{business_news_en['title']}]({business_news_en['url']})", unsafe_allow_html=True)
        container.markdown(f"[{finance_news_en['title']}]({finance_news_en['url']})", unsafe_allow_html=True)
        container.markdown(f"[{economy_news_en['title']}]({economy_news_en['url']})", unsafe_allow_html=True)
        

