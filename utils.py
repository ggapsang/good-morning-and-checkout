from datetime import date, timedelta

import streamlit as st
import pandas as pd
import numpy as np

import FinanceDataReader as fdr
from googleapiclient.discovery import build

def get_today_us_market(df, container, date_string_today, date_string_yesterday, jpy_100=False):
    
    index = df['Close'].head(1).values[0]
    change = df['Close'].head(1).values[0] - df['Close'].head(2).values[1]
    change_percent = (df['Close'].head(1).values[0] - df['Close'].head(2).values[1]) / df['Close'].head(2).values[1] * 100

    if jpy_100:
        index = np.round(index, 2) * 100
        change = np.round(change, 2) * 100
    else:
        index = np.round(index, 2)
        change = np.round(change, 2)
    change_percent = np.round(change_percent, 2)

    if change > 0:
        color = 'green'
    elif change < 0:
        color = 'red'
    else:
        color = 'black'
    
    with container:
        st.write(f"<span style='font-size:18px; font-weight:bold'>{index}</span>", unsafe_allow_html=True)
        st.write(f"<span style='color:{color};'>{change}</span>", unsafe_allow_html=True)
        st.write(f"<span style='color:{color};'>{change_percent}%</span>", unsafe_allow_html=True)


def get_latest_video_by_keyword(youtube, channel, search_query, is_handle=True):
    """
    채널 이름 또는 ID로 최신 동영상 검색
    is_handle이 True면 채널 핸들(@없는 형태)로 간주, False면 채널 ID로 간주
    """
    if is_handle:
        # 핸들이라면 @ 제거
        if channel.startswith('@'):
            channel = channel[1:]
            
        # 먼저 핸들로 채널 ID 찾기
        channel_request = youtube.search().list(
            part="snippet",
            q=channel,
            type="channel",
            maxResults=1
        )
        channel_response = channel_request.execute()
        
        if not channel_response['items']:
            return None
            
        channel_id = channel_response['items'][0]['id']['channelId']
    else:
        channel_id = channel
    
    # 이제 찾은 채널 ID로 검색
    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        q=search_query,
        type="video",
        maxResults=1,
        order="date"
    )
    
    response = request.execute()
    
    if response['items']:
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
