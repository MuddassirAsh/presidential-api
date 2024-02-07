var button = document.getElementById("fetch-quote")
button.addEventListener('click', getRandomQuote);

var text = document.getElementById("returned-quote")

function getRandomQuote(){    
    fetch('https://animechan.xyz/api/random')
    .then(response => response.json())
    .then(quote => text.innerText = quote.quote);

}