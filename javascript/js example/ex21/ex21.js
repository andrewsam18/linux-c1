
let progress = document.getElementById('progress');
let song = document.getElementById('song');
let ctrlIcon = document.getElementById('ctrlIcon');

song.onloadedmetadata = function() {
    progress.max = song.duration;
    progress.value = song.currentTime;
}

// Update progress bar as song plays
song.addEventListener('timeupdate', function() {
    progress.value = song.currentTime;
});

// Handle progress bar seeking
progress.addEventListener('input', function() {
    song.currentTime = progress.value;
});

// Handle song ended
song.addEventListener('ended', function() {
    ctrlIcon.classList.remove('fa-pause');
    ctrlIcon.classList.add('fa-play');
});

function playPause() {
    // Corrected class check with quotes
    if (ctrlIcon.classList.contains('fa-pause')) {
        song.pause();
        ctrlIcon.classList.remove('fa-pause');
        ctrlIcon.classList.add('fa-play');
    } else {
        song.play();
        ctrlIcon.classList.add('fa-pause');
        ctrlIcon.classList.remove('fa-play');
        
        // Update progress continuously while playing
        setInterval(() => {
            progress.value = song.currentTime;
        }, 500);
    }
}   
   // Skip controls
   function forward() {
            song.currentTime = Math.min(song.currentTime + 10, song.duration);
        }

        function backward() {
            song.currentTime = Math.max(song.currentTime - 10, 0);
        }
   
