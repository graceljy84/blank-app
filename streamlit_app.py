import streamlit as st

# 세션 상태(Session State) 초기화
# 'submitted' 키가 세션 상태에 없으면 False로 설정
if 'submitted' not in st.session_state:
    st.session_state.submitted = False

# MBTI 문항 및 선택지
# 각 문항은 사전(dictionary) 형태로 구성
questions = [
    {
        "question": "1. 주말을 보내는 당신의 방식은?",
        "options": ["(E) 친구들과 함께하는 파티나 모임", "(I) 집에서 조용히 보내는 휴식"],
        "type": ("E", "I")
    },
    {
        "question": "2. 새로운 기술을 배울 때 선호하는 방법은?",
        "options": ["(S) 구체적인 예제와 실제 데이터를 통해 학습", "(N) 전체적인 개념과 미래 가능성을 먼저 파악"],
        "type": ("S", "N")
    },
    {
        "question": "3. 팀 프로젝트에서 갈등이 생겼을 때 당신의 선택은?",
        "options": ["(T) 논리적이고 객관적인 사실에 기반하여 결정", "(F) 팀원들의 감정과 관계를 우선적으로 고려"],
        "type": ("T", "F")
    },
    {
        "question": "4. 여행 계획을 세울 때 당신은?",
        "options": ["(J) 출발 전 모든 일정을 꼼꼼하게 계획", "(P) 기본적인 계획만 세우고 상황에 따라 유연하게 행동"],
        "type": ("J", "P")
    },
    {
        "question": "5. 처음 만나는 사람들과의 대화에서 당신은?",
        "options": ["(E) 먼저 다가가 대화를 시작하는 편", "(I) 다른 사람이 말을 걸어주기를 기다리는 편"],
        "type": ("E", "I")
    },
    {
        "question": "6. 영화를 보고 나서 당신의 감상은?",
        "options": ["(S) 영화의 구체적인 장면이나 대사를 기억", "(N) 영화가 담고 있는 숨겨진 의미나 상징을 생각"],
        "type": ("S", "N")
    },
    {
        "question": "7. 친구가 고민을 털어놓을 때 당신의 반응은?",
        "options": ["(T) 문제 해결을 위한 현실적인 조언을 제공", "(F) 친구의 감정에 공감하며 위로의 말을 건넴"],
        "type": ("T", "F")
    },
    {
        "question": "8. 업무를 처리할 때 선호하는 방식은?",
        "options": ["(J) 마감 기한을 철저히 지키고 체계적으로 관리", "(P) 마감 기한에 임박했을 때 집중해서 처리"],
        "type": ("J", "P")
    }
]

# MBTI 유형별 학습 스타일 설명
learning_styles = {
    "ISTJ": "실용적이고 체계적인 학습을 선호합니다. 구체적인 사실과 데이터를 바탕으로 꾸준히 학습하는 스타일입니다.",
    "ISFJ": "세심하고 책임감이 강하여, 다른 사람에게 도움이 되는 지식을 학습할 때 동기부여를 받습니다.",
    "INFJ": "통찰력이 뛰어나고 장기적인 비전을 중요시합니다. 깊이 있는 이론과 개념을 탐구하는 것을 즐깁니다.",
    "INTJ": "독립적이고 논리적인 학습자입니다. 복잡한 이론을 체계적으로 분석하고 자신만의 방식으로 재구성하는 능력이 뛰어납니다.",
    "ISTP": "경험을 통해 배우는 것을 선호합니다. 직접 부딪히고 시행착오를 겪으며 원리를 터득하는 실습형 학습자입니다.",
    "ISFP": "호기심이 많고 개방적입니다. 딱딱한 이론보다는 자유로운 환경에서 자신의 관심사를 탐구하는 것을 좋아합니다.",
    "INFP": "자신의 가치관과 신념에 부합하는 내용을 학습할 때 가장 큰 흥미를 느낍니다. 창의적이고 이상적인 아이디어를 좋아합니다.",
    "INTP": "지적 호기심이 왕성한 논리적인 사색가입니다. 복잡한 문제의 원리를 파고드는 것을 즐기며, 토론을 통해 아이디어를 발전시킵니다.",
    "ESTP": "활동적이고 사교적입니다. 직접적인 경험과 실제 활동을 통해 배우는 것을 선호하며, 이론보다는 실전에 강합니다.",
    "ESFP": "사람들과 어울리며 배우는 것을 즐깁니다. 긍정적이고 재미있는 학습 환경에서 가장 높은 효율을 보입니다.",
    "ENFP": "열정적이고 상상력이 풍부합니다. 다양한 가능성을 탐색하고, 창의적인 아이디어를 나누는 협력 학습을 선호합니다.",
    "ENTP": "도전적이고 재치 있는 토론을 즐깁니다. 기존의 방식에 의문을 제기하고 새로운 아이디어를 탐구하는 것을 좋아합니다.",
    "ESTJ": "체계적이고 효율적인 학습을 추구합니다. 목표를 설정하고 계획에 따라 학습하며, 실질적인 결과를 중요시합니다.",
    "ESFJ": "다른 사람들과 협력하고 도우며 배우는 것을 좋아합니다. 조화로운 학습 분위기에서 동기부여를 받습니다.",
    "ENFJ": "사람들의 성장을 돕는 것에 큰 보람을 느낍니다. 다른 사람을 가르치거나 이끌면서 스스로도 배우는 리더형 학습자입니다.",
    "ENTJ": "전략적이고 목표 지향적인 학습자입니다. 장기적인 목표를 세우고, 이를 달성하기 위해 효율적인 학습 계획을 수립하고 실행합니다."
}

# --- 앱 UI 구성 ---
st.title("🚀 MBTI 학습 유형 진단")
st.write("간단한 질문을 통해 자신에게 맞는 학습 스타일을 알아보세요!")

# 답변을 저장할 리스트
answers = []

# st.form을 사용하여 모든 질문에 답변 후 한 번에 제출
with st.form("mbti_form"):
    # 각 질문에 대해 라디오 버튼 생성
    for i, q in enumerate(questions):
        answer = st.radio(q["question"], q["options"], key=f"q{i}")
        answers.append(answer)

    # 제출 버튼
    submitted = st.form_submit_button("결과 확인하기")

# 제출 버튼이 클릭되면, st.session_state.submitted를 True로 변경
if submitted:
    st.session_state.submitted = True

# st.session_state.submitted가 True일 때만 결과를 표시
if st.session_state.submitted:
    # MBTI 점수 계산
    scores = {'E': 0, 'I': 0, 'S': 0, 'N': 0, 'T': 0, 'F': 0, 'J': 0, 'P': 0}
    for i, answer in enumerate(answers):
        # 선택한 옵션에 따라 유형 점수 증가
        selected_option_index = questions[i]["options"].index(answer)
        mbti_type_char = questions[i]["type"][selected_option_index]
        scores[mbti_type_char] += 1

    # 최종 MBTI 유형 결정
    result = ""
    result += "E" if scores['E'] > scores['I'] else "I"
    result += "S" if scores['S'] > scores['N'] else "N"
    result += "T" if scores['T'] > scores['F'] else "F"
    result += "J" if scores['J'] > scores['P'] else "P"

    # 결과 출력
    st.subheader(f"📈 당신의 MBTI 학습 유형은: {result}")
    st.info(learning_styles.get(result, "결과를 분석 중입니다."))
    st.success("진단이 완료되었습니다. 이 결과를 바탕으로 자신에게 맞는 학습 전략을 세워보세요!")
    
    # 다시 시작 버튼
    if st.button("다시 진단하기"):
        st.session_state.submitted = False
        st.experimental_rerun() # 앱을 새로고침하여 처음부터 다시 시작