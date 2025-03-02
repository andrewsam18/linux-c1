let speech = new SpeechSynthesisUtterance();
let voices = [];
let voiceSelect = document.querySelector("select");

// Function to load voices
function loadVoices() {
    voices = window.speechSynthesis.getVoices();
    
    if (voices.length === 0) {
        setTimeout(loadVoices, 100); // Retry after a short delay
        return;
    }

    speech.voice = voices[0]; // Set default voice

    // Clear previous options
    voiceSelect.innerHTML = ""; 

    voices.forEach((voice) => {
        let option = new Option(`${voice.name} (${voice.lang})`, voice.name);
        voiceSelect.appendChild(option);
    });

    // Set a Tamil voice if available
    let tamilVoice = voices.find(voice => voice.lang === "ta-IN");
    if (tamilVoice) {
        speech.voice = tamilVoice;
        voiceSelect.value = tamilVoice.name;
    }
}

// Load voices on page load and when they change
window.speechSynthesis.onvoiceschanged = loadVoices;
setTimeout(loadVoices, 100);

// Change voice when selecting from the dropdown
voiceSelect.addEventListener("change", () => {
    let selectedVoice = voices.find(voice => voice.name === voiceSelect.value);
    if (selectedVoice) {
        speech.voice = selectedVoice;
    }
});

// Speak text when the button is clicked
document.querySelector("button").addEventListener("click", () => {
    speech.text = document.querySelector("textarea").value;
    window.speechSynthesis.speak(speech);
});
