const express = require('express');
const dotenv = require('dotenv');
const cors = require('cors');
const products_router = require('./routes/products.js')
const {db} = require('./dbconfig/db.js')

const app = express();


dotenv.config();

app.listen(process.env.PORT||3001, ()=>{
    console.log(`run on port ${process.env.PORT||3001}`);
});

app.use(cors());
app.use(express.urlencoded({extended:true}));
app.use(express.json())

db('products')
.select('*')
.then(data=>{
    console.log(data);
})
.catch(e => {
    console.log(e);
})

app.use(products_router.router)