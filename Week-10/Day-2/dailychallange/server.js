const express =require('express');

const app = express();
app.use(express.urlencoded({extended:true}))
app.use(express.json())

app.listen(3001, () => {
    console.log('run on port 3001');
});
console.log(__dirname + '/public')
app.use('/', express.static(__dirname + '/public'))

app.get('/aboutMe/:hobby', (req,res)=>{
    // res.sendFile(__dirname + '/public/about.html')
    const hobby = req.params.hobby
    if(isNaN(hobby)){
      return res.status(200).send(`This is my hobby: ${hobby}`)
    }
    res.status(404).send('hobby not found')
  })

app.get('/pic', (req,res) => {
    res.sendFile(__dirname + '/public/images/pic1.jpg')
})

app.get('/form', (req,res) => {
    res.sendFile(__dirname + '/public/form.html')
})

app.get('/formdata', (req,res) => {
    console.log(req.query)
    res.send(`ok from /fromData ${req.query.email}`)
})

app.post('/formdata', (req,res) => {
    console.log(req.body)
    res.send(`Recived data from form. Email is - ${req.body.email}, message is - ${req.body.message} `)
})