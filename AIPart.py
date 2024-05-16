from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def search():
    data = request.json
    input_value = data.get('value', '').strip()  # Changed key to 'value'
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
