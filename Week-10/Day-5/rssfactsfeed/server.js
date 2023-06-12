const express = require('express');
const path = require('path')
const app = express();

app.use(express.static('public'));

app.set('views', path.join(__dirname, '/public/pages'))
app.set('view engine', 'ejs');

app.get('/', (req, res) => {
    // The render method takes the name of the HTML
    // page to be rendered as input
    // This page should be in the views folder
    // in the root directory.
    res.render('index', { nameRestaurant: "Papa Pizza", pizzaMenu: menu })
})


app.listen(3001, () => {
    console.log('run on port 3001');
});

let menu = [
    {
        name: "Margarita",
        price: 10,
        ingredients: ["Tomato Sauce", "Mozzarella", "Basil"]
    },
    {
        name: "Bianca",
        price: 13,
        ingredients: ["Ricotta", "Mozzarella", "Garlic"]
    },
    {
        name: "Etna",
        price: 14,
        ingredients: ["Tomato sauce", "Mozzarella", "Anchovies", "Capers", "Olives"]
    }
]




// console.log(__dirname + '/public')
// app.use('/', express.static(__dirname + '/public'))


// app.use(express.urlencoded({extended:true}))
// app.use(express.json())




// app.get('/aboutMe/:hobby', (req,res)=>{
//     // res.sendFile(__dirname + '/public/about.html')
//     const hobby = req.params.hobby
//     if(isNaN(hobby)){
//       return res.status(200).send(`This is my hobby: ${hobby}`)
//     }
//     res.status(404).send('hobby not found')
//   })

// app.get('/pic', (req,res) => {
//     res.sendFile(__dirname + '/public/images/pic1.jpg')
// })

// app.get('/form', (req,res) => {
//     res.sendFile(__dirname + '/public/form.html')
// })

// app.get('/formdata', (req,res) => {
//     console.log(req.query)
//     res.send(`ok from /fromData ${req.query.email}`)
// })

// app.post('/formdata', (req,res) => {
//     console.log(req.body)
//     res.send(`Recived data from form. Email is - ${req.body.email}, message is ${req.body.message} `)
// })




// let Parser = require('rss-parser');
// let parser = new Parser();

// (async () => {

//   let feed = await parser.parseURL('https://thefactfile.org/feed/');
//   console.log(feed.title);

//   feed.items.forEach(item => {
//     console.log(item.title + ' : ' + item.link)
//   });

// })();