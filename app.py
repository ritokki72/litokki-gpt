import streamlit as st
import openai
from PIL import Image
import os

st.set_page_config(page_title="리토끼GPT - 감성 디카시 생성기")

st.markdown("""
# 🐰 리토끼GPT – 감성 디카시 생성기
한 장의 사진, 한 줄의 감정.  
**감정과 이야기를 리토끼와 함께 풀어보세요.**  
(지금은 사진 없이 감성 키워드만 입력해도 작동합니다)
""")

# OpenAI API 키 입력
api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

# 이미지 업로드
uploaded_file = st.file_uploader("포토지마다 가장 견본적인 파일을 업로드해주세요", type=["jpg", "jpeg", "png"])
if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 사진", use_column_width=True)

# 장르 선택
genre = st.selectbox("포스팅할 글의 형식을 선택해주세요", ["시", "수필"])

# 감성 키워드 입력
keyword = st.text_input("🌱 감성을 입력해주세요 (예: 아름다운 느낌, 구름, 살인)")

# 생성 버튼
if st.button("🌸 디카시 생성하기"):
    if not api_key:
        st.warning("우선 OpenAI API 키를 입력해주세요.")
    elif not keyword:
        st.warning("감성 키워드를 입력해주세요.")
    else:
        with st.spinner("키워드로 디카시 생성 중..."):
            client = openai.OpenAI(api_key=api_key)

            prompt = f"""
            다음 조건을 참고하여 감성적인 {genre}을(를) 작성해줘:
            - 키워드: {keyword}
            - 시적인 표현, 감동을 주는 흐름, 사람의 마음을 어루만지는 언어 사용
            - 문학적인 개성 강조 (특히 시의 경우 함축적이고 이미지 중심 표현 사용)
            - 결과는 제목 + 본문으로 구성
            """

            try:
                response = client.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": "당신은 감성적인 시를 잘 쓰는 디카시 작가입니다."},
                        {"role": "user", "content": prompt}
                    ]
                )
                result = response.choices[0].message.content
                st.markdown("## 🌸 생성된 디카시")
                st.success(result)
            except Exception as e:
                st.error(f"오류 발생: {e}")

