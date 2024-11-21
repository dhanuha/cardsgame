from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Game variables
suits = ["♥", "♦", "♣", "♠"]
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [val + " of " + suit for val in values for suit in suits]
player_hand = []
robot_hand = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shuffle', methods=['POST'])
def shuffle_deck():
    global deck
    random.shuffle(deck)
    return jsonify({"message": "Deck shuffled!", "deck_size": len(deck)})

@app.route('/draw', methods=['POST'])
def draw_cards():
    global player_hand, robot_hand, deck
    if len(deck) < 2:
        return jsonify({"error": "Not enough cards in the deck!"})
    player_card = deck.pop()
    robot_card = deck.pop()
    player_hand.append(player_card)
    robot_hand.append(robot_card)
    return jsonify({"player_card": player_card, "robot_card": robot_card, "deck_size": len(deck)})

@app.route('/player-hand', methods=['GET'])
def show_player_hand():
    return jsonify({"player_hand": player_hand})

if __name__ == '__main__':
    app.run(debug=True, port=8080)
