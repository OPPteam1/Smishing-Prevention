# phishing_app.py
import streamlit as st
import joblib  # 또는 pickle
import re

# 📦 모델 불러오기
model = joblib.load('phishing_model.pkl')  # 예: 저장된 모델 파일명
vectorizer = joblib.load('vectorizer.pkl')  # 텍스트 전처리 벡터라이저

# 🔧 텍스트 전처리 함수 예시 (필요시 수정)
def clean_text(text):
    text = re.sub(r'\W+', ' ', text)  # 특수문자 제거
    return text.lower().strip()

# 🎨 Streamlit UI 구성
st.title("📮 피싱 문자 탐지 시스템")
st.write("문자 메시지나 이메일 내용을 입력해주세요. 모델이 피싱 여부를 판별합니다.")

# 📥 입력창
user_input = st.text_area("메시지 입력", height=150)

# 🔍 예측 버튼
if st.button("피싱 여부 확인"):
    if user_input.strip() == "":
        st.warning("⚠️ 메시지를 입력해주세요.")
    else:
        # 전처리 & 예측
        cleaned = clean_text(user_input)
        vec = vectorizer.transform([cleaned])
        prediction = model.predict(vec)

        # 출력
        if user_input.strip() <= 2:
            st.error("🚨 문자가 너무 짧아 구별이 어렵습니다!")
        else if prediction[0] == 1:
            st.error("🚨 피싱 가능성이 높은 메시지입니다!")
        else:
            st.success("✅ 일반 메시지로 판단됩니다.")
