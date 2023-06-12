const express = require ('express')

const app = express()

const user = {firstname: 'John',lastname: 'Doe'}

app.use(express.urlencoded({extended:true}))
app.use(express.static('public'));

app.listen(3003, (req, res) => {
    console.log('listen on 3003')
})


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

app.get('/form', (req, res) => {
    res.sendFile(__dirname+'/public/form.html')

})



app.post('/dataRecived', (req, res) => {
    data = req.body
    for (key in data) {
        console.log(`${key} : "${data[key]}"`)
    }
    res.send(`Recived data from form. Name is - ${req.body.name}, message is ${req.body.phone} `)
})

