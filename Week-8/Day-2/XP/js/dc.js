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

    for (let ind in amountOfChange) {
        total += coinValuesList[ind] * amountOfChange[ind]
    }
    return (total >= itemPrice) ? true : false
}


console.log(isChangeEnough(4.25, [25, 20, 5, 0]))
console.log(isChangeEnough(14.11, [2,100,0,0])) 


//ex4
console.log("---------------------Ex4-----------------------")
//define all consts
const hotelPrice = 140
const carRentalPrice = 40
const airTicketPrice = {
    'London': 183,
    'Paris': 220
}

// helpful functions
function isAlpha(value) {
    return (value) && /^[a-zA-Z]+$/.test(value)
}

function isNumeric(value) {
    return (value) && !isNaN(value) 
}

function getUserInput(text, checkFunction) {
    let input
    do {
        input = prompt (text)
    } while (!checkFunction(input))
    return input
}

// a little bit more helpful functions

function getHotelCost(num_of_night) {
    return hotelPrice * num_of_night
}

function planeRideCost(destination) {
    if (destination in airTicketPrice) {
        return airTicketPrice[destination];
    } else {
        return 300;
    }   
}

function getCarCost(num_of_day) {
    let cost = carRentalPrice * num_of_day
    return (num_of_day < 11) ? cost : cost * 0.95
}

// finlally main function

function totalVacationCost() {

    let num_of_night = getUserInput('Enter number of night:', isNumeric)
    let destination = getUserInput('Enter destination: ', isAlpha)
    let num_of_day = getUserInput('Enter number of car rental days:', isNumeric)
 
    let hotelCost = getHotelCost(num_of_night)
    let airTicketCost = planeRideCost(destination)
    let carCost = getCarCost(num_of_day)
    return `The car cost: ${carCost}, the hotel cost: ${hotelCost}, the plane tickets cost: ${airTicketCost}.`
}

console.log(totalVacationCost())


//ex5
console.log("---------------------Ex5-----------------------")