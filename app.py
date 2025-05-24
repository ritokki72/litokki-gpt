          
import streamlit as st
import openai
from PIL import Image
import io

st.set_page_config(page_title="리토끼GPT", page_icon="🐰")
st.title("🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("한 장의 사진과 당신의 감정을 AI 친구, 리토끼GPT가 시로 풀어드립니다.")

openai.api_key = st.text_input("🔑 OpenAI API 키를 입력해주세요", type="password")

st.subheader("🖼️ 오늘의 디카시")
image = st.file_uploader("사진을 업로드해주세요", type=["jpg", "jpeg", "png"])

if image:
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    user_emotion = st.text_input("💬 이 사진을 보고 느낀 감정이나 장면을 적어주세요", placeholder="예: 고요한 호수 위 햇살, 그리움, 여름밤")

    if user_emotion and openai.api_key:
        prompt = f"'{user_emotion}'이라는 감정 또는 장면을 바탕으로 감성적인 한국어 디카시 한 편을 써줘. 시적 언어로, 짧고 여운 있게."
        
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": prompt}
            ]
        )

        st.write("✍️ 디카시 생성 결과:")
        st.markdown(response.choices[0].message.content)

st.markdown("---")
st.caption("© 2025 리토끼GPT. 감정은 당신에게, 기술은 우리에게.")
