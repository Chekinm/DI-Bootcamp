
const makeAllCaps =(arr) => new Promise((resolve,reject) => {
    let retArr = []
    for (word of arr) {
        
        if (typeof(word) === "string") {
            retArr.push(word.toUpperCase())
        } else {
            reject(`${word} is not a string`)
        }
    }
    resolve (retArr)
})

const sortWords = (arr) => new Promise ((resolve, reject) => {
    if (arr.length > 4) {
        resolve (arr.sort())
    } else {
        reject ("arr is too short to sort")
    }

}) 


//in this example, the catch method is executed
makeAllCaps([1, "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, the catch method is executed
makeAllCaps(["apple", "pear", "banana"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result))
      .catch(error => console.log(error))

//in this example, you should see in the console, 
// the array of words uppercased and sorted
makeAllCaps(["apple", "pear", "banana", "melon", "kiwi"])
      .then((arr) => sortWords(arr))
      .then((result) => console.log(result)) //["APPLE","BANANA", "KIWI", "MELON", "PEAR"]
      .catch(error => console.log(error))