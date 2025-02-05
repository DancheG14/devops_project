import streamlit as st
import requests


st.title('Определение тональности текста')
text = st.text_input('Введите текст', 'Я люблю распределенные вычисления')
result = st.button('Определить тональность')

if result:
    response = requests.post('http://127.0.0.1:8000/predict', 
                             json={'text': text})
    st.write('**Результаты распознавания:**')
    st.write(response.json()['label'])
