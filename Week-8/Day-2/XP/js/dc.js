//ex 1
console.log("---------------------Ex1-----------------------")

function DivisibleBy(devisor) {
    var sum = 0;
    console.log(`Here is all numbers from 0 to 500 devisible by ${devisor}.`)
    for (var i=1; i<501; i++) {
        if (! (i%devisor)) {
            sum += i;
            console.log(i);
        };
    };
    console.log(sum);
}
DivisibleBy(27);

//ex2
console.log("---------------------Ex2-----------------------")
// I redefine the task a bit. 
// I want to have a shop with pricelist and stock as properties
// and releaseOrder as metod , which takes 
// shoping list obj as parametner, 
// this method check aviability and return 
// billing list



let shop = {
    stock : { 
        "banana": 6, 
        "apple": 4,
        "pear": 12,
        "orange": 32,
        "blueberry":1
    },  
    prices : {    
        "banana": 4, 
        "apple": 2, 
        "pear": 1,
        "orange": 1.5,
        "blueberry": 10
    },  

    checkAviabiliy: function (shoppingList) {
        for (product in shoppingList) {     
            if (! (product in this.stock && shoppingList[product] <= this.stock[product] )) {
                console.log(`Not enough ${product} on stock`)
                return false
            } 
        }     
        return true     
    },
    releaseOrder : function(shoppingList) {
        bill = 0
        //first - check aviability for all product
        if (this.checkAviabiliy(shoppingList)) {
            
            console.log ("Welcom to the DI fruits shop.")
            console.log ("Here is your bill:")       
            console.log ("Item\t\tqty.\t\tprice\t\tcost")
            for (product in shoppingList) {
                this.stock[product] -= shoppingList[product];
                bill += this.prices[product] * shoppingList[product]
                console.log(`${product}\t\t${shoppingList[product]}\t\t\t${this.prices[product]}\t\t\t${this.prices[product]*shoppingList[product]}`)
            }
            console.log(`The total for the order:\t\t\t${bill}`)
            return bill  
        } else {
            return NaN
        }      
    }
}; 

let shoppingList = {
    "banana": 2,
    "orange": 3,
    "apple" : 4,
}

// now it is as simple as this
console.log(shop.releaseOrder(shoppingList))


//ex3
console.log("---------------------Ex3-----------------------")


const coinValuesByName= { 
    quarters: 0.25,
    dimes: 0.10,
    nickel: 0.05,
    penny:  0.01
}

let coinValuesList = Object.values(coinValuesByName)


function isChangeEnough (itemPrice, amountOfChange) {
    let total = 0
    for (ind in amountOfChange) {
        total += coinValuesList[ind] * amountOfChange[ind]
    }
    return (total >= itemPrice) ? true : false
}

console.log(isChangeEnough(4.25, [25, 20, 5, 0]))
console.log(isChangeEnough(14.11, [2,100,0,0])) 


//ex4
console.log("---------------------Ex4-----------------------")


function hotelCost() {
    prompt ()



}