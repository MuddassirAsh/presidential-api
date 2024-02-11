
var button = document.getElementById("fetch-quote")
button.addEventListener('click', displayRandomQuote);

async function getRandomQuote(){    
    return fetch("http://localhost:8000/api/random")
    .then(response => response.json())
    .then(obj => {
            console.log(obj)
            return JSON.stringify(obj, null, "\t")
        })
}

function displayRandomQuote(){
var container = document.getElementById("returned-quote")
    getRandomQuote()
        .then(data =>  {
            var html = Prism.highlight(data, Prism.languages.json, "json")
            container.innerHTML = html
        })
        .catch(error => {
            console.error("Error displaying random quote: ", error);
        });
}
