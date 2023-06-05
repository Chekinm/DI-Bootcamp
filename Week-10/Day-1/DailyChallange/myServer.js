const http = require('http')
const script = require('./script.js')

numberFromScript = script.result
datestring = script.datestring
console.log(script.datestring)

const server = http.createServer((req,res) => {
    res.setHeader('Content-Type', 'text/html')
    res.end(`</head>
    <body>
        <p>My module is</p>
        <p>${numberFromScript}<p>
        <h1>Hi there at the frontend</h1>
        <h2>${datestring}<h2>
    </body>
    </html>`)
})

server.listen(3001, () => {
    console.log('I am listening!')
})