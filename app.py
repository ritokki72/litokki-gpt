# 장르 선택메뉴
genre = st.selectbox("포스팅할 글의 형식을 선택해주세요", ["시", "수필"])

# 감성 키워드 입력
keyword = st.text_input("🌱 감성을 입력해주세요 (예: 아름다운 느낌, 구름, 햇살 등)")

# 생성 버튼
if st.button("🌸 디카시 생성하기"):
    if not api_key:
        st.warning("다시한다면 OpenAI API 키를 입력해주세요.")
    elif not keyword:
        st.warning("감성 키워드를 입력해주세요.")
    else:
        with st.spinner("키워드로 디카시 생성 중..."):
            client = OpenAI(api_key=api_key)

            prompt = f"""
            다음 조건을 참고해서 감성적인 {genre}을(를) 작성해줘:
            - 키워드: {keyword}
            - 시적인 표현, 감독을 주는 흐름, 사랑과 사이에서 동생하는 마음을 응원하는 언어 사용
            - 문학적 개성 강조 ( 특히 시의 경우 함초적과 이미지 중심 표현 사용 )
            - 결과는 제목 + 보문으로 구성
            """

            try:
                response = client.chat.completions.create(
                    model="gpt-3.5-turbo",
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
