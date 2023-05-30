let promis1 = fetch ('https://jsonplaceholder.typicode.com/users')
.then(res=>res.json())
.then(data=> {
    console.log(data)
})


const urls = [
    "https://jsonplaceholder.typicode.com/users",
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/albums"
  ];

Promise.all(urls.map(e=>(fetch(e))))
.then(results => {
    for (res of results) {
        console.log(res.json())
    }
})
.catch(err => {
    console.log(err)
})

