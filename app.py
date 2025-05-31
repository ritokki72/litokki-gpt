import streamlit as st
from openai import OpenAI
import os

# 🔐 OpenAI API 키 입력
api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

# 🎯 제목 및 설명
st.title("🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("""
한 장의 사진, 한 줄의 감정.  
**감정과 이야기를 리토끼와 함께 풀어보세요.**  
(지금은 사진 없이 **감성 키워드만 입력**해도 작동합니다)
""")

# 📝 감성 키워드 입력
keyword = st.text_input("🍀 감성을 입력하세요 (예: 어머니, 구름, 새벽 등)")

# 🧠 GPT 호출 (OpenAI 최신 방식)
if api_key and keyword:
    client = OpenAI(api_key=api_key)

    with st.spinner("디카시 생성 중입니다..."):
        try:
            response = client.chat.completions.create(
                model="gpt-4",  # 필요시 gpt-3.5-turbo로 변경 가능
                messages=[
                    {"role": "system", "content": "너는 감성적인 디카시를 짓는 작가입니다. 짧고 인상 깊은 디카시 한 편을 써주세요."},
                    {"role": "user", "content": f"감성 키워드: {keyword}"}
                ],
                temperature=0.9
            )
            generated_poem = response.choices[0].message.content
            st.markdown("### 🌸 생성된 디카시")
            st.success(generated_poem)

        except Exception as e:
            st.error(f"오류 발생: {e}")
elif not api_key:
    st.warning("먼저 OpenAI API 키를 입력해주세요.")
   
