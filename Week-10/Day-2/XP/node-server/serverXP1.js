const http = require('http')
const user = {
    firstname: 'John',
    lastname: 'Doe'
}



const myserver = http.createServer((req, res) => {
//    // ----------par 1-------------------
   
//     res.setHeader('Content-Type', 'text/html')
//     res.end(`</head>
//                 <body>
//                     <h1>Hello1</h1>
//                     <h2>Hello2</h2>
//                     <h3>Hello3</h3>
//                 </body>
//                 </html>`)

//--------------part 2 --------------------
    res.setHeader('Content-Type', 'application/json')
    res.end(JSON.stringify(user))

})

myserver.listen(3000,() => {
    console.log('listening in port 3000')
})