// Initialize song list and current song
let songList = [];
let currentSong = 0;

// Function to populate song list
function populateSongList() {
    // Add songs to the list
    songList = [
        { name: "Song 1", artist: "Artist 1" },
        { name: "Song 2", artist: "Artist 2" },
        { name: "Song 3", artist: "Artist 3" },
    ];

    // Populate the song list
    const songListElement = document.getElementById("song-list");
    songList.forEach((song) => {
        const songListItem = document.createElement("li");
        songListItem.textContent = `${song.name} by ${song.artist}`;
        songListElement.appendChild(songListItem);
    });
}

// Function to update song information
function updateSongInfo(song) {
    document.getElementById("song-name").textContent = song.name;
    document.getElementById("artist-name").textContent = song.artist;
}

// Function to play/pause song
function playPauseSong() {
    // Toggle play/pause button text
    const playPauseBtn = document.getElementById("play-pause-btn");
    if (playPauseBtn.textContent === "Play") {
        playPauseBtn.textContent = "Pause";
    } else {
        playPauseBtn.textContent = "Play";
    }
}

// Function to play next song
function playNextSong() {
    currentSong = (currentSong + 1) % songList.length;
    updateSongInfo(songList[currentSong]);
    playPauseSong();
}

// Function to play previous song
function playPrevSong() {
    currentSong = (currentSong - 1 + songList.length) % songList.length;
    updateSongInfo(songList[currentSong]);
    playPauseSong();
}

populateSongList();
updateSongInfo(songList[currentSong]);
document.getElementById("play-pause-btn").addEventListener("click", playPauseSong);
document.getElementById("next-btn").addEventListener("click", playNextSong);
document.getElementById("prev-btn").addEventListener("click", playPrevSong);
