import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.preprocessing import LabelEncoder

# 1. 데이터 불러오기
df = pd.read_csv("phising_dataset.csv")
X = df["message"]
y = df["label"]

# 라벨 인코딩
encoder = LabelEncoder()
y_encoded = encoder.fit_transform(y)

# 2. 텍스트 벡터화
vectorizer = CountVectorizer()
X_vec = vectorizer.fit_transform(X)

# 3. 모델 학습
model = MultinomialNB()
model.fit(X_vec, y_encoded)

# 4. 예측 테스트
test = ["이 문자가 스미싱일까요 아닐까요?"]
test_vec = vectorizer.transform(test)
pred = model.predict(test_vec)[0]
print("예측 결과:", "스미싱" if pred == 1 else "정상")
