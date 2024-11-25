import streamlit as st

# 질문 리스트
QUESTIONS = [
    "나는 환경 문제를 해결하기 위해 다른 사람들과 팀을 이루어 활동하는 것이 즐겁다.",
    "나는 혼자서 조용히 실천할 수 있는 환경 보호 활동을 선호한다.",
    "나는 친환경 캠페인에 참여할 때, 다른 사람들과의 상호작용이 동기를 부여한다.",
    "나는 온라인에서 혼자 정보를 찾아보며 환경 문제에 대해 공부하는 것을 즐긴다.",
    "나는 일상에서 실천 가능한 환경 보호 활동(예: 텀블러 사용, 대중교통 이용)을 중시한다.",
    "나는 기후변화의 원인과 해결책에 대한 큰 그림을 이해하는 것에 관심이 많다.",
    "나는 환경 보호를 위해 직접 행동할 수 있는 구체적인 방법이 필요하다.",
    "나는 미래 세대를 위한 장기적인 환경 문제 해결에 대해 더 관심이 많다.",
    "나는 환경 문제를 해결하기 위해 논리적이고 실질적인 방법을 중요시한다.",
    "나는 환경 문제를 해결하는 데 있어 사람들의 감정적 동기가 중요하다고 생각한다.",
    "나는 기후 문제 해결에 있어서 수치화된 결과와 데이터가 필수적이라고 생각한다.",
    "나는 환경 문제를 해결하는 과정에서 인간과 자연의 공감이 더 중요한 요소라고 본다.",
    "나는 환경 보호 활동을 위해 세부적인 계획과 목표를 세우고 실천한다.",
    "나는 유연하게 상황에 따라 다양한 환경 보호 방법을 시도하는 것을 선호한다.",
    "나는 주어진 시간 내에 정해진 환경 보호 목표를 달성하는 데 집중한다.",
    "나는 다양한 환경 보호 활동 중 내게 가장 흥미로운 것을 그때그때 선택한다."
]

# 결과와 추천 실천법
RESULTS = {
    "ENTP": ("그린 혁신가", ["기후 기술 아이디어 제안", "환경 캠페인 콘텐츠 제작", "친환경 트렌드 제안"]),
    "ISFJ": ("환경 수호자", ["재활용 체계 정리", "일회용품 줄이기", "자연과의 공존 강조"]),
    "ESTJ": ("환경 리더", ["지역 캠페인 리더 활동", "에너지 절약 계획 수립", "팀 단위 환경 보호"]),
    # 더 많은 결과 추가 가능
}

# Streamlit 앱 구현
st.title("기후감수성 MBTI 테스트")

# 사용자 답변 수집
answers = []
if "submitted" not in st.session_state:
    st.session_state["submitted"] = False

if not st.session_state["submitted"]:
    with st.form(key="quiz_form"):
        for i, question in enumerate(QUESTIONS):
            st.write(f"{i + 1}. {question}")
            answer = st.radio(
                f"q{i}",
                options=["그렇다", "아니다"],
                key=f"q{i}",
                index=1  # 기본값: '아니다'
            )
            answers.append(1 if answer == "그렇다" else 0)
        submitted = st.form_submit_button("결과 보기")
        if submitted:
            st.session_state["submitted"] = True
            st.session_state["answers"] = answers

# 결과 계산 및 출력
if st.session_state["submitted"]:
    answers = st.session_state["answers"]

    # MBTI 계산 로직
    e_score = sum(answers[:4])
    s_score = sum(answers[4:8])
    t_score = sum(answers[8:12])
    j_score = sum(answers[12:16])

    mbti = (
        ("E" if e_score >= 2 else "I") +
        ("S" if s_score >= 2 else "N") +
        ("T" if t_score >= 2 else "F") +
        ("J" if j_score >= 2 else "P")
    )

    result, actions = RESULTS.get(mbti, ("알 수 없음", ["환경 보호를 위한 다양한 방법을 시도해 보세요!"]))

    # 결과 출력
    st.subheader("테스트 결과")
    st.write(f"당신의 기후감수성 MBTI 유형은: **{result}**")
    st.write("추천 실천 방법:")
    st.write("- " + "\n- ".join(actions))

    # 다시 시작 버튼
    if st.button("다시 테스트하기"):
        st.session_state["submitted"] = False
        st.session_state["answers"] = []
