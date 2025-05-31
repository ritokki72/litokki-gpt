import streamlit as st
from PIL import Image
import openai

# 🔑 OpenAI API 키 입력
st.set_page_config(page_title="리토끼GPT - 감성 디카시 생성기")
st.title("🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("""
한 장의 사진, 한 줄의 감정.  
감정과 이야기를 리토끼와 함께 풀어보세요.  
(지금은 사진 없이 감성 키워드만 입력해도 작동합니다)
""")

api_key = st.text_input("🔑 OpenAI API 키를 입력해주세요", type="password")
if not api_key:
    st.warning("API 키를 입력해주세요.")
    st.stop()

client = openai.OpenAI(api_key=api_key)

# 📷 이미지 업로드
uploaded_file = st.file_uploader("포토지마다 가장 감성적인 파일을 업로드해주세요", type=["jpg", "jpeg", "png"])

# ✍️ 장르 선택
genre = st.selectbox("포스팅할 글의 형식을 선택해주세요", ["시", "수필"])

# 💭 감성 키워드
prompt = st.text_input("🌷 감성을 입력해주세요 (예: 아름다운 느낌, 구름, 설렘)")

# 🪄 디카시 생성
if st.button("🌸 디카시 생성하기"):
    if not prompt:
        st.warning("감성을 입력해주세요!")
        st.stop()

    with st.spinner("리토끼가 감성을 느끼는 중...🐰"):
        try:
            messages = [
                {"role": "system", "content": f"당신은 감성적인 {genre} 작가입니다."},
                {"role": "user", "content": f"{prompt}에 어울리는 {genre} 한 편을 써 주세요."}
            ]

            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages
            )

            result = response.choices[0].message.content
            st.markdown("## 🌸 생성된 디카시")
            st.success(result)

            if uploaded_file:
                image = Image.open(uploaded_file)
                st.image(image, caption="📷 업로드한 사진", use_column_width=True)

        except Exception as e:
            st.error(f"오류 발생: {e}")
   
