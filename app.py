from flask import Flask, render_template_string, request
import datetime

app = Flask(__name__)

# 샘플 콘텐츠 데이터 (일자별 데이터 관리 가능)
daily_articles = {
    "인문": {
        "title": "고대 그리스 철학과 민주주의",
        "content": [
            "고대 그리스는 서양 철학과 정치 사상의 발상지로 여겨집니다. 특히 소크라테스, 플라톤, 아리스토텔레스 등은 인간 존재와 지식, 윤리, 국가에 대한 근본적인 질문을 탐구하였습니다.",
            "소크라테스는 문답법을 통해 진리를 찾고자 했고, 플라톤은 이데아론을 통해 보이는 세계 너머의 진리 세계를 주장했습니다. 아리스토텔레스는 경험과 논리를 중시하며 학문적 분류 체계를 발전시켰습니다.",
            "한편, 고대 아테네에서는 직접 민주주의가 시행되어 시민들이 광장에서 법률을 제정하고 정책을 결정하는 데 참여했습니다. 이는 현대 민주주의의 원형으로 평가받습니다.",
            "고대 그리스의 철학과 정치 제도는 인간의 이성과 공동체 정신의 가치를 강조하며, 오늘날까지도 큰 영향을 끼치고 있습니다."
        ],
        "question": "플라톤이 주장한 '이데아'는 무엇을 의미하나요?",
        "answer_keywords": ["진리", "세계"]
    }
}

# HTML 템플릿
html_template = """
<!DOCTYPE html>
<html lang="ko">
<head>
    <meta charset="UTF-8">
    <title>{{ title }}</title>
    <style>
        body { font-family: sans-serif; padding: 2em; line-height: 1.6; max-width: 800px; margin: auto; }
        .question { margin-top: 2em; }
        .result { font-weight: bold; color: green; }
        .error { font-weight: bold; color: red; }
    </style>
</head>
<body>
    <h1>{{ category }}: {{ title }}</h1>
    {% for paragraph in content %}
        <p>{{ paragraph }}</p>
    {% endfor %}
    <div class="question">
        <h3>이해도 점검</h3>
        <p>{{ question }}</p>
        <form method="post">
            <input type="text" name="answer" placeholder="여기에 답변을 입력하세요" style="width: 100%; padding: 0.5em;">
            <br><br>
            <button type="submit">제출</button>
        </form>
        {% if result is not none %}
            <p class="{{ 'result' if result else 'error' }}">
                {{ '정답입니다!' if result else '틀렸습니다. 다시 생각해보세요.' }}
            </p>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def daily_article():
    category = "인문"  # 날짜 기반으로 랜덤하게 선택 가능 (간단히 인문 고정)
    article = daily_articles[category]
    user_answer = request.form.get("answer", "")
    result = None

    if request.method == "POST":
        result = all(keyword in user_answer for keyword in article["answer_keywords"])

    return render_template_string(
        html_template,
        category=category,
        title=article["title"],
        content=article["content"],
        question=article["question"],
        result=result
    )

if __name__ == "__main__":
    app.run(debug=True)
