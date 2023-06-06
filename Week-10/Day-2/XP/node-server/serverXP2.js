const express = require ('express')

const app = express()

const user = {firstname: 'John',lastname: 'Doe'}


app.listen(3003, (req, res) => {
    console.log('listen on 3003')
})

app.use(express.static('public'));

app.get('/users/', (req, res) => {
    //res.setHeader('Content-Type', 'application/json')
    textJson = JSON.stringify(user)
    console.log(textJson)
    res.send(textJson)
})


app.get('/userid/:id', (req, res) => {
    const id = req.params
    
    if (!isNaN(id.id)) {
        res.send(id)
        console.log(id)
    }

})