//read url query
let queryString = window.location.search

//parse query string using URLSearhParams
params = new URLSearchParams(queryString)

//pass is to div
let mydiv = document.getElementById('mydiv')
mydiv.innerText = `${params.get('name')} ${params.get('last_name')}`

