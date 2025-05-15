          
import streamlit as st

st.set_page_config(page_title="리토끼GPT", page_icon="🐇")

st.title("🐇 리토끼GPT – 감성 디카시 생성기")
st.markdown("한 장의 사진으로부터 감성을 불어넣는 AI 친구, 리토끼GPT와 함께 해요.")

st.subheader("✍️ 오늘의 디카시")
image = st.file_uploader("사진을 업로드해주세요", type=["jpg", "jpeg", "png"])

if image:
    st.image(image, caption="업로드한 이미지", use_column_width=True)
    st.write("🪄 디카시 생성 중...")
    st.markdown("> 절벽 끝에 선 바람처럼\n> 나는 오늘도 두려움 위에 선다\n> 멈추지 않는 너를 닮기 위해")

st.markdown("---")
st.caption("© 2025 리토끼GPT. 감성은 당신에게, 기술은 우리에게.")
