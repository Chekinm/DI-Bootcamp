let result = document.getElementById("result")

let bracketStack = []

function number(value) {  

    if (!result.textContent) {
        result.textContent = value
    } else if (!result.textContent.includes("Error")){
        result.textContent += value
    }
}


function operator (operation) {
    regex = /[\d\)]$/
    console.log(regex.test(result.textContent))
    if (regex.test(result.textContent)) {
        
    
    switch (operation) {

        case ('+'):
            result.textContent += '+'
            break; 
        
        case ('-'):
            result.textContent += '-'
            break; 
            
        case ('*'):
            result.textContent += '*'
            break; 
      
        case ('/'):
            result.textContent += '/'
            break; 

        case ('.'):
            regex = /\d+$/
            if (regex.test(result.textContent)) {
                result.textContent += '.'}
            break; 
        }
    }
} 

function brackets() {
    console.log(bracketStack)
    regexOpenBracket = /[(]+$|[\+\-\/\*]$/
    regexCloseBracket = /\d+$|[)]+$/
    if (!result.textContent){ 
        console.log("Open bracket")
        result.textContent = '('
        bracketStack.push('(')
    } else if (regexCloseBracket.test(result.textContent) && bracketStack.length) {
        result.textContent += ')'
        console.log("close bracket")
        bracketStack.pop()
    } else if (regexOpenBracket.test(result.textContent)) {
        result.textContent += '('
        console.log("open bracket")
        bracketStack.push('(')

    }
}

function equal() {
    let regex =/[\+\-\/\*]$/
    if (!regex.test(result.textContent)){ 
        // check if last simbol is not an operator
        // if not close all opened brackets
        while (bracketStack.length) {
            result.textContent += ")"
            bracketStack.pop()
        } 
    }
    let res;
    try {
        res = eval(result.textContent)
        if (res==Infinity) {
            alert("MathError(result)")
            result.textContent = "Error. Press C"
        } else {
            result.textContent = res
        }
    } catch (SyntaxError) {
        alert ("Fihish your input!")
    }
    
}


// function isValid(value) {
//     res = /^[\d()]+(?:[+*\/\./-][\d()]+)+$/.test(value)
//     console.log(res)
//     return res
// }

function c () {
    result.textContent = ''
    bracketStack = []
}

function bs() {
    if (result.textContent[result.textContent.length-1]==='(') {

        bracketStack.pop()
        console.log(bracketStack)
    } else if (result.textContent[result.textContent.length-1]===')') {

        bracketStack.push('(')
        console.log(bracketStack)
    } 
    result.textContent = result.textContent.slice(0,result.textContent.length-1)
    console.log(result.textContent)
}


function keyPressed(e) {
    key = e.code
    console.log(key)
    console.log(key.slice(-1), key.startsWith('Numpad'))
    if (key.startsWith('Numpad')) {
        number(key.slice(-1))
}
}