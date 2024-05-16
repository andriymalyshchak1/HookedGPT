from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/search', methods=['POST'])
def search():
    data = request.json
    input_value = data.get('value', '').strip()
    if not input_value:
        return jsonify({'error': 'Invalid input: Value is empty or null'})
    else:
        print('You searched for:', input_value)
        return jsonify({'input_value': input_value})

if __name__ == '__main__':
    app.run(debug=True)