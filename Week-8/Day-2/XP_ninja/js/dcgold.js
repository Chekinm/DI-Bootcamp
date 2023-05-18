function isAlpha (value) {
    return (value) && /^[a-zA-Z]+$/.test(value);
}

function isAlphaLower(value) {
    return (value) && /^[a-z]+$/.test(value);
}



function isNumeric(value) {
    return (value) && !isNaN(value) 
}

function getUserInput(text, checkFunction) {
    let input;
    do {
        input = prompt (text);
    } while (!checkFunction(input));
    return input;
};



// //----------------------------ex1--------------

// function rnd() {
//     return Math.round(Math.random()*99 + 1);
// }
// let limit = rnd()
// let numList = []

// for (let i=0; i < limit; i++) {
//     if (!(i%2)) {
//         numList.push(i)
//     } 
// }
// console.log(numList.join()) 

// //-------------------------------ex2------------

// word = getUserInput("Enter word", isAlphaLower)

// function cApItAlAiSe(word) {
//     let WoRd = []
//     let wOrD = []
//     let len = word.length
//     for (let i=0; i<len; i++) {
//         if (!(i%2)) {
//             WoRd.push(word[i])
//             wOrD.push(word[i].toUpperCase()) 
//         } else {
//             WoRd.push(word[i].toUpperCase())
//             wOrD.push(word[i]) 
//         }   
//     }
//     return [WoRd.join(''), wOrD.join('')]
// }

// console.log(cApItAlAiSe(word))


//-------------------------------ex4------------

function isPalindrome (sentence) {
    sentence = sentence.toLowerCase()
    let l = 0
    let r = sentence.length
    while (l<=r) {
        while (!isAlphaLower(sentence[l])) {
            l++
        }
        while (!isAlphaLower(sentence[r])) {
            r--
        }
        if (sentence[l] === sentence[r]) {
            l++
            r--
        } else {
            return false
        }

    }
    return true

}

console.log(isPalindrome('Roma tib%%i subito motibus//// ibit a112mor”'))


//-----------------------------------ex5-------------------------

function maxFromArr(arr) {
    let max = NaN
    for (let item of arr) {
        if (!(item.isNaN)) {
            max = (max.isNaN) ? Math.max(max, item) : item
        }
    }
    return max
}
console.log(maxFromArr([1,2,3,'a',[1,2],{a:4},'55']))


//----------------------ex6------------------

function uniqueFromArr(arr) {
    // trivial varian
    return Array.from(new Set(arr))
    
    
    // this is not working on non monotone array
    // need to add to set anyway.....so this code is usless
    //
    // if (arr.length) {
    //     let tmp = arr[0];
    //     let res = [arr[0]];
    //     for (let i=1; i<arr.length; i++) {
    //         if (arr[i] != tmp) {
    //             res.push(arr[i]);
    //             tmp =arr[i]
    //         }
    //     }
    //     return res
    // }
    // return []    
}

let a = {'a':[1,2]}
let b = {'a':[1,2]}
let c = b

console.log(uniqueFromArr([1,1,2,2,3,4,5,6,6]));
console.log(uniqueFromArr([]));
console.log(uniqueFromArr([1]));
console.log(uniqueFromArr([b,a,c]))
console.log(uniqueFromArr([1,1,2,2,3,4,5,6,6,1]));
