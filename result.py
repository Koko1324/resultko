#작은 따옴표는 변수임
import streamlit as st
from PIL import Image
# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 로고 이미지를 열고, 크기를 조절합니다.
logo = Image.open("logo.png")

# 헤더 섹션을 만들기 위해 열(column)을 나눕니다.
header_col1, header_col2, header_col3 = st.columns([1,1,4])

#레이아웃 설정
col4, col5, col6 = st.columns([1,1,1])

with header_col1:
    # 첫 번째 열에 로고 이미지를 추가합니다.
    st.image(logo, use_column_width=True)

with header_col2:
    abc = 'A'
    st.markdown(f"<p style='font-size:18px;'>코스 {abc}</p>", unsafe_allow_html=True)#abc에 "A","B","C"중 하나 선택

with header_col3:
    with st.expander("설명"):
        st.write('''
        설명
        ''')
        #st.image('필요할 시 이미지 넣고 필요 없으면 지우기')


with col4:
    st.write('a1234'+"일차")#a1234에 몇일차인지 입력
    st.write('장소')
    #st.image('장소이미지')
    st.write('장소 설명')
with col5:
    st.write('a1234'+"일차")#a1234에 몇일차인지 입력
    st.write('장소')
    #st.image('장소이미지')
    st.write('장소 설명')
with col6:
    st.write('a1234'+"일차")#a1234에 몇일차인지 입력
    st.write('장소')
    #st.image('장소이미지')
    st.write('장소 설명')