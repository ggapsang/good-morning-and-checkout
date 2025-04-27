from datetime import date, timedelta
import FinanceDataReader as fdr
import pandas as pd

date_today = date.today()   
date_yesterday = date.today() - timedelta(days=1)
date_string_today = date_today.strftime("%Y-%m-%d")
date_string_yesterday = date_yesterday.strftime(("%Y-%m-%d"))

# US market Indices
nasdaq_df = fdr.DataReader('IXIC').sort_index(ascending=False)
snp_df = fdr.DataReader('S&P500').sort_index(ascending=False)
dji_df = fdr.DataReader('DJI').sort_index(ascending=False)
rut_df = fdr.DataReader('RUT').sort_index(ascending=False)
vix_df = fdr.DataReader('VIX').sort_index(ascending=False)

# Exchange Rate
usd_idx_df = fdr.DataReader('^NYICDX')
usd_kr_df = fdr.DataReader('USD/KRW').sort_index(ascending=False)
eur_kr_df = fdr.DataReader('EUR/KRW').sort_index(ascending=False)
jpy_kr_df = fdr.DataReader('JPY/KRW').sort_index(ascending=False)