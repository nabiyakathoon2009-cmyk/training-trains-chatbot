
// =========================
// 💬 AI CHAT
// =========================
async function sendMessage() {

    let input = document.getElementById("userInput");
    let chatBox = document.getElementById("chatBox");

    let text = input.value;
    if (text === "") return;

    chatBox.innerHTML += "<div class='user-message'>" + text + "</div>";

    let response = await fetch("/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: text })
    });

    let data = await response.json();

    chatBox.innerHTML += "<div class='bot-message'>" + data.reply + "</div>";

    input.value = "";
}


// =========================
// 🔘 QUICK BUTTONS
// =========================
window.quickMessage = function(type) {

    let chatBox = document.getElementById("chatBox");

    let msg = "";

    if(type === "about"){
        msg = "Training Trains AI Internship Platform 🤖";
    }
    else if(type === "domains"){
        msg = "Domains: AI, Web Dev, Cybersecurity, Cloud ☁️";
    }
    else if(type === "duration"){
        msg = "Duration: 1-3 Months ⏳";
    }
    else if(type === "certificate"){
        msg = "Certificate provided after completion 🎓";
    }
    else if(type === "contact"){
        msg = "Contact: trainingtrains@gmail.com 📩";
    }

    chatBox.innerHTML += "<div class='bot-message'>" + msg + "</div>";
};


// =========================
// 📝 APPLY FORM SAVE
// =========================
async function applyInternship() {

    let inputs = document.querySelectorAll(".internship-form input");

    let data = {
        name: inputs[0].value,
        email: inputs[2].value,
        college: inputs[4].value,
        domain: document.querySelector(".internship-form select").value
    };

    let res = await fetch("/apply", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    let result = await res.json();

    alert(result.message);
}


// =========================
// 🎤 VOICE
// =========================
window.startVoice = function () {

    let SpeechRecognition = window.SpeechRecognition || window.webkitSpeechRecognition;

    if (!SpeechRecognition) {
        alert("Voice not supported ❌");
        return;
    }

    let recognition = new SpeechRecognition();

    recognition.onresult = function(event){
        document.getElementById("userInput").value = event.results[0][0].transcript;
    };

    recognition.start();
};
async function generateCertificate() {

    let name = document.querySelector(".certificate-section input").value;
    let domain = document.querySelector(".internship-form select").value;

    let res = await fetch("/certificate", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            name: name,
            domain: domain
        })
    });

    let data = await res.json();

    alert(data.message + "\nFile: " + data.file);
}