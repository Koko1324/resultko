#작은 따옴표는 변수임
import streamlit as st
from PIL import Image

# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 로고 이미지를 열고, 크기를 조절합니다.
logo = Image.open("logo.png")

# 첫 번째 열에 로고 이미지를 추가합니다.
st.image(logo, use_column_width=True)

#A코스
with st.container(border = True):
    abc = 'A'
    st.markdown(f"<p style='font-size:18px;'>코스 {abc}</p>", unsafe_allow_html=True)#abc에 "A","B","C"중 하나 선택

    def day():
        #일차 저장
        a = 1
        input_by_user = 6#실제로 입력받은 값 저장해야 함
        #결과 자세히 보기 눌렀을 때
        for i in range(input_by_user):
            with st.container(border = True):
                st.write("{}일차".format(a))#a(int)에 몇일차인지 입력
                st.write('장소 : ')
                st.write('장소 설명 : ')
            a += 1
        with st.container(border = True):
            st.write('총 예산 : ')
    day()
#B코스
with st.container(border = True):
    abc = 'B'
    st.markdown(f"<p style='font-size:18px;'>코스 {abc}</p>", unsafe_allow_html=True)#abc에 "A","B","C"중 하나 선택
    day()
#C코스
with st.container(border = True):
    abc = 'C'
    st.markdown(f"<p style='font-size:18px;'>코스 {abc}</p>", unsafe_allow_html=True)#abc에 "A","B","C"중 하나 선택
    day()