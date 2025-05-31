import streamlit as st
import openai
from PIL import Image
import os

# 🔐 OpenAI API 키 입력
openai.api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

st.title("🐰 리토끼GPT – 감성 디카시 생성기")

st.markdown("""
한 장의 사진, 한 줄의 감정.  
**감정과 이야기를 리토끼와 함께 풀어보세요.**  
(지금은 사진 없이 감성 키워드만 입력해도 작동합니다)
""")

# 📸 이미지 업로드
uploaded_file = st.file_uploader("📷 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

# 🎭 장르 선택
genre = st.selectbox("✍️ 생성할 글의 형식을 선택하세요", ["시", "수필"])

# 🍀 감성 키워드 입력
keyword = st.text_input("🍀 감성을 입력하세요 (예: 어머니, 구름, 새벽 등)")

# 📝 디카시 생성 버튼
if st.button("🌸 디카시 생성하기") and openai.api_key and keyword:
    if uploaded_file:
        image = Image.open(uploaded_file)
        st.image(image, caption="업로드한 사진", use_column_width=True)

    with st.spinner("✍️ 디카시 생성 중입니다..."):
        prompt = f"""
당신은 감성적인 {genre} 작가입니다.
아래 키워드를 보고 {genre}를 한 편 작성해 주세요.

키워드: {keyword}

답변은 반드시 마크다운 형식으로 해주세요.
"""

        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "당신은 감성 글을 쓰는 디카시 작가입니다."},
                    {"role": "user", "content": prompt}
                ],
                temperature=0.8
            )
            result = response.choices[0].message.content
            st.markdown("## 🌸 생성된 디카시")
            st.markdown(result)

        except Exception as e:
            st.error(f"오류 발생: {e}")
 
