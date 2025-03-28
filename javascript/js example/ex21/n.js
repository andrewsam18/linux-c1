let progress = document.getElementById('progress');
let song = document.getElementById('song');
let ctrlIcon = document.getElementById('ctrlIcon');
let progressUpdateInterval;

song.onloadedmetadata = function() {
    progress.max = song.duration;
    progress.value = song.currentTime;
};

function playPause() {
    if (ctrlIcon.classList.contains('fa-pause')) {
        song.pause();
        ctrlIcon.classList.remove('fa-pause');
        ctrlIcon.classList.add('fa-play');
        clearInterval(progressUpdateInterval);
    } else {
        song.play();
        ctrlIcon.classList.add('fa-pause');
        ctrlIcon.classList.remove('fa-play');
        progressUpdateInterval = setInterval(() => {
            progress.value = song.currentTime;
        }, 500);
    }
}

progress.onchange = function() {
    song.currentTime = progress.value;
    if (song.paused) {
        song.play();
        ctrlIcon.classList.add('fa-pause');
        ctrlIcon.classList.remove('fa-play');
        clearInterval(progressUpdateInterval);
        progressUpdateInterval = setInterval(() => {
            progress.value = song.currentTime;
        }, 500);
    }
};

song.addEventListener('ended', function() {
    song.currentTime = 0;
    progress.value = 0;
    ctrlIcon.classList.remove('fa-pause');
    ctrlIcon.classList.add('fa-play');
    clearInterval(progressUpdateInterval);
});