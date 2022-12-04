import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.datasets import load_iris

iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)

df['target'] = iris.target

df.loc[df['target'] == 0, 'target'] = 'setosa'
df.loc[df['target'] == 1, 'target'] = 'varsicolor'
df.loc[df['target'] == 2, 'target'] = 'virginica'


x = iris.data[:, [0, 2]]
y = iris.target


clf = LogisticRegression()
clf.fit(x, y)


st.sidebar.header('Input Features')

sepalVal = st.sidebar.slider('sepal length (cm)', min_value=0.0, max_value=10.0, step=0.1)
petalVal = st.sidebar.slider('petal length (cm)', min_value=0.0, max_value=10.0, step=0.1)


st.title('Iris Classifier')
st.write('## Input value')

value_df = pd.DataFrame([], columns=['data', 'sepal length (cm)', 'petal length (cm)'])
record = pd.Series(['data', sepalVal, petalVal], index=value_df.columns)
value_df = value_df.append(record, ignore_index=True)
value_df.set_index('data', inplace=True)

st.write(value_df)


pred_probs = clf.predict_proba(value_df)
pred_df = pd.DataFrame(pred_probs, columns=['setosa', 'versicolor', 'virginica'], index=['probability'])

st.write('## Prediction')
st.write(pred_df)

name = pred_df.idxmax(axis=1).tolist()
st.write("## Result")
st.write('このアイリスはきっと', str(name[0]), 'です！')
