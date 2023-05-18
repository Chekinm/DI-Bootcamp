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
    // trivial variant
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


//fron Ziv

function getUniqueElements(arr) {
    const uniqueElements = [];
  
    // Helper function to check if two arrays are deeply equal
    function deepArrayEquals(a, b) {
      if (a === b) return true;
      if (a.length !== b.length) return false;
  
      for (let i = 0; i < a.length; i++) {
        if (!deepEquals(a[i], b[i])) return false;
      }
  
      return true;
    }
  
    // Helper function to check if two objects are deeply equal
    function deepObjectEquals(a, b) {
      if (a === b) return true;
  
      const keysA = Object.keys(a);
      const keysB = Object.keys(b);
  
      if (keysA.length !== keysB.length) return false;
  
      for (let key of keysA) {
        if (!deepEquals(a[key], b[key])) return false;
      }
  
      return true;
    }
  
    // Helper function to check if two values are deeply equal
    function deepEquals(a, b) {
      if (Array.isArray(a) && Array.isArray(b)) {
        return deepArrayEquals(a, b);
      }
  
      if (typeof a === 'object' && typeof b === 'object') {
        return deepObjectEquals(a, b);
      }
  
      return a === b;
    }
  
    // Iterate over the input array

    for (let i = 0; i < arr.length; i++) {
      let isUnique = true;
  
      // Check if the element is already in the uniqueElements array
      for (let j = 0; j < uniqueElements.length; j++) {
        if (deepEquals(arr[i], uniqueElements[j])) {
          isUnique = false;
          break;
        }
      }
  
      // If the element is unique, add it to the uniqueElements array
      if (isUnique) {
        uniqueElements.push(arr[i]);
      }
    }
  
    return uniqueElements;
  }
  
  // Example usage
  const inputArray = [
    1,
    'Hello',
    [1, 2, 3],
    [1, 2, 3], // Duplicate array
    { name: 'John', age: 25 },
    { name: 'John', age: 25 }, // Duplicate object
    1, // Duplicate primitive
    'Hello', // Duplicate primitive
  ];
  
  const uniqueArray = getUniqueElements(inputArray);
  console.log(uniqueArray);
