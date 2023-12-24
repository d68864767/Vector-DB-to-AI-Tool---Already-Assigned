// article_selection.js

document.addEventListener('DOMContentLoaded', (event) => {
    fetchArticles();
});

document.getElementById('articleForm').addEventListener('submit', (event) => {
    event.preventDefault();
    let selectedArticle = document.getElementById('articleSelect').value;
    // You can use the selectedArticle for further processing
});

function fetchArticles() {
    // Assuming you have an endpoint that uses the ArticleService to fetch all articles
    fetch('/api/articles')
        .then(response => response.json())
        .then(data => populateArticleDropdown(data))
        .catch(error => console.error('Error:', error));
}

function populateArticleDropdown(articles) {
    let dropdown = document.getElementById('articleSelect');
    dropdown.length = 0;

    let defaultOption = document.createElement('option');
    defaultOption.text = 'Choose article...';

    dropdown.add(defaultOption);
    dropdown.selectedIndex = 0;

    articles.forEach(article => {
        let option = document.createElement('option');
        option.text = article.title;
        option.value = article.id;
        dropdown.add(option);
    });
}
