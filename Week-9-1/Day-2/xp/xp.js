// ex1
let a = 'good'
let b = 'bad'


const compareToTen = (num) => new Promise((resolve, reject)=>(num<10 ? resolve([num,"n<10"]) : reject([num,"n>=10"])))
    


//In the example, the promise should reject
compareToTen(15)
  .then(result => console.log(result))
  .catch(error => console.log(error))

//In the example, the promise should resolve
compareToTen(8)
  .then(result => console.log(result))
  .catch(error => console.log(error))


