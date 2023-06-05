const express = require('express');
const {products} = require('./config/data.js')
const {products2} = require('./config/data2.js')
//const {product1} = require('./config/data.js')

const app = express();




const logger = (req, res, next) => {
    console.log('url=',req.url);
    console.log('params=',req.params)
    console.log('query=',req.query)
    console.log('body=',req.body)
    next()
}

app.use('/api/', logger)
app.use(express.urlencoded({extended:true}),)
app.use(express.json())


app.listen(3001, () => {
    console.log('server  is running on port 3001')
})


app.get ('/api/products',(req, res) => {
    res.send(products)
});

app.get ('/api/products/:product_id', (req, res) => {
    console.log(req.params)
    let id = req.params.product_id
    console.log(id)
    const product = products.find(item => item.id == id);
    console.log(product)
    if (!product) {
        res.status(404).json({message:'Product not found'})
    }
    res.status(200).json(product)  //end(product)
    
});


app.get ('/api/search', (req, res) => {
    console.log(req.query)
    pattern = req.query.name
    
    console.log(pattern)
    
    let res1  = []
    for (prod of products) {
        console.log(prod.name.toLowerCase())
        if (prod.name.toLowerCase().includes(pattern.toLowerCase())) {
            res1.push(prod)
            
        } 
        console.log(res1)
    }
    if (!res1) {res.status(404).json({message:'Product not found'})
    }
    res.status(200).json(res1)  //end(product)



    
});


app.post ('/api/products',(req, res) => {
    console.log(req.body)//  .body)
    products.push(req.body)
    console.log(products)
    res.send("we got it")
});


app.delete ('/api/products/:product_id',(req, res) => {
    idx = req.params.product_id
    console.log(idx)
    let i = 0 
    let found = 0
    for (prod of products) {
        if (prod.id != idx) {
            products[i] = prod
            i++
        } else {found ++}
        
        }
    while (found) {
        products.pop()
        found --
    }

    res.send(products)
    console.log(products)
    
});

