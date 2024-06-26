
from openai import OpenAI
from flask import Flask, request, jsonify
from flask_cors import CORS
from script import get_openai_response

app = Flask(__name__)
CORS(app)
@app.route('/', methods=['POST'])  # Correct route definition
def search():
    data = request.json
    input_value = data.get('input', '').strip()  # Changed key to 'input'
    if not input_value:
        return jsonify({'error': 'Invalid input: Value is empty or null'})
    else:
        print('You searched for:', input_value)
        result = get_openai_response(input_value)
        print(result)
        return jsonify({'result': result})
        



if __name__ == '__main__':
    app.run(debug=True)

