

// function func1(arr) {
    
//     for (i=0; i<arr.length; i++) {
//     arr[i] += 1

//     }
//     //let a = arr.length
// }


// function func2(arr) {
//     let len = arr.length
//     for (i=0; i < len; i++) {
//     arr[i]+=1
//     }
// }


// let arr = []
// for (i=1;i<1000000;i++) {
//     arr.push(i)
// }

// console.time('Execution Time');
// func2(arr);

// let a = console.timeEnd('Execution Time');

// consol
// console.time('Execution Time');

// func1(arr);


// // console.timeEnd('Execution Time');
// function reverseWord (word) {
//     let new_word = []
//     for (i=word.length-1; i>=0;i--) {
//         new_word.push(word[i])
//     }
//     return new_word.join('')
// }


// function reverse(event) {

//     event.preventDefault();
//     strArr =  event.target.text.value.split(' ')
//     response = []

//     for (word of strArr) {
//             response.push(reverseWord(word))
//     }
//     document.getElementById("resp").innerText = response.join(' ')
// }

// function a (var1) {
//     function b(var2) {
//         return var1 + var2
//     }
//     return b
// }

// let nestedfunc = a(10)
// let res = nestedfunc(5)
// console.log(res)


function xnorm (a,b) {
    function insidefunc (c) {
        return a(b(c))
    }
    return insidefunc
}



const x = (a,b) => (c) => {
    return a(b(c))
}

const sum2 = num => num * 2;

const sum = num => num + 1 ;

let insidefunc = xnorm(sum, sum2)
let res = insidefunc(6)
console.log(res)

const obj1 = {a:1}
const obj2 = obj1
obj1.r = 10
console.log(obj1)
console.log(obj2)