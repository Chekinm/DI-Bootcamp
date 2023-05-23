console.log("--------------dc2------------------------------")

let client = "John";

const groceries = {
    fruits : ["pear", "apple", "banana"],
    vegetables: ["tomatoes", "cucumber", "salad"],
    totalPrice : "20$",
    other : {
        payed : true,
        meansOfPayment : ["cash", "creditCard"]
    }
}


const displayGroceries = (fruits) =>console.log(groceries[fruits].join(', '))
displayGroceries('fruits')
// Create an arrow function named displayGroceries, that console.logs the 3 fruits from the groceries object. Use the forEach method.

const cloneGroceries = (cloningObj)=> {
    newObj = cloningObj 
    return newObj
}
let newUser = cloneGroceries(client) 
console.log(newUser)
client = "Ben"
console.log(newUser)


let newShop = cloneGroceries(groceries) 
console.log(newShop)
console.log("before")
console.log("new shop.total = ", newShop.totalPrice,"\n", "crocery total = ", groceries.totalPrice)
groceries.totalPrice = "100$"
console.log("after")
console.log("new shop.total = ", newShop.totalPrice,"\n", "crocery total = ", groceries.totalPrice)


console.log("-----------------------------------")
console.log("before")
console.log("new shop.other.payed = ", newShop.other.payed,"\n", "crocery.other.payed = ", groceries.other.payed)
groceries.other.payed = false
console.log("after")
console.log("new shop.other.payed = ", newShop.other.payed,"\n", "crocery other.payed = ", groceries.other.payed)

//
// Invoke the cloneGroceries function.
