import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.sidebar.title('streamlit 超入門')

# メイン画面
st.header('読み込みデータ表示')


st.title('Explore a dataset')
st.write('A general purpose data exploration app')
file = st.file_uploader("Upload file", type=['csv'])
st.write(file)



# サイドバー
# ファイルアップロード
uploaded_file = st.sidebar.file_uploader("ファイルアップロード", type='csv') 

if uploaded_file is not None:
    # アップロードファイルをメイン画面にデータ表示
    df = pd.read_csv(uploaded_file)
    df = df.iloc[:,[3, 4, 9, 10, 11, 12, 14, 17, 18, 19, 20, 26]]
    df = df.dropna()
    df = df.reset_index(drop=True)
    st.write(df)
    members = df['担当者名'].unique()
    
    total_tbl = []
    for member in members:
    	_df = df[df['担当者名'] == member]
    	nounyu_gaku = _df['納入合計'].str.replace(',','').astype(int).sum()
    	nounyu_gaku_h = '{:,}'.format(nounyu_gaku)
    	total_tbl.append(dict(担当者名= member, 納入合計 = nounyu_gaku_h))
    total_gaku = df['納入合計'].str.replace(',','').astype(int).sum()
    total_gaku_h = '{:,}'.format(total_gaku)
    total_tbl.append(dict(担当者名= '事業所計', 納入合計 = total_gaku_h))
    
    df_display = pd.DataFrame(total_tbl, columns=['担当者名', '納入合計'])
    df_display
    

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
	right_column.write('ここは右カラム')

' '
' '
' '
' '

expander1 = st.expander('問い合わせ1')
expander1.write('回答内容１')
expander1.write('回答内容２')
expander1.write('回答内容３')
expander1.write('回答内容４')

expander2 = st.expander('問い合わせ2')
expander2.write('回答内容22')


' '
' '
' '






