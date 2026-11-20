import streamlit as st
from lotto_utils import *

st.title('🎱로또 번호 생성기')
n = st.number_input('몇 게임 할까요?', min_value=1, max_value=10, value=5)

if st.button('번호 뽑기'):
    games = make_games(n)
    for i in range(n):
        st.write(f'**{i + 1}게임** : {to_text(games[i])}')