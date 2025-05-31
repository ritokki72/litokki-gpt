import streamlit as st
from PIL import Image
import openai
import os
import base64

st.set_page_config(page_title="리토끼GPT - 감성 디카시 생성기")

# ✅ API 키 입력
openai.api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

# ✅ 제목 및 설명
st.markdown("## 🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("한 장의 사진, 한 줄의 감정.  \n**감정과 이야기를 리토끼와 함께 풀어보세요.**  \n(지금은 사진 없이 감성 키워드만 입력해도 작동합니다)")

# ✅ 이미지 업로드
uploaded_file = st.file_uploader("📸 사진을 업로드하세요", type=["jpg", "jpeg", "png"])
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 사진", use_column_width=True)
    # 이미지를 base64로 인코딩
    image_bytes = uploaded_file.getvalue()
    encoded_image = base64.b64encode(image_bytes).decode("utf-8")
else:
    encoded_image = None

# ✅ 형식 선택: 시 / 수필
genre = st.selectbox("📝 생성할 글의 형식을 선택하세요", ["시", "수필"])

# ✅ 감성 키워드 입력
keyword = st.text_input("🍀 감성을 입력하세요 (예: 어머니, 구름, 새벽 등)")

# ✅ 버튼 클릭 시 실행
if st.button("🌸 디카시 생성하기") and openai.api_key and keyword:
    with st.spinner("디카시 생성 중입니다..."):

        # 프롬프트 구성
        prompt = f"""
다음 조건을 만족하는 {genre}를 작성해 주세요:

1. 감성 키워드: "{keyword}"
2. 이미지가 있다면 이미지의 분위기를 참고해서 작성하세요.
3. 독자가 감정에 몰입할 수 있도록 서정적이고 진정성 있는 문체로 작성하세요.
"""
        if encoded_image:
            prompt += "\n4. 이미지 분위기에 어울리는 묘사나 정서를 포함해 주세요."

        # 최신 openai API (v1.x 방식)
        client = openai.OpenAI()
        response = client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "너는 시와 수필을 감성적으로 잘 쓰는 디카시 작가입니다."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.8,
            max_tokens=1000
        )

        result = response.choices[0].message.content.strip()
        st.markdown("## 🌸 생성된 디카시")
        st.success(result)
