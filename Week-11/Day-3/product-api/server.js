const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const products_router = require('./routes/products.js')
const users_router = require('./routes/users.js')


const app = express()
dotenv.config()

app.set('view engine','ejs');

app.listen(process.env.PORT||3001, ()=>{
  console.log(`run on port ${process.env.PORT||3001}`);
})

app.use('/', express.static(__dirname +'/public'))
app.use(cors());
app.use(express.urlencoded({extended:true}));
app.use(express.json());

app.use( products_router.router)
app.use('/users', users_router.router)
// app.get('/shop', (req,res)=>{
//   res.render('shop')
// })


// /api/search - get - name=ip search the db by name of products
