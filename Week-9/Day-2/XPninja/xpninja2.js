console.log('----------------Ex2--------------')

const stringChop = (str, chopSize) => {
    let answer = []
    let i = 0
    while (i <= str.length) {
        answer.push(str.slice(i, i+chopSize))
        i += chopSize
    }
    return answer
}
console.log(stringChop('developers', 2)); 
//["de", "ve", "lo", "pe", "rs"] 