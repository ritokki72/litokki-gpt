import streamlit as st
import openai

st.set_page_config(page_title='리토끼GPT - "감성의 집"', layout="centered")

st.title("🐰 리토끼GPT – 감성의 집")
st.markdown("어떤 마음이든, 어떤 글이든 더 넓어질 수 있는 공간." 
감정과 이야기를 리토끼와 함께 풀어보세요.")

# API 키 입력
api_key = st.text_input("🔐 OpenAI API 키를 입력해주세요", type="password")

# 장르 선택
genre = st.selectbox(
    "✍️ 생성할 글의 장르를 선택하세요",
    [
        "디카시", "감성 수필", "명상문", "편지글", "일기",
        "단편소설 도입부", "영상 나레이션", "유튜브 인트로 스크립트",
        "블로그 소개글", "SNS 캡션", "광고 카피", "독후감",
        "이어쓰기 창작", "창작 프롬프트", "자유 형식"
    ]
)

# 글 주제 또는 키워드 입력
prompt = st.text_area("💬 글의 주제, 감정, 장면 등을 자유롭게 입력해주세요:", height=150, placeholder="예: 그리움, 따뜻한 바람, 이별의 기억")

if st.button("✨ 글 생성하기"):
    if not api_key:
        st.error("API 키를 입력해주세요!")
    elif not prompt.strip():
        st.error("주제나 감정을 입력해주세요!")
    else:
        with st.spinner("리토끼가 감성 글을 짓는 중입니다... 🐰✍️"):
            try:
                openai.api_key = api_key
                response = openai.chat.completions.create(
                    model="gpt-4",
                    messages=[
                        {"role": "system", "content": f"너는 감성적인 글을 창작하는 작가야. 사용자가 선택한 장르는 '{genre}'야."},
                        {"role": "user", "content": f"장르: {genre}\n주제: {prompt}\n이 내용을 바탕으로 {genre} 형식의 글을 써줘."}
                    ],
                    temperature=0.85
                )
                result = response.choices[0].message.content.strip()
                st.success("🎉 글 생성 완료!")
                st.markdown(f"### ✨ 생성된 {genre}\n\n{result}")
            except Exception as e:
                st.error(f"⚠️ 오류 발생: {e}")

st.markdown("---")
st.caption("© 2025 리토끼GPT - 감성 창작의 집. 모두의 이야기를 담습니다.")
