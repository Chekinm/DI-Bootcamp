// ex2 

// function winBattle(){
//     return true;
// }

const winBattle = () => true;
let experiencePoints;
experiencePoints = winBattle() ? 10:1
console.log(experiencePoints) 

//ex3

const isString = (val) => typeof val === "string" 
console.log(typeof 'hello')
console.log(isString('hello')); 
//true
console.log(isString([1, 2, 4, 0]));
//false

//ex4

const colors = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const colors_whitout_violet = ["Blue", "Green", "Red", "Orange",  "Indigo", "Yellow"];

colors.forEach((color,ind)=>console.log(`${ind+1}# choice is ${color}`))


const containsViolet = (arr) => arr.some((cl) => cl === "Violet") ? console.log("Yeah!") : console.log("No...")

containsViolet(colors)
containsViolet(colors_whitout_violet)


//ex5

const colors_long = ["Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow","Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow","Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow","Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow","Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow","Blue", "Green", "Red", "Orange", "Violet", "Indigo", "Yellow"];
const ordinal = ["th","st","nd","rd"];

const ordinalSuffix = (num, ordinal) => (num == 11 || num == 12 || num%10 > 3) ? ordinal[0]:ordinal[num%10]
    
colors_long.forEach((color,ind)=>console.log(`${ind+1}${ordinalSuffix(ind+1,ordinal)} choice is ${color}`))
    

//ex5





const details = ["+200", "-100", "+146", "+167", "-2900"]

// we will solve another task
//we have income and pay incoetax of 20% from it
// expense is just axpense, is not our deal to handle VAT.
// so

let bankAmount = 0;
const incomeTax = 0.17
details.forEach((transaction) => (transaction >= 0) ? bankAmount += Number(transaction)*(1-incomeTax) : bankAmount += Number(transaction))
console.log(bankAmount)

//we need more imcome :(