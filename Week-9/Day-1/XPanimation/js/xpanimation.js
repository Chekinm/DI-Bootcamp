
// Part I
// In your Javascript file, using setTimeout, call a function after 2 seconds.
// The function will alert “Hello World”.
function sayHello() {
    alert('HelloWorld')
}
setTimeout (sayHello,3000)

// Part II
// In your Javascript file, using setTimeout, call a function
// after 2 seconds.
// The function will add a new paragraph <p>Hello World</p> 
// to the <div id="container">.


//we have defined paretn and child to be added
//lets create function to do this, so that we can postpone it
let parentEl = document.getElementById("container")
let childEl = document.createElement('p')
childEl.textContent = 'Hello World'

function addParaOnce(parentEl, childEl) {

    parentEl.appendChild(childEl)
}

setTimeout (addParaOnce,1000, parentEl, childEl)

// ----Part III

function addPara() {
    let parentEl = document.getElementById("container")
    let childEl = document.createElement('p')
    childEl.textContent = 'I say Helloooooooo World!!!!!'
    parentEl.appendChild(childEl)
}
let testInt = setInterval(addPara, 2000)

function stopInt() {
    clearInterval(testInt)
}

