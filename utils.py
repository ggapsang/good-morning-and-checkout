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


# API 키 설정
API_KEY = "YOUR_API_KEY" 
youtube = build('youtube', 'v3', developerKey=API_KEY)

def get_latest_video_by_keyword(channel_id, query):
    """특정 채널에서 키워드로 검색한 영상 중 가장 최신 영상 1개 반환"""

    request = youtube.search().list(
        part="snippet",
        channelId=channel_id,
        q=query,
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

# 사용 예시
channel_id = "UC_CHANNEL_ID"  # 채널 ID 입력
search_query = "검색어"  # 검색할 키워드
latest_video = get_latest_video_by_keyword(channel_id, search_query)

if latest_video:
    print(f"제목: {latest_video['title']}")
    print(f"URL: {latest_video['url']}")
    print(f"업로드 날짜: {latest_video['published_at']}")
else:
    print("검색 결과가 없습니다.")