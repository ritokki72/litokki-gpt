import streamlit as st
import openai

# 앱 제목과 소개 문구
st.markdown("🐰 **리토끼GPT – 감성의 집**")
st.markdown("""
**어떤 마음이든, 어떤 글이든 더 깊이 담아낼 수 있는 공간.  
감정과 이야기를 리토끼와 함께 풀어보세요.**
""")

# API 키 입력
api_key = st.text_input("🔐 OpenAI API 키를 입력해주세요", type="password")

# 글 장르 선택
genre = st.selectbox("✍️ 생성할 글의 장르를 선택하세요", ["디카시", "감성수필", "편지글", "영상 내레이션"])

# 글 주제 입력
prompt = st.text_area("💬 글의 주제, 장면, 장면 등을 입력해주세요:")

# 글 생성 버튼
if st.button("🎉 글을 만들어보세요!"):

    if not api_key:
        st.error("API 키를 입력해주세요!")
    elif not prompt.strip():
        st.error("글의 주제를 입력해주세요!")
    else:
        with st.spinner("리토끼가 감성을 담는 중... 🐇"):
            try:
                openai.api_key = api_key

                messages = [
                    {"role": "system", "content": f"당신은 '{genre}' 장르의 감성 작가입니다. 감정이 풍부하고 문학적인 글을 써주세요."},
                    {"role": "user", "content": prompt}
                ]

                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=messages,
                    temperature=0.9,
                    max_tokens=800
                )

                result = response.choices[0].message.content
                st.markdown("### ✨ 생성된 " + genre)
                st.write(result)

            except Exception as e:
                st.error(f"오류 발생: {str(e)}")

