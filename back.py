from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # allows frontend to talk to backend

FAKE_KEYWORDS = [
    "100% cure",
    "miracle",
    "secret revealed",
    "you won't believe",
    "guaranteed result",
    "shocking truth"
]

@app.route("/analyze", methods=["POST"])
def analyze():
    text = request.form.get("text", "").lower()
    image = request.files.get("image")

    if not text and not image:
        return jsonify({
            "status": "uncertain",
            "message": "Please enter text or upload an image."
        })

    score = sum(1 for word in FAKE_KEYWORDS if word in text)

    if score >= 2 and image:
        return jsonify({
            "status": "incorrect",
            "title": "Likely Misinformation",
            "details": [
                "Text contains sensational claims.",
                "Image does not verify the claim."
            ]
        })

    elif score == 0 and len(text) > 20:
        return jsonify({
            "status": "correct",
            "title": "Possibly Correct Information",
            "details": [
                "No common misinformation patterns detected.",
                "Still verify with trusted sources."
            ]
        })

    else:
        return jsonify({
            "status": "uncertain",
            "title": "Uncertain Information",
            "details": [
                "Insufficient evidence.",
                "Manual verification recommended."
            ]
        })
@app.route("/")
def home():
    return "Backend is running successfully!"

@app.route("/test")
def test():
    return jsonify({"status": "OK", "message": "API working"})  

if __name__ == "__main__":
    app.run(debug=True)


