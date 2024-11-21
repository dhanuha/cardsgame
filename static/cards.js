document.getElementById("shuffle-btn").addEventListener("click", function () {
    fetch("/shuffle", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            document.getElementById("messages").innerText = data.message;
        });
});

document.getElementById("draw-btn").addEventListener("click", function () {
    fetch("/draw", { method: "POST" })
        .then(response => response.json())
        .then(data => {
            if (data.error) {
                document.getElementById("messages").innerText = data.error;
            } else {
                document.getElementById("messages").innerText = 
                    `You drew: ${data.player_card}, Robot drew: ${data.robot_card}`;
            }
        });
});

document.getElementById("show-hand-btn").addEventListener("click", function () {
    fetch("/player-hand")
        .then(response => response.json())
        .then(data => {
            document.getElementById("player-hand").innerText = 
                `Your hand: ${data.player_hand.join(", ")}`;
        });
});
