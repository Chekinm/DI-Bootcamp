
// Exercise 1: Traversing the DOM
// Knowing how to traverse the DOM using JavaScript provides a foundation
// to altering an HTML page in real time.
// Using the HTML markup in Listing 1, perform these tasks:


let page = document.getElementById("page")
//console.log(a) 


// 1. Use the firstElementChild property to access an element.

let header = page.firstElementChild
console.log(header.id)

let title = header.firstElementChild
title.textContent = 'My new page title'


// 2. Use the lastElementChild property to access an element.
let content = page.lastElementChild
console.log(content.id)

// 3. Use the nextElementSibling property to access an element.

let content2 = header.nextElementSibling
console.log(content2.id)

// 4. Use the previousElementSibling property to access an element.

let header2 = content2.previousElementSibling
console.log(header2.id)

// 5. Use the parentNode property to access an element.
let page2 = content2.parentElement
console.log(page2.id)


// 6. Use the childNodes property to access a group of child elements.

let child = page2.childNodes
console.log(child)


// Exercise 2: Targeting nodes
// In exercise 1, you learned how to target nodes in several ways.
// Continuing to use the markup in Listing 1, perform the following tasks:
// 1. Retrieve the value of a node using / innerText / innerHTML / textContent.
// 2. Change the value of a node using / innerText / innerHTML. / textContent.
// 3. Retrieve the value of a node attribute.
// 4. Change the value of a node attribute.

// Exercise 3: Manipulating the DOM
// Now that you know how to traverse the DOM and alter node values,
// the next logical step is to learn how to add, remove, and replace nodes.
// Perform the following tasks:
// 1. Use the appendChild method to add a node.
// 2. Use the insertBefore method to add a node.
// 3. Use the removeChild method to remove a node.
// 4. Use the replaceChild method to replace a node.