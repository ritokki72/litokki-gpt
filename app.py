          
import openai
import streamlit as st
from PIL import Image
import io

st.set_page_config(page_title="리토끼GPT", page_icon="🐰")
st.title("🐰 리토끼GPT – 감성 디카시 생성기")
st.markdown("한 장의 사진으로부터 감성을 불어넣는 AI 친구, 리토끼GPT와 함께 해요.")

openai.api_key = st.text_input("🔑 OpenAI API 키를 입력하세요", type="password")

st.subheader("✍️ 오늘의 디카시")
image = st.file_uploader("사진을 업로드해주세요", type=["jpg", "jpeg", "png"])

if image and openai.api_key:
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    
    prompt = "이 이미지에서 느껴지는 감정과 풍경을 담은 감성적인 디카시 한 편을 써줘. 짧고 시처럼 표현해줘."
    
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    st.write("🖋️ 디카시 생성 결과:")
    st.markdown(response.choices[0].message.content)

st.markdown("---")
st.caption("© 2025 리토끼GPT. 감정은 당신에게, 기술은 우리에게.")
