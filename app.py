from flask import Flask, render_template, request, jsonify, session
from googletrans import Translator, LANGUAGES
from datetime import datetime
import os

app = Flask(__name__,
    static_url_path='/static',
    static_folder='static'
)
app.secret_key = os.environ.get('FLASK_SECRET_KEY', 'your-secret-key')

#create a translator object
translator = Translator()

# language names
LANGUAGE_NAMES = {
    'en': 'English',
    'ar': 'Arabic',
    'bg': 'Bulgarian',
    'de': 'German',
    'el': 'Greek',
    'es': 'Spanish',
    'fr': 'French',
    'hi': 'Hindi',
    'it': 'Italian',
    'ja': 'Japanese',
    'ko': 'Korean',
    'nl': 'Dutch',
    'pl': 'Polish',
    'pt': 'Portuguese',
    'ru': 'Russian',
    'sw': 'Swahili',
    'th': 'Thai',
    'tr': 'Turkish',
    'ur': 'Urdu',
    'vi': 'Vietnamese',
    'zh': 'Chinese'
}

def detect_language(text):
    try:
        # use google translator
        detection = translator.detect(text)
        
        return {
            'language': detection.lang,
            'language_name': LANGUAGE_NAMES.get(detection.lang, LANGUAGES.get(detection.lang, detection.lang.upper())),
            'confidence': round(detection.confidence * 100, 2),
            'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
    except Exception as e:
        print(f"Error detecting language: {e}")
        return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/detect', methods=['POST'])
def detect_route():
    text = request.json.get('text', '')
    if not text:
        return jsonify({'error': 'No text provided'}), 400
    
    result = detect_language(text)
    if result:
        # save history
        if 'history' not in session:
            session['history'] = []
        history = session['history']
        history.append({
            'text': text[:100] + '...' if len(text) > 100 else text,
            'result': result
        })
        session['history'] = history[-10:]
        return jsonify(result)
    return jsonify({'error': 'Detection failed'}), 500

@app.route('/history', methods=['GET'])
def get_history():
    return jsonify(session.get('history', []))

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['history'] = []
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    port = os.environ.get('PORT', 10000)
    app.run(host='0.0.0.0', port=port)