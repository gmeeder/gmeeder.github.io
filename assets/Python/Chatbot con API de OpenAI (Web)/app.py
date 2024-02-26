from flask import Flask, render_template, request, jsonify
import openai

app = Flask(__name__)
openai.api_key = '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'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    prompt = request.form['prompt']
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prompt,
        max_tokens=100
    )
    return jsonify({'response': response['choices'][0]['text']})

if __name__ == '__main__':
    app.run(debug=True)
