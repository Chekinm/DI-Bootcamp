// Using a DOM property, retrieve the h1 and console.log it.

let article = document.getElementsByTagName('article')
console.log(article[0])

let h1 = document.getElementsByTagName('h1')
console.log(h1[0].textContent)


// Using DOM methods, remove the last paragraph in the <article> tag.
let paragraphs = document.getElementsByTagName('p')
console.log(paragraphs[paragraphs.length-1])
paragraphs[paragraphs.length-1].remove()

// Add a event listener which will change the background color of the h2 to red, when it’s clicked on.

function setBgRed (event) {
    event.target.style = "background:red";
}
// Add an event listener which will hide the h3 when it’s clicked on (use the display:none property).

function setHidden (event) {
    event.target.style.display = "none";
}
// Add a <button> to the HTML file, that when clicked on, should make the text of all the paragraphs, bold.

function SetBold() {
    let strongTag = document.createElement("strong")
    //create DOM element that whould wrap my article

    let strongTagDomEl = article[0].parentElement.insertBefore(strongTag,article[0])
    //insert it befor articel
    
    strongTagDomEl.appendChild(article[0])
    //put article inside strong
}

// BONUS : When you hover on the h1, set the font size to a random pixel size between 0 to 100.(Check out this documentation)

function rndFont(event) {
    event.target.style.fontSize = String(Math.round(Math.random()*100))+'px'
}


// BONUS : When you hover on the 2nd paragraph, it should fade out (Check out “fade css animation” on Google)

function fadeOut(event) {
    console.log(event.target)
    event.target.style.opacity = "0";
    event.target.style.transition = "all 4s";
    
}
