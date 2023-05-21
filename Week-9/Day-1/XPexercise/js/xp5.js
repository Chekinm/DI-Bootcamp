function rnd() {
    return Math.round(Math.random()*255)
}

function rndColor(event) {
    //leftclick
    let div = event.target
    div.style.background = 'rgb(' + rnd() + ',' + rnd() + ',' + rnd() + ')';




}

function colorYellow(event) {
    //rightclick
    event.preventDefault()
    let div = event.target

    div.style.background = "yellow"
}


function makeBig(event) {
    //mouse over
    let div = event.target
    div.style.width="100px"
    div.style.height="100px"
    div.style.left="150px"
    div.style.top="150px"
        
}

function makeSmall (event) {
    //mousout
    let div = event.target
    div.style.width="50px"
    div.style.height="50px"
    div.style.left="175px"
    div.style.top="175px"
}

  