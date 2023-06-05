async function readUsers() {
    let data = (await fetch('https://jsonplaceholder.typicode.com/users')).json()
    let arr = []
    data.then((data) => {
        for (userObj of data) {
            arr.push(userObj.name)
        }
    }
    )
    return  arr
    }
    

console.log(readUsers().then((data)=>console.log(data)))