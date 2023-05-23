const letters = ['x', 'y', 'z', 'z'];

let dict = {}
for (letter of letters) {
    if (letter in dict) {
        dict[letter] +=1
    } else {
        dict[letter] = 1
    }

}
console.log(dict)


let dictR = letters.reduce((dict, letter) => {
        if (letter in dict) {
            dict[letter] +=1 
        } else {
            dict[letter] = 1
        }
        return dict
        },{})

console.log(dictR)



// Use a for loop to get this output { x: 1, y: 1, z: 2 };
// Use the reduce() method to get this output { x: 1, y: 1, z: 2 };