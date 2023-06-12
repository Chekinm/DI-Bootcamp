const a = (x=[]) => {
    x.push('ss')
    return x
} 

console.log(a())
console.log(a())
console.log(a()[1])
console.log(['ss','ss'])