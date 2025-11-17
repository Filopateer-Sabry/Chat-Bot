from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import cohere

app = Flask(__name__)
CORS(app)

co = cohere.Client("lQa4OIvkZPgz59dtqewJSJdDn9Q5ilG98ZCqmZuz") 

@app.route('/', methods=['GET'])
def home():
    return render_template("index.html") 

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    message = data.get("message", "")

    if not message:
        return jsonify({"error": "No message provided."}), 400

    try:
        response = co.chat(message=message)
        return jsonify({"response": response.text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    
if __name__ == '__main__':
    app.run(debug=True)