import streamlit as st
import openai
from PIL import Image
import os

# 🔑 OpenAI API 키 입력
openai.api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

st.markdown("## 🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("한 장의 사진, 한 줄의 감정.  
**감정과 이야기를 리토끼와 함께 풀어보세요.**  
(지금은 사진 없이 감성 키워드만 입력해도 작동합니다)")

# 📸 사진 업로드 (선택 사항)
uploaded_file = st.file_uploader("📷 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

# 🌸 감성 키워드 입력
keyword = st.text_input("🍀 감성을 입력하세요 (예: 어머니, 구름, 새벽 등)")

# ✍️ 장르 선택
genre = st.radio("✍️ 생성할 형식을 선택하세요", ["디카시", "수필"])

# 📝 생성 버튼
if st.button("🌸 디카시 생성하기") and keyword and openai.api_key:
    with st.spinner("디카시를 생성 중입니다..."):

        # 프롬프트 구성
        if genre == "디카시":
            role_content = f"'{keyword}'이라는 감성 키워드를 바탕으로 디카시(짧은 시)를 써 주세요. 상징성과 이미지가 담긴 시로, 사진을 본 듯한 느낌을 주는 시로 작성해 주세요."
        else:
            role_content = f"'{keyword}'이라는 키워드를 주제로 감성 수필을 써 주세요. 감정을 담고 흐름이 자연스러운 산문 형태로 구성해 주세요."

        # OpenAI Chat API 호출
        try:
            response = openai.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "당신은 감성 시와 수필을 잘 쓰는 문학 작가입니다."},
                    {"role": "user", "content": role_content}
                ]
            )

            result = response.choices[0].message.content
            st.markdown("### 🌸 생성된 디카시" if genre == "디카시" else "### 📝 생성된 수필")
            st.success(result)

            # 업로드한 사진이 있을 경우 표시
            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="업로드한 사진", use_column_width=True)

        except Exception as e:
            st.error("🚨 오류가 발생했습니다. API 키를 확인하거나 다시 시도해 주세요.")
            st.exception(e)
