
var button = document.getElementById("fetch-quote")
button.addEventListener('click', displayRandomQuote)

async function getRandomQuote(){    
    return fetch("https://api.prezidential.xyz/api/random")
    .then(response => response.json())
    .then(obj => {
            console.log(obj)
            return JSON.stringify(obj, null, "\t")
        })
}

function displayRandomQuote(e){
    e.preventDefault()
    button.disabled = true
    button.className = "bg-rose-300 text-white active:bg-rose-800 font-bold uppercase text-xs px-4 py-3 \
        rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 my-5 false"
    var container = document.getElementById("returned-quote")
    getRandomQuote()
        .then(data =>  {
            var html = Prism.highlight(data, Prism.languages.json, "json")
            container.innerHTML = html
            button.disabled = false
            button.className = "bg-rose-500 text-white active:bg-rose-800 font-bold uppercase text-xs px-4 py-3 \
        rounded shadow hover:shadow-md outline-none focus:outline-none mr-1 my-5 false"
        })
        .catch(error => {
            console.error("Error displaying random quote: ", error)
        });
}
