// sitemap_upload.js

document.addEventListener('DOMContentLoaded', (event) => {
    const uploadForm = document.getElementById('uploadForm');
    const uploadButton = document.getElementById('uploadButton');

    uploadButton.addEventListener('click', (e) => {
        e.preventDefault();
        handleFormSubmit(uploadForm);
    });
});

function handleFormSubmit(form) {
    const formData = new FormData(form);
    const file = formData.get('sitemapFile');
    const numLinks = formData.get('numLinks');

    if (!file) {
        alert('Please select a sitemap file to upload.');
        return;
    }

    if (!numLinks || numLinks < 6 || numLinks > 8) {
        alert('Please enter a number between 6 and 8 for interlinks.');
        return;
    }

    uploadSitemap(file, numLinks);
}

function uploadSitemap(file, numLinks) {
    const xhr = new XMLHttpRequest();
    const formData = new FormData();

    formData.append('sitemapFile', file);
    formData.append('numLinks', numLinks);

    xhr.open('POST', '/upload_sitemap', true);
    xhr.onload = function () {
        if (this.status == 200) {
            alert('Sitemap uploaded successfully.');
        } else {
            alert('An error occurred while uploading the sitemap.');
        }
    };

    xhr.send(formData);
}
