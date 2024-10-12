from flask import Flask, request, jsonify
import requests
import logging

# Створюємо інстанс Flask додатку
app = Flask(__name__)

# Налаштовуємо логування
logging.basicConfig(level=logging.DEBUG)

# Список повідомлень
messages = []

# Список secondary серверів
secondaries = ["http://secondary:5000"]

@app.route('/messages', methods=['POST'])
def post_message():
    logging.debug(f"Request data: {request.data}")
    message = request.json.get('message')
    if message:
        logging.info(f"Received message: {message}")
        messages.append(message)

        # Реплікація повідомлення на всі secondary
        for secondary in secondaries:
            try:
                logging.info(f"Replicating message to {secondary}")
                response = requests.post(f"{secondary}/replicate", json={"message": message})
                if response.status_code == 200:
                    logging.info(f"Successfully replicated to {secondary}")
                else:
                    logging.error(f"Failed to replicate to {secondary}")
                    return jsonify({"error": "Failed to replicate"}), 500
            except requests.exceptions.RequestException:
                logging.error(f"Secondary {secondary} unavailable")
                return jsonify({"error": "Secondary unavailable"}), 500

        return jsonify({"status": "Message replicated"}), 200
    else:
        logging.error("No message provided in POST request")
        return jsonify({"error": "No message provided"}), 400

@app.route('/messages', methods=['GET'])
def get_messages():
    logging.info("GET request received for all messages")
    return jsonify(messages), 200

if __name__ == '__main__':
    logging.info("Starting Master server...")
    app.run(host='0.0.0.0', port=5000)
