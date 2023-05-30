// num =  prompt("Enter a number")
num = 5

function fibb(n) {
    let res = [0,1]
    let sum = [0,1]
    i = 2
    while (i <= n) {
        res.push (res[i-2]+res[i-1]);
        sum.push( res[i]+ sum[i-1])
        i++; 
    }
    return {'n-th fibb':res[n],'sum of n fib':sum[n]}
}

console.log(fibb(20))