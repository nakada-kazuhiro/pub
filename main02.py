import streamlit as st
import time

st.title('streamlit 超入門')


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

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
	latest_iteration.text(f'Iteration {i + 1}')
	bar.progress(i + 1)
	time.sleep(0.1)

'Done!!!!'
' '
' '
' '






