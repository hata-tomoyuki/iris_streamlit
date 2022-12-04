import streamlit as st
import numpy as np
import pandas as pd

st.title('Streamlit Basic')
st.write('Hello World!')

df = pd.DataFrame({
    'First' : [1, 2, 3, 4],
    'Second' : [10, 20, 30, 40]
})


st.dataframe(df)

st.dataframe(df.style.highlight_max(axis=0), width=100, height=150)

st.table(df)

df = pd.DataFrame(
    np.random.rand(10, 3),
    columns=['a', 'b', 'c']
)

st.line_chart(df)

st.area_chart(df)

st.bar_chart(df)

df = pd.DataFrame(
    np.random.rand(100,2) / [50, 50] + [35.69, 139.70],
    columns=['lat', 'lon']
)

st.map(df)


from PIL import Image

img = Image.open('penguin.jpg')
st.image(img, caption='Penguin', use_column_width=True)


if st.checkbox('Show Image'):
    img = Image.open('penguin.jpg')
    st.image(img, caption='Penguin', use_column_width=True)


option = st.selectbox(
    '好きな数字',
    list(range(1, 11))
)

'あなたの好きな数字は', option


text = st.sidebar.text_input('好きなスポーツは？')
text

condition = st.sidebar.slider('あなたの今日の調子は？', 0, 100, 50)
'condition: ', condition

ex1 = st.expander('Q1')
ex1.write('A1')
ex2 = st.expander('Q2')
ex2.write('A2')
ex3 = st.expander('Q3')
ex3.write('A3')


import time
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i + 1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done'
