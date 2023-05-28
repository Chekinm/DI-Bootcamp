//ex1
// data goes to the url

//ex2
// data packed into request body 

const marioGame = {
detail : "An amazing game!",
characters : {
    mario : {
        description:"Small and jumpy. Likes princesses.",
        height: 10,
        weight: 3,
        speed: 12,
    },
    bowser : {
        description: "Big and green, Hates princesses.",
        height: 16,
        weight: 6,
        speed: 4,
    },
    princessPeach : {
        description: "Beautiful princess.",
        height: 12,
        weight: 2,
        speed: 2,
    }
},
}

console.log(marioGame)
debugger
let marioJSON =  JSON.stringify(marioGame)
//objec became a JSON string
//nested boject became JSON nested bojects.
console.log('sdfsd')
console.log(marioJSON)
