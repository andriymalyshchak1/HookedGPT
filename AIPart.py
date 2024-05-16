from flask import Flask, request, jsonify
from flask_cors import CORS

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
        # Process input_value as needed (e.g., use it as a prompt for the OpenAI API)
        # For demonstration, let's return a dummy result
        result = 'Dummy result for: ' + input_value
        return jsonify({'result': result})



if __name__ == '__main__':
    app.run(debug=True)

