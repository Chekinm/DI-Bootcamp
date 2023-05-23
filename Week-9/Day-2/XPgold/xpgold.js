// ex1 sum
let arr1 = [1,2,3,5,6,6,8,9,12,45]

let sum=(arr)=>arr.reduce( (total,item)=>total+item)
console.log(sum(arr1))

// ex2
let arr2 = [1,1,1,1,1,1,2,3,5,2,2,6,7,6,9,12,45]

function removeDuplicates (arr) {
    let setArr = new Set(arr)
    let i = 0
    while (i<arr.length) {
        if (setArr.has(arr[i])) {
            setArr.delete(arr[i]);
            i++;
        }else{ arr.splice(i,1) }    
    }
    return arr
}
console.log(removeDuplicates(arr2))

//alterative found not by myself
let arr3 = [1,2,3,5,2,2,6,7,6,9,9,12,45]
arr3 = Array.from(new Set(arr3))
console.log(arr3)

//3 remove values


let arr4 = [NaN, 0, 15, false, -22, '',undefined, 47, null]

console.log(arr4.filter((e)=>e))
    //item=>Boolean(item)));


//4 repeat

function repeat(str,n) {
    let res=[]
    for (i=0;i<n;i++) {
        res.push(str)
    }
    return res.join('')
}
console.log(repeat('Hello!',8))

// //5

const startLine = '                     ||<- Start line';
let turtle = '🐢';
let rabbit = '🐇';
st = startLine.indexOf("|")
turtle = turtle.padStart(st+2, ' ')
rabbit = rabbit.padStart(st+2, ' ')
console.log(startLine);
console.log(turtle);
console.log(rabbit);




