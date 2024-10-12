from flask import Flask, request, jsonify
import time

app = Flask(__name__)

# Список реплікованих повідомлень
replicated_messages = []

@app.route('/replicate', methods=['POST'])
def replicate_message():
    message = request.json.get('message')
    if message:
        time.sleep(2)  # Затримка для тестування блокуючої реплікації
        replicated_messages.append(message)
        return jsonify({"status": "Message replicated"}), 200
    return jsonify({"error": "No message provided"}), 400

@app.route('/messages', methods=['GET'])
def get_replicated_messages():
    return jsonify(replicated_messages), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
