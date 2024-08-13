#작은 따옴표는 변수임
import streamlit as st
from PIL import Image
# 페이지 레이아웃 설정
st.set_page_config(layout="wide")

# 로고 이미지를 열고, 크기를 조절합니다.
logo = Image.open("logo.png")

#레이아웃 설정
col1, col2, col3, col4 = st.columns([1,1,1,1])

with col3,col4:
    print('설명')#설명

with col1:
    st.write("코스"+'abc')#abc에 'A','B','C'중 하나 저장
    st.write('a1234'+"일차")#a1234에 몇일차인지 입력
    st.write("장소")
    st.image('장소이미지')
with col2:
    st.write("코스"+'abc')#abc에 'A','B','C'중 하나 저장
    st.write('a1234'+"일차")#a1234에 몇일차인지 입력
    st.write("장소")
    st.image('장소이미지')
with col3:
    st.write("코스"+'abc')#abc에 'A','B','C'중 하나 저장
    st.write('a1234'+"일차")#a1234에 몇일차인지 입력
    st.write("장소")
    st.image('장소이미지')
with col4:
    st.write("코스"+'abc')#abc에 'A','B','C'중 하나 저장
    st.write('a1234'+"일차")#a1234에 몇일차인지 입력
    st.write("장소")
    st.image('장소이미지')