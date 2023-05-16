//ex1

let numbers = [123, 8409, 100053, 333333333, 7]

for  (num of numbers) {
    console.log(num, !(num%3))  
}


//ex2

let guestList = {
  randy: "Germany",
  karla: "France",
  wendy: "Japan",
  norman: "England",
  sam: "Argentina"
}

function capitlize (string) {
    if (string) {
        frst = string.charAt(0)
        frst = frst.toUpperCase()
        return frst + string.slice(1,string.length)
    }
    else return string
}


let guestName = prompt("Hey, enter your name!")
if (guestName in guestList) {
    console.log(`Hi. You are ${capitlize(guestName)} from ${guestList[guestName]}. Welcome!`)
}
else{
    console.log(`I don't know you ${capitlize(guestName)}`)
}

//ex3


let age = [20,5,12,43,98,55];

function sumArr(arr) {
    if (arr.length){
        sum = 0
        for (num of arr) {
            if (num.isNaN) return NaN
            else sum = sum + num 
        }
        return sum
    }
    else{
        return NaN
    }
}

function maxArr(arr) {
    if (arr.length){
        max = arr[0]
        for (num of arr) {
            if (num.isNaN) return NaN
            else if (num > max) max = num
        }
        return max
    }
    else{
        return NaN
    }
}


console.log(sumArr(age))
console.log(maxArr(age))