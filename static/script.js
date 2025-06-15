document.addEventListener("DOMContentLoaded", function () {
    const input = document.getElementById("user-input");
    const sendBtn = document.getElementById("send-btn");
    const resetBtn = document.getElementById("reset-btn");
    const resignBtn = document.getElementById("resign-btn");
    const chatContainer = document.getElementById("chat-container");

    function sendMessage() {
        const msg = input.value.trim();
        if (!msg) return;

        // Display user message
        const userDiv = document.createElement("div");
        userDiv.className = "message user";
        userDiv.textContent = msg;
        chatContainer.appendChild(userDiv);

        // Clear input
        input.value = "";

        // Send to server
        fetch("/chat", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ msg }),
        })
            .then((res) => res.json())
            .then((data) => {
                const botDiv = document.createElement("div");
                botDiv.className = "message bot";
                botDiv.textContent = data.reply;
                chatContainer.appendChild(botDiv);
                chatContainer.scrollTop = chatContainer.scrollHeight;
            })
            .catch((err) => {
                const errDiv = document.createElement("div");
                errDiv.className = "message bot error";
                errDiv.textContent = "SRGBot malfunctioned. Probably your fault.";
                chatContainer.appendChild(errDiv);
            });
    }

    // Send on Enter
    input.addEventListener("keydown", function (event) {
        if (event.key === "Enter") {
            event.preventDefault();
            sendMessage();
        }
    });

    // Send button
    sendBtn.addEventListener("click", sendMessage);

    // Reset chat
    resetBtn.addEventListener("click", () => {
        chatContainer.innerHTML = "";
    });

    // Resign button
    resignBtn.addEventListener("click", () => {
        alert("SRGBot accepts your resignation. You're free now.");
        window.close(); // May not work unless opened via JS or in some browsers
    });
});
const input = document.getElementById("input"); // make sure your input has id="input"
const chatbox = document.getElementById("chatbox"); // make sure your chat div has id="chatbox"

input.addEventListener("keypress", function (e) {
    if (e.key === "Enter") {
        e.preventDefault();
        sendMessage();
    }
});

