//1
const array = [[1],[2],[3],[[[4]]],[[[5]]]]
let newArray = array.flat(2)
console.log(newArray)

//2
const greeting = [["Hello", "young", "grasshopper!"], ["you", "are"], ["learning", "fast!"]]

let newArray2 = greeting.map((item)=>item.join(' '))
console.log(newArray2)

//3
let newArray3 = newArray2.join(' ')
console.log(newArray3)

//4

const trapped = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]] 

//this actually is not possible as we declared trapped as const
// lets try with let

let trappedMutable = [[[[[[[[[[[[[[[[[[[[[[[[[[3]]]]]]]]]]]]]]]]]]]]]]]]]] 

while ((typeof trappedMutable[0]) != 'number') {
    trappedMutable = trappedMutable.flat()
}

console.log(trappedMutable)