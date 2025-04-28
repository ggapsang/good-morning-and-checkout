from datetime import date, timedelta

import streamlit as st
import pandas as pd
import numpy as np

import FinanceDataReader as fdr
from googleapiclient.discovery import build
import plotly.graph_objects as go

def render_today_market(df, container, label, jpy_100=False):
    index = df['Close'].head(1).values[0]
    change = df['Close'].head(1).values[0] - df['Close'].head(2).values[1]
    change_percent = (df['Close'].head(1).values[0] - df['Close'].head(2).values[1]) / df['Close'].head(2).values[1] * 100

    if jpy_100:
        index = np.round(index, 1) * 100
        change = np.round(change, 2) * 100
    else:
        index = np.round(index, 1)
        change = np.round(change, 2)
    change_percent = np.round(change_percent, 2)

    with container:
        st.markdown(f"##### {change_percent}")
        st.markdown("""
        <style>
        [data-testid="stMetricValue"] {
            font-size: 1.5rem !important;
            font-weight: bold !important;
        }
        </style>
        """, unsafe_allow_html=True)
        st.metric(label=label, value=index, delta=change, delta_color="normal", help=f"{change} ({change_percent}%)")


def create_candlestick(df, title='Candlestick Chart', yaxis_title='index', xaxis_title='date'):
    # 이동평균선 계산
    # df['MA5'] = df['Close'].rolling(window=5).mean()
    df['MA20'] = df['Close'].rolling(window=20).mean()
    df['MA60'] = df['Close'].rolling(window=60).mean()
    df['MA120'] = df['Close'].rolling(window=120).mean()
    df['MA180'] = df['Close'].rolling(window=180).mean()
    
    # 캔들차트 생성
    fig = go.Figure(data=[go.Candlestick(
        x=df.index,
        open=df['Open'],
        high=df['High'],
        low=df['Low'],
        close=df['Close'],
        name='candle'
    )])
    
    # 이동평균선 추가
    # fig.add_trace(go.Scatter(x=df.index, y=df['MA5'], mode='lines', name='MA5', line=dict(color='blue')))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA20'], mode='lines', name='MA20', line=dict(color='orange')))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA60'], mode='lines', name='MA60', line=dict(color='green')))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA120'], mode='lines', name='MA120', line=dict(color='red')))
    fig.add_trace(go.Scatter(x=df.index, y=df['MA180'], mode='lines', name='MA180', line=dict(color='purple')))
    
    # 레이아웃 설정
    fig.update_layout(
        title=title,
        yaxis_title=yaxis_title,
        xaxis_title=xaxis_title,
        legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="center", x=0.5)
    )
    
    return fig

@st.cache_data(ttl=3600*12)  # 12시간 동안 캐싱
def get_latest_video_by_keyword(_youtube, channel, search_query, is_handle=False):
    """채널 ID로 최신 동영상 검색 (캐싱 적용)"""
    
    # is_handle 파라미터가 False일 때는 channel을 ID로 바로 사용
    channel_id = channel
    
    # 채널 ID로 바로 검색
    request = _youtube.search().list(
        part="snippet",
        channelId=channel_id,
        q=search_query,
        type="video",
        maxResults=1,
        order="date"
    )
    
    try:
        response = request.execute()
        
        if response.get('items') and len(response['items']) > 0:
            item = response['items'][0]
            video_id = item['id']['videoId']
            title = item['snippet']['title']
            url = f"https://www.youtube.com/watch?v={video_id}"
            published_at = item['snippet']['publishedAt']
            
            return {
                'title': title,
                'url': url,
                'published_at': published_at
            }
        else:
            return None
    except Exception as e:
        st.error(f"API 오류: {str(e)}")
        return None
    
