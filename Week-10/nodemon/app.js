const http = require ('http')

const server = http.createServer((req,res) => {
    res.end("hello from server")
}) 

server.listen(5000, () =>{
    console.log('run on 5000)');
})

