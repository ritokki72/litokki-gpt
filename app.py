import streamlit as st
import openai
from PIL import Image
import os

# 🔑 OpenAI API 키 입력
openai.api_key = st.text_input("🔑 OpenAI API Key를 입력하세요", type="password")

# 📷 감성 키워드 입력
st.title("🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("한 장의 사진, 한 줄의 감정. **감성과 이야기를 리토끼와 함께 풀어보세요.**")

uploaded_file = st.file_uploader("📂 사진을 업로드하세요", type=["jpg", "jpeg", "png"])
keyword = st.text_input("✨ 감성 키워드를 입력하세요 (예: 어머니, 바람, 고요한 새벽 등)")

if uploaded_file and keyword and openai.api_key:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 사진", use_column_width=True)

    with st.spinner("✍️ 디카시 생성 중..."):
        response = openai.ChatCompletion.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "당신은 감성적인 시를 잘 쓰는 디카시 작가입니다."},
                {"role": "user", "content": f"이 키워드를 담아 디카시 한 편을 써 주세요: {keyword}"}
            ]
        )
        poem = response['choices'][0]['message']['content']
        st.markdown("### 🌿 생성된 디카시")
        st.write(poem)

elif not openai.api_key:
    st.warning("🔑 먼저 OpenAI API Key를 입력하세요.")
      
