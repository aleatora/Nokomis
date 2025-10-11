from flask import Flask, render_template, request, jsonify
import os
from openai import OpenAI

app = Flask(__name__)
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """[YOUR FULL SYSTEM PROMPT HERE]"""

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message')
    
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": user_message}
    ]
    
    try:
        response = client.chat.completions.create(
            model="gpt-4",
            messages=messages,
            temperature=0.9,
            max_tokens=369
        )
        
        nokomis_response = response.choices[0].message.content.strip()
        return jsonify({'response': nokomis_response})
        
    except Exception as e:
        return jsonify({'response': 'The waters are still. Please try again.'})

if __name__ == '__main__':
    app.run(debug=True)
