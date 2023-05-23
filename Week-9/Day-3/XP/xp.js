// ------1------
const fruits = ["apple", "orange"];
const vegetables = ["carrot", "potato"];

const result = ['bread', ...vegetables, 'chicken', ...fruits];
console.log(result);
// returns ['bread', "carrot", "potato", 'chicken', "apple", "orange"];

//------2------
const country = "a";
console.log([...country]);
//return ["USA"]
// oups:) no its ["U","S","A"], so it need iterable nad if it gets, 
// it do iterate, so do with string  :)



// ------Bonus------
emptyArr = [,,]
console.log(emptyArr)

console.log('try for each')
emptyArr.forEach((e)=>console.log(e, 'forEach'))

console.log('try for in')
for (item in emptyArr) {
    console.log(item,'for in')
}

console.log('try for of')
for (item of emptyArr) {
    console.log(item,'for of')
}


console.log(emptyArr[0], 'console.log(emptyArr[0]')

console.log(emptyArr, 'console.log(emptyArr)')

let undefArr = [...emptyArr]

console.log(undefArr, 'console.log(undefArr, )')
undefArr.forEach((item)=>console.log(item,'forEach'))


console.log('try for in')
for (item in undefArr) {
    console.log(item, undefArr[item], 'for in')
}

console.log('try for of')
for (item of undefArr) {
    console.log(item,'for of')
}

//Ok. That interesting.
//check the output!!



