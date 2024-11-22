from flask import Flask, render_template, jsonify, request
import random

app = Flask(__name__)

# Game variables
suits = []
values = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = []
player_hand = []
robot_hand = []


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/start-game', methods=['POST'])
def start_game():
    global suits, deck, player_hand, robot_hand

    # Reset hands and suits
    player_hand.clear()
    robot_hand.clear()

    suit_choice = request.json.get('suit_choice', '1')
    if suit_choice == "1":
        suits = ["♥", "♦", "♣", "♠"]
    elif suit_choice == "2":
        suits = ["😃", "😈", "😵", "🤢", "😨"]
    elif suit_choice == "3":
        suits = ["🤡", "👹", "👺", "👻", "👽", "👾", "🤖"]
    else:
        suits = ["♥", "♦", "♣", "♠"]

    # Create a new deck
    deck = [val + " of " + suit for val in values for suit in suits]
    random.shuffle(deck)

    return jsonify({"message": "Game started!", "deck_size": len(deck), "suits": suits})


@app.route('/shuffle', methods=['POST'])
def shuffle_deck():
    global deck
    if not deck:
        return jsonify({"error": "Deck is empty. Start the game first."}), 400
    random.shuffle(deck)
    return jsonify({"message": "Deck shuffled!", "deck_size": len(deck)})


@app.route('/pick', methods=['POST'])
def pick_cards():
    global player_hand, robot_hand, deck
    if not deck or len(deck) < 2:
        return jsonify({"error": "Not enough cards to pick. Please shuffle or start a new game."}), 400

    player_card = random.choice(deck)
    deck.remove(player_card)
    player_hand.append(player_card)

    robot_card = random.choice(deck)
    deck.remove(robot_card)
    robot_hand.append(robot_card)

    return jsonify({
        "message": "Cards picked!",
        "player_card": player_card,
        "robot_card": robot_card,
        "deck_size": len(deck)
    })


@app.route('/show-cards', methods=['GET'])
def show_cards():
    if not player_hand:
        return jsonify({"error": "You haven't picked any cards yet."}), 400
    return jsonify({"player_hand": player_hand})


@app.route('/check-winner', methods=['GET'])
def check_winner():
    if not player_hand or not robot_hand:
        return jsonify({"error": "No cards have been picked yet."}), 400

    player_score = sum(get_card_value(card) for card in player_hand)
    robot_score = sum(get_card_value(card) for card in robot_hand)

    if player_score > robot_score:
        winner = "Player"
    elif player_score < robot_score:
        winner = "Robot"
    else:
        winner = "It's a tie!"

    return jsonify({
        "player_score": player_score,
        "robot_score": robot_score,
        "winner": winner
    })


def get_card_value(card):
    value = card.split()[0]  # Extract card value
    if value == 'J':
        return 11
    elif value == 'Q':
        return 12
    elif value == 'K':
        return 13
    elif value == 'A':
        return 1
    return int(value)


if __name__ == '__main__':
    app.run(debug=False, port=8080)
