from flask import Flask, render_template, request, send_file, jsonify
from gtts import gTTS
import uuid, os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/speak', methods=['POST'])
def speak():
    text = request.form.get('text', '').strip()
    if not text:
        return jsonify({"error": "Empty text"}), 400

    lang = "hi" if any('\u0900' <= ch <= '\u097f' for ch in text) else "en"

    filename = f"static/{uuid.uuid4().hex}.mp3"
    tts = gTTS(text=text, lang=lang, slow=False)
    tts.save(filename)
    return jsonify({"path": filename})

if __name__ == '__main__':
    os.makedirs('static', exist_ok=True)
    app.run(debug=True)
