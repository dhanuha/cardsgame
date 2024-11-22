# Card Game Web Application

## Description
The **Card Game Web Application** is a web-based implementation of a fun and interactive card game. The game allows players to draw cards from a shuffled deck and compete against a robot to determine the winner based on the card values. The game features multiple suit options, shuffling functionality, and a scoring mechanism to evaluate who wins.

This project demonstrates the integration of Python (Flask) as the backend, and HTML, CSS, and JavaScript for the frontend, ensuring a smooth and engaging user experience.

---

## Features
- **Suit Selection**: Choose from three different sets of suits:
  1. Classic suits: `♥`, `♦`, `♣`, `♠`
  2. Emoji suits: 😃, 😈, 😵, 🤢, 😨
  3. Fantasy suits: 🤡, 👹, 👺, 👻, 👽, 👾, 🤖
  
- **Shuffle the Deck**: The player can shuffle the deck to randomize card order.

- **Pick Cards**: Both the player and the robot draw cards from the deck.

- **Show Cards**: Displays the cards in the player's hand.

- **Check Winner**: Determines the winner based on the card values using these rules:
  1. **Card Value Comparison**: Cards are scored (`J=11`, `Q=12`, `K=13`, `A=1`), and the total score determines the winner.
  2. **Tie Handling**: If scores are equal, it's declared a tie.

---

## Technologies Used
- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Communication**: REST API with JSON responses
- **Styling**: Responsive CSS for a clean and simple user interface

---

## How to Run the Project

### 1. Clone the Repository
git clone <https://github.com/dhanuha/card-game.git>
cd card-game

### 2. Set up the virtual environment:
python3 -m venv .venv source .venv/bin/activate # For Linux/Mac
.venv\Scripts\activate # For Windows

### 3. Install dependencies:
pip install flask

### 4. Run the Flask app:
python app.py
The Flask development server will start, and you’ll see a message like this:
 Running on http://127.0.0.1:8080/

### 5. Open a browser and navigate to:
<http://127.0.0.1:8080/>


## How to Play
1. Select a suit set from the dropdown menu and click **Start Game**.
   <img width="680" alt="gamestarted" src="https://github.com/user-attachments/assets/ebb83058-1f39-4d37-b980-d603b8264b43">
2. Use the buttons to:
- **Shuffle Deck**: Randomize the deck.
- **Pick Cards**: Draw cards for both the player and the robot.
- <img width="705" alt="pickcards" src="https://github.com/user-attachments/assets/806f0dd0-5079-4e13-89e9-1f3809e1afba">
- **Show My Cards**: Display the player's hand.
- <img width="702" alt="showmycards" src="https://github.com/user-attachments/assets/05c286e3-17ea-4258-ac40-579de9559a76">
- **Check Winner**: Calculate the scores and determine the winner.
- <img width="715" alt="showwinner" src="https://github.com/user-attachments/assets/8efbc43c-9852-405d-a8ee-83ea94e50404">
3. Repeat or restart the game as desired.

## Game Logic
- The game uses a standard deck of cards with customizable suits.
- Players draw cards alternately, and their scores are calculated based on card values.
- The player with the highest score wins. Ties are handled gracefully.

## Project Structure
<img width="488" alt="projectstructure" src="https://github.com/user-attachments/assets/a0015702-61fb-4dba-b8c9-a24f8b8cba02">


## Future Enhancements
- Add a login system for saving player progress and scores.
- Introduce more complex game rules and additional features.
- Implement animations for card shuffling and drawing.
- Expand the game for multiplayer functionality.

## About the Developer
This project was created as a learning experience to demonstrate the use of Python, Flask, and web technologies in building interactive applications. It showcases backend logic, RESTful API integration, and a user-friendly frontend.
