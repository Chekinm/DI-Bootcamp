// //part I

// function makeJuice (size) {

//     function addIngredients (firstIngredient, secondIngredient, thirdIngredient) {
//         text = `The client wants a ${size} juice, containing ${firstIngredient}, ${secondIngredient}, ${thirdIngredient}.`
        
//         let div = document.createElement('div')
//         div.innerText = text
//         let body = document.getElementsByTagName("body")[0]
//         body.appendChild(div)  
//     }
//     return addIngredients:  
//     //('orange','apple','cucomber');

// }

// makeJuice('small')
// makeJuice('middle')
// makeJuice('big')


function makeJuice (size) {

    let ingrArr = []
    function addIngredients (...ingredients) {
        for (item of ingredients) {
            ingrArr.push(item)
        }
    }

    function createDrink () {
        text = `The client wants a ${size} juice, containing `+ ingrArr.join(", ") +"."
        let div = document.createElement('div')
        div.innerText = text
        let body = document.getElementsByTagName("body")[0]
        body.appendChild(div)  
    }
    
    addIngredients('orange','apple','cucomber','tomato');
    addIngredients('banana');
    console.log(ingrArr)
    createDrink()

}

makeJuice('small')






//part II


// function makeJuice (size) {

    
//     function addIngredients (...ingredients) {
        

//         function createDrink () {
            
//             text = `The client wants a ${size} juice, containing `+ ingredients.join(", ") +"."
//             let div = document.createElement('div')
//             div.innerText = text
//             let body = document.getElementsByTagName("body")[0]
//             body.appendChild(div)  
//         }
//         return createDrink
//     }

//     return addIngredients
   

// }

// let addIngrToSmall = makeJuice('small')

// let createSmallOrangeAppleCucpmberTomatoDrink = addIngrToSmall('orange','apple','cucomber','tomato');

// createSmallOrangeAppleCucpmberTomatoDrink()









//The way I'd like to do it.
// // part I

// function makeJuice (size) {

//     function addIngredients (firstIngredient, secondIngredient, thirdIngredient) {
//         text = `The client wants a ${size} juice, containing ${firstIngredient}, ${secondIngredient}, ${thirdIngredient}.`
        
//         let div = document.createElement('div')
//         div.innerText = text
//         let body = document.getElementsByTagName("body")[0]
//         body.appendChild(div)  
//     }
//     return addIngredients 
//     //('orange','apple','cucomber');

// }

// let smalldrink = makeJuice('small')

// let middledrink = makeJuice('middle')

// let bigdrink = makeJuice('big')
// smalldrink('orange','apple','cucomber')
// bigdrink('orange','apple','cucomber')
// middledrink('orange','apple','cucomber')