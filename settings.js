// settings.js

document.addEventListener('DOMContentLoaded', (event) => {
    loadSettings();
});

document.getElementById('settingsForm').addEventListener('submit', (event) => {
    event.preventDefault();
    saveSettings();
});

function loadSettings() {
    // Assuming you have an endpoint that fetches the current settings
    fetch('/api/settings')
        .then(response => response.json())
        .then(data => populateSettings(data))
        .catch(error => console.error('Error:', error));
}

function populateSettings(settings) {
    document.getElementById('numLinks').value = settings.numLinks;
}

function saveSettings() {
    let numLinks = document.getElementById('numLinks').value;

    if (!numLinks || numLinks < 6 || numLinks > 8) {
        alert('Please enter a number between 6 and 8 for interlinks.');
        return;
    }

    updateSettings(numLinks);
}

function updateSettings(numLinks) {
    const xhr = new XMLHttpRequest();
    const formData = new FormData();

    formData.append('numLinks', numLinks);

    xhr.open('POST', '/api/settings', true);
    xhr.onload = function () {
        if (this.status == 200) {
            alert('Settings updated successfully.');
        } else {
            alert('An error occurred while updating the settings.');
        }
    };

    xhr.send(formData);
}
