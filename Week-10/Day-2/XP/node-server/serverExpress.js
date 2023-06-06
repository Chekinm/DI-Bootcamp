const express = require ('express')



const app = express()

app.listen(3002, (req, res) => {
    console.log('listen on 3002')
})

app.get('/', (req, res) => {
    res.setHeader('Content-Type', 'text/html')
    res.end(`</head>
                    <body>
                        <h1>Hello1</h1>
                        <h2>Hello2</h2>
                        <h3>Hello3</h3>
                    </body>
                    </html>`)
})