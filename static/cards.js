document.getElementById("start-game-btn").addEventListener("click", function () {
    const suitChoice = document.getElementById("suit-choice").value;
    fetch("/start-game", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ suit_choice: suitChoice })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("messages").innerText = data.message;
            enableButtons();
        });
});

document.getElementById("shuffle-btn").addEventListener("click", function () {
    fetch("/shuffle", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            document.getElementById("messages").innerText = data.message;
        });
});

document.getElementById("pick-card-btn").addEventListener("click", function () {
    fetch("/pick", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("messages").innerText = data.error;
            } else {
                document.getElementById("messages").innerText =
                    `You picked: ${data.player_card}, Robot picked: ${data.robot_card}`;
            }
        });
});

document.getElementById("show-cards-btn").addEventListener("click", function () {
    fetch("/show-cards")
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("messages").innerText = data.error;
            } else {
                document.getElementById("player-hand").innerText =
                    `Your hand: ${data.player_hand.join(", ")}`;
            }
        });
});

document.getElementById("check-winner-btn").addEventListener("click", function () {
    fetch("/check-winner")
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("messages").innerText = data.error;
            } else {
                document.getElementById("messages").innerText =
                    `Player Score: ${data.player_score}, Robot Score: ${data.robot_score}. Winner: ${data.winner}`;
            }
        });
});

function enableButtons() {
    document.getElementById("shuffle-btn").disabled = false;
    document.getElementById("pick-card-btn").disabled = false;
    document.getElementById("show-cards-btn").disabled = false;
    document.getElementById("check-winner-btn").disabled = false;
}
