import streamlit as st
from PIL import Image
import openai
import io

# 페이지 설정
st.set_page_config(page_title="리토끼GPT - 감성 디카시 생성기", layout="centered")

# 타이틀
st.title("🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("한 장의 사진과 당신의 감정을 AI 친구, 리토끼GPT가 시로 풀어드립니다.")

# 🔑 API 키 입력
user_api_key = st.text_input("🔐 OpenAI API 키를 입력해주세요", type="password")

# 🖼️ 이미지 업로드
st.header("🖼️ 오늘의 디카시")
uploaded_file = st.file_uploader("사진을 업로드해주세요", type=["jpg", "jpeg", "png"])

if uploaded_file:
    image = Image.open(uploaded_file)
    st.image(image, caption="업로드한 이미지", use_column_width=True)

    # 🎯 감정 키워드 입력
    prompt = st.text_input("💬 이 사진을 보고 떠오른 감정이나 장면을 적어주세요", placeholder="예: 햇살, 그리움, 여운")

    if st.button("✍️ 디카시 생성하기"):
        if not user_api_key:
            st.error("⚠️ 먼저 OpenAI API 키를 입력해주세요.")
        elif not prompt:
            st.error("⚠️ 감성 키워드를 입력해주세요.")
        else:
            with st.spinner("리토끼GPT가 시를 쓰는 중... 🐰🖌️"):
                try:
                    openai.api_key = user_api_key
                    response = openai.chat.completions.create(
                        model="gpt-4",  # ← gpt-3.5로 바꾸면 무료 버전
                        messages=[
                            {"role": "system", "content": "너는 감성적인 시를 쓰는 시인이야."},
                            {"role": "user", "content": f"다음 감정을 담아 한 편의 디카시를 써줘: {prompt}"}
                        ],
                        temperature=0.8
                    )
                    poem = response.choices[0].message.content.strip()
                    st.success("✨ 디카시 생성 완료!")
                    st.markdown(f"### 📝 리토끼의 디카시\n\n{poem}")
                except Exception as e:
                    st.error(f"⚠️ 오류 발생: {e}")

# 푸터
st.markdown("---")
st.caption("© 2025 리토끼GPT. 감성은 당신에게, 기술은 우리에게.")
