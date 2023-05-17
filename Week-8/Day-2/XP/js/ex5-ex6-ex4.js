// ex5


// Retrieve the div and console.log it
let container = document.getElementById('container');
console.log(container);


// Change the name “Pete” to “Richard”.
let ul1 = container.nextElementSibling;

let ul1_li2 = ul1.lastElementChild;

ul1_li2.innerHTML = 'Richard';


// Delete the <li> that contains the text node “Sarah”. (It’s the second <li> of the second <ul>)

let ul2 = ul1.nextElementSibling;
li_list = ul2.children;
ul2.removeChild(li_list[1]);



// Change each first name of the two <ul>'s to your name. (Hint : use a loop)
let elem = ul1;
elem.className +=' university';
elem.className +=' attendance';
while (elem.firstElementChild !== null) {
    console.log(elem);
    
    elem.firstElementChild.textContent = 'Mike';              
    
    elem.className += ' student_list' 
    elem = elem.nextElementSibling;
}   


container.style.backgroundColor = 'lightblue';

// ul2 defined before
let ul2_li2 = ul2.lastElementChild;
ul2_li2.style.cssText += 'display:none;'

//defined before
ul1_li2.style.cssText += 'border-style: solid; border-width: 1px;'

container.parentElement.style.cssText += 'font-size: 30px;'



//  ---------------ex6 ------------------------------------

let nav_div = document.getElementById('navBar')
nav_div.setAttribute('id', 'socialNetworkNavigation')
console.log(nav_div)
const newLi = document.createElement('li')
const newLiLink =  document.createElement('a');
newLiLink.innerHTML='Logout';
newLiLink.href='#';
newLiLink.title='Logout';
newLi.appendChild(newLiLink)
nav_div.firstElementChild.appendChild(newLi)
console.log(nav_div.firstElementChild.firstElementChild.textContent)
console.log(nav_div.firstElementChild.lastElementChild.textContent)


// ------------------------------------ex-4-------------------------------

const allBooks = [{title:'Winnie the Pooh',
    author:'Alan Miln',
    image: 'https://static.hdrezka.ac/i/2016/5/26/xa943452bf0a9er63j41x.jpg',
    alreadyread: false},
    {title:'Hamlet',
    author:'William Shakespeare',
    image: 'https://kbimages1-a.akamaihd.net/e919fc20-6c6b-4971-91ee-109e2624d76e/353/569/90/False/hamlet-prince-of-denmark-22.jpg',
    alreadyread: true},
    {title:'Secrets of the JavaScript Ninja',
    author:'John Resig',
    image: 'https://m.media-amazon.com/images/I/51u9Pg4riRL._SX397_BO1,204,203,200_.jpg',
    alreadyread: false}
];
console.log(allBooks)

bookList = document.querySelector('.listBooks')

for (let book of allBooks) {
    console.log(book)
    let new_book = document.createElement('ul')
    let text = document.createTextNode(book.title)
    new_book.appendChild(text)
    bookList.appendChild(new_book)
    if (book.alreadyread) {
        console.log(book.alreadyread)
        new_book.style.color += 'blue'
        new_book.style.background += 'lightgreen'
    }

    let new_aut = document.createElement('li')
    let author = document.createTextNode(book.author)
    new_aut.appendChild(author)
    new_book.appendChild(new_aut)

    let new_image = document.createElement('li')
    let img = document.createElement('img')
    img.src = book.image
    img.width="100"
    new_image.appendChild(img)
    new_book.appendChild(new_image)
    console.log(new_book)

} 







