from flask import Flask, request, jsonify, render_template
from Agents import MotivateBot, TherapyBot, VentBot, CalmBot


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    agent_name = data.get('agent', '')

    if not user_message or not agent_name:
        return jsonify({'response': "Invalid input."}), 400

    # Route to correct agent
    if agent_name == "therapist":
        ai_response = TherapyBot.respond(user_message)
    elif agent_name == "motivator":
        ai_response = MotivateBot.respond(user_message)
    elif agent_name == "vent":
        ai_response = VentBot.respond(user_message)
    elif agent_name == "calm":
        ai_response = CalmBot.respond(user_message)
    else:
        ai_response = "Sorry, I don't know that AI agent."

    return jsonify({'response': ai_response})

if __name__ == '__main__':
    app.run(debug=True)