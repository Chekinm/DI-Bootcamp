

const nomilizeString = (str) => { 
    return str.replace(' ','').trim().toLowerCase()
}

const strCountDict= (str) => {
    let charDict = {}
    for (char of str) {
        if (char in charDict) {
            charDict[char] += 1
        } else {
            charDict[char] = 1
        }
    }
    return charDict
}

const isAnagram = (str1, str2) => {
    let strNorm1 = nomilizeString(str1)
    let strNorm2 = nomilizeString(str2)
    let contDict1 = strCountDict(strNorm1)
    let contDict2 = strCountDict(strNorm2)

    
    for (let key of Object.keys(contDict1)) {
        
        if (key in contDict2) {
            if (contDict1[key] === contDict2[key]) {
                delete contDict2[key]
                } else {
                    return false
                } 
            } else {
                return false
            } 
        }
        console.log(Object.keys(contDict2))
        if (Object.keys(contDict2).length) {
            return false
        } else {
        return true
        }
    }


console.log(isAnagram("Astronomer", "Moon starer"))
console.log(isAnagram("School master", "The classroom"))
console.log(isAnagram("The Morse Code", "Here come dotsj"))
