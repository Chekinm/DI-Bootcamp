const allTruthy = (...args) => {

    for (val of args) {
        if (!val) {
            return false
        }
    }
    return true
}

console.log(allTruthy(true, true, true))

console.log(allTruthy(true, false, true))

console.log(allTruthy(5, 4, 3, 2, 1, 0))

//or, if you prefer one string solutions

const allTruthyOneStringer=(...args) => Boolean(args.reduce((answer, currElem)=>answer && currElem))

console.log(allTruthyOneStringer(true, true, true))

console.log(allTruthyOneStringer(true, false, true))

console.log(allTruthyOneStringer(5, 4, 3, 2, 1, NaN ))