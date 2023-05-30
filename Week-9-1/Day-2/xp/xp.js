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



// ex2

const delayed = (time) => new Promise(function (resolve,reject) {
  setTimeout(()=>resolve("we did it"),time*1000)

})



let promise = Promise.resolve("we decide to resolve promise by hand")
promise.then(res=>console.log(res))
console.log(promise)

let promiseRejected = Promise.reject("we decide to reject your promis")
promiseRejected.catch(res=>console.log(res))

