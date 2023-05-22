// //  ex1

// const s = (a,b) => a+b


// // ex2

// function kgTogr(weigth) {
//     return weigth*1000
// }

// console.log(kgTogr(1.5))

// const kgTogrExpression = function (weigth) {
//     return weigth*1000
// }

// console.log(kgTogrExpression(1.5))

// // declaration is a function declaration using key word function
// // expression when function is managed like a variable 

// const kggr = (weigth) => weigth*1000
// console.log (kggr(1.5))


// ex3

(function (numOfChildren, partnersName, geographicLocation, jobTitle) {
    let div = document.createElement('div')
    div.innerText = `You will be a ${jobTitle} in ${geographicLocation}, and married to ${partnersName} with ${numOfChildren} kids.`

    let body = document.getElementsByTagName("body")
    console.log(body[0])
    body[0].appendChild(div)
    
})('sdf','sdf','sdfsdfs','sdfsdfsdf');


(function (userName) {
    let span = document.createElement('span')
    span.innerText = `${userName}`
    span.className = "navbar-text"
    let navBar = document.getElementById("navbarText")
    console.log(navBar)
    navBar.appendChild(span)
    
})('Vasya');


//


