import streamlit as st
import openai
from PIL import Image
import os

# 🌟 OpenAI API 키 입력
openai.api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

# 🌸 앱 제목 및 설명
st.markdown("## 🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("""
한 장의 사진, 한 줄의 감정.  
**감정과 이야기를 리토끼와 함께 풀어보세요.**  
(지금은 사진 없이 감성 키워드만 입력해도 작동합니다)
""")

# 🌿 감성 키워드 입력
keyword = st.text_input("🍀 감성을 입력하세요 (예: 어머니, 구름, 새벽 등)")

# 🛎️ 버튼을 눌러야 생성되도록 명시
if st.button("🌸 디카시 생성하기"):
    if not openai.api_key:
        st.warning("⚠️ 먼저 OpenAI API 키를 입력하세요.")
    elif not keyword:
        st.warning("⚠️ 감성 키워드를 입력해주세요.")
    else:
        with st.spinner("🌀 디카시 생성 중입니다..."):

            # GPT-4 또는 gpt-3.5-turbo로 구성 가능
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {
                        "role": "system",
                        "content": "당신은 감성을 자극하는 시를 잘 쓰는 디카시 작가입니다."
                    },
                    {
                        "role": "user",
                        "content": f"'{keyword}'를 주제로 감성적인 디카시 한 편을 써 주세요."
                    }
                ]
            )

            result = response.choices[0].message.content
            st.markdown("## 🌸 생성된 디카시")
            st.success(result)
