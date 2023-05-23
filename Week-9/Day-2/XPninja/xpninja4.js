console.log('--------------------Ex4---------------')


const reverseArray = (arr) => {
    let left = 0
    
    while (left < arr.length-left) {
        tmp = arr[arr.length-left-1]
        arr[arr.length-left-1] = arr[left]
        arr[left] = tmp
        left++;
        
    }
    return arr
}



console.log(reverseArray([1,2,3,4,5])) // [5,4,3,2,1]
console.log (reverseArray([1,2])) // [2,1]
console.log(reverseArray([])) // []
console.log(reverseArray([1,2,3,4,5,6,7,8,9,10])) // [10,9,8,7,6,5,4,3,2,1]
console.log([1,2])


