from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text = request.form['text']
        translations = {
            'en': GoogleTranslator(source='es', target='en').translate(text),
            'fr': GoogleTranslator(source='es', target='fr').translate(text),
            'it': GoogleTranslator(source='es', target='it').translate(text),
            'de': GoogleTranslator(source='es', target='de').translate(text),
        }
        return render_template('index.html', translations=translations)
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)



"""
from flask import Flask, render_template, request
from deep_translator import GoogleTranslator

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        text_to_translate = request.form['text_to_translate']
        translated_texts = {
            'English': GoogleTranslator(source='auto', target='en').translate(text_to_translate),
            'French': GoogleTranslator(source='auto', target='fr').translate(text_to_translate),
            'Italian': GoogleTranslator(source='auto', target='it').translate(text_to_translate),
            'German': GoogleTranslator(source='auto', target='de').translate(text_to_translate)
        }
        return render_template('index.html', translated_texts=translated_texts)
    return render_template('index.html', translated_texts=None)

if __name__ == '__main__':
    app.run(debug=True)
"""