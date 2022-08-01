function getArticles() {
  fetch("http://127.0.0.1:8000/articles/")
    .then((res) => res.json())
    .then((data) => {
      for (article of data) {
        let row = document.createElement("tr");
        let id = document.createElement("th");
        id.innerHTML = article.id;
        let title = document.createElement("th");
        title.innerHTML = article.title;
        let created = document.createElement("th");
        created.innerHTML = article.created_at;
        row.appendChild(id);
        row.appendChild(title);
        row.appendChild(created);
        elem = document.getElementById("articles");
        document.getElementById("articles").appendChild(row);
      }
    })
    .catch((err) => console.log(err));
}

function createArticle(data) {
  fetch("http://127.0.0.1:8000/articles/", {
    method: "post",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(data),
  });
}
