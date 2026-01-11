import nltk
nltk.download('stopwords')
from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

model = pickle.load(open("models/model.pkl", "rb"))
vectorizer = pickle.load(open("models/vectorizer.pkl", "rb"))

TRUSTED_ENTITIES = [
    "isro", "nasa", "who", "un", "government",
    "ministry", "supreme court", "bbc", "reuters"
]

SENSATIONAL_WORDS = [
    "shocking", "breaking", "secret",
    "miracle", "instantly", "cure"
]

def credibility_rules(text):
    score = 50
    text = text.lower()

    for t in TRUSTED_ENTITIES:
        if t in text:
            score += 20

    for w in SENSATIONAL_WORDS:
        if w in text:
            score -= 15

    if "sources say" in text or "experts say" in text:
        score -= 10

    return max(0, min(score, 100))

@app.route("/", methods=["GET", "POST"])
def index():
    result = score = confidence = None

    if request.method == "POST":
        news = request.form["news"]

        # ML probability
        vec = vectorizer.transform([news])
        prob_real = model.predict_proba(vec)[0][1] * 100

        # Rule score
        rule_score = credibility_rules(news)

        # 🔥 Professional fusion
        final_score = int((0.6 * rule_score) + (0.4 * prob_real))

        if final_score >= 75:
            result = "LIKELY CREDIBLE"
        elif final_score >= 50:
            result = "NEEDS VERIFICATION"
        else:
            result = "HIGHLY SUSPICIOUS"

        score = final_score
        confidence = f"{prob_real:.2f}%"

    return render_template(
        "index.html",
        result=result,
        score=score,
        confidence=confidence
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

