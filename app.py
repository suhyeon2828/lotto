import streamlit as st
from lotto_utils import *

st.title('🎱 로또 번호 생성기')

@st.cache_data # CSV는 처음 한 번만 읽기
def get_counts():
    return load_counts('lotto.csv')

count = get_counts()
tab1, tab2, tab3 = st.tabs(['🎲 자동 뽑기', '📊 번호별 통계', '✋ 수동 선택'])

with tab1: # ① 자동 뽑기
    n = st.number_input('몇 게임 할까요?', min_value=1, max_value=10, value=5)
    col1, col2 = st.columns(2)
    if col1.button('랜덤으로 뽑기'):
        st.session_state.games = make_games(n)
    if col2.button('자주 나온 번호로 뽑기'):
        games = []
        for i in range(n):
            games.append(make_hot_game(count))
        st.session_state.games = games
    if 'games' in st.session_state:
        for i in range(len(st.session_state.games)):
            st.write(f'**{i + 1}게임** : {to_text(st.session_state.games[i])}')

with tab2: # ② 번호별 당첨 횟수
    st.write('1회 ~ 1250회 당첨번호 6개 기준 (보너스 제외)')
    st.bar_chart(pd.Series(count, name='당첨 횟수'))
    top10 = top_numbers(count, 10)
    st.write('자주 나온 번호 TOP 10 :', to_text(top10))