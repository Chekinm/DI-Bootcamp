//read url query
let queryString = window.location.search

//parse query string using URLSearhParams
params = new URLSearchParams(queryString)

let paramsObj = Object.fromEntries(params) 
let paramsJSON = JSON.stringify(paramsObj)

//pass is to div
let mydiv = document.getElementById('mydiv')

mydiv.innerText = paramsJSON

