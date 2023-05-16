// buble sort is boring soooo....

// I coded merge sort which os O(n(log(n))
// have fun!!

// the idea of merge sort is next
// if we have two sorted array we can merge it 
// to a big sorted array for 0(n).
// so lets devide our main arr, and run a reqursion
// zero case -  is trivial array, with one element, which is
// sorted by default
// as number of such devision by 2 is log(n) we ahve a fast
// sort functio. takes also o(n) memory.

function merge(num1, num2, desc) {
    //if to array are soreted we can merge it
    let res = []
    let ind1 = 0
    let ind2 = 0
    while (ind1 < num1.length && ind2 < num2.length) {
     // here we choose what is the order of sorting, by flag desc
        let condition = (desc) ? (num1[ind1] <= num2[ind2]) : (num1[ind1] >= num2[ind2])      
        if (condition) {
            res.push(num1[ind1])
            ind1 += 1
        }
        else {
            res.push(num2[ind2])
            ind2 += 1
        }
        }
    //so in the first step we get all element from one of the arr
    // so only one of them still have elements
    // just push the reset to the result, a the rest is sorted already
    while (ind1 < num1.length) {
            res.push(num1[ind1])
            ind1 += 1
        }
    while (ind2 < num2.length) {
            res.push(num2[ind2])
            ind2 += 1
        }
    
    return res
}

function mergeSort (arr, desc) {
    //zero reqursion case
    if (arr.length < 2) return arr
    //reqursion
    else{    
        let mid = (arr.length-arr.length % 2) / 2
        return merge(mergeSort(arr.slice(0,mid),desc),mergeSort(arr.slice(mid, arr.length),desc),desc)
    }
}

const nums = [5,0,9,1,7,4,2,6,3,8];
// I've added sort option as it cost nothing true- ascending
// false descending, choose false as is is ascing in th task
c = mergeSort(nums,false)
console.log(c.join())

//I only google one thing - integer devision. ELse is form my memeory. 

// by the way if ou have all the  number in the array 
//(like we have in task) we can sort it for O(n)
//as easy as that ...

function countSort(arr, desc){
    let ind = 0;
    if (desc) {
        while (ind < arr.length) {
            sortInd = arr.length - 1 - ind 
            while (arr[sortInd] != ind) {
                tmp = arr[sortInd]
                arr[sortInd] = arr[arr.length - 1 - tmp]
                arr[arr.length - 1 - tmp] = tmp
                }
            ind += 1
            }
        }
    else {
        while (ind < arr.length) {
            while (arr[ind] != ind) {
                tmp = arr[ind]
                arr[ind] = arr[tmp]
                arr[tmp] = tmp
                }
            ind += 1
        }
    }   
    return arr
    }
d = countSort(nums,false)
console.log(d.join())