import streamlit as st
from PIL import Image
import openai
import os

# 🧠 OpenAI API 키 입력
openai.api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

st.markdown("## 🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("""
한 장의 사진, 한 줄의 감정.  
**감정과 이야기를 리토끼와 함께 풀어보세요.**  
(지금은 사진 없이 감성 키워드만 입력해도 작동합니다)
""")

# 📸 이미지 업로드
uploaded_file = st.file_uploader("🖼️ 사진을 업로드하세요", type=["jpg", "jpeg", "png"])

# 📝 시/수필 선택
genre = st.selectbox("🧡 생성할 글의 형식을 선택하세요", ["시", "수필"])

# 🌿 감성 키워드 입력
keyword = st.text_input("🍀 감성을 입력하세요 (예: 어머니, 구름, 새벽 등)")

# 🚀 디카시 생성
if st.button("🌸 디카시 생성하기") and openai.api_key:
    with st.spinner("디카시를 생성 중입니다..."):

        # 업로드된 이미지 경로 (임시 저장)
        image_info = ""
        if uploaded_file is not None:
            image = Image.open(uploaded_file)
            st.image(image, caption="업로드한 사진", use_column_width=True)
            image_info = "사진 속 풍경은 마치 {}의 감정을 담은 장면처럼 느껴진다.\n".format(keyword)

        # 프롬프트 구성
        prompt = f"""
다음은 감성적인 {genre}를 쓰는 디카시 작가입니다.
{image_info}
주제는 "{keyword}"입니다. 한국어로 문학적인 {genre}를 써주세요.
"""

        try:
            client = openai.OpenAI()
            response = client.chat.completions.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "너는 감성 시를 잘 쓰는 디카시 작가입니다."},
                    {"role": "user", "content": prompt}
                ]
            )
            generated_text = response.choices[0].message.content
            st.subheader("🌸 생성된 디카시")
            st.success(generated_text)

        except Exception as e:
            st.error(f"오류 발생: {e}")
