function reverseSimple (str) {
    let newStr = ''
    for (i=str.length-1;i>=0;i--) {
      newStr +=str[i]
    }
    return newStr
}

function detectState (a,b,currState) {
    if (a > b) {
        currState.func = gt
        currState.state = "raising"
    }
    if (a < b) {
        currState.func = lt,    
        currState.state = "falling"
    } 
    if (a == b) {
        currState.func = eq
        //we not change currSt.state in this case!!!
    }
    return currState
}

const gt = (a,b) => a > b
const lt = (a,b) => a < b
const eq = (a,b) => a == b


function reverseNumber(n){
    let i = 0
    let sign = ''   
    if (n && n[i]==='-') {
        sign = '-'
        n = n.slice(i+1,)
    } 
    if (n && n.length < 2) {
        return sign + n
    }

    
   // let currCompare = detectState(n[i+1], n[i])
    let newN = ''

    let indStart = i
     
    let currState = {state:"new", func:0}
    currState = detectState(n[i+1],n[i], currState)
    
    while (i < n.length - 1) {
        if (currState.func(n[i+1],n[i])) {
            i++;
        } else if (currState.state == "new") {
            currState = detectState(n[i+1],n[i], currState)
            i++;
        } else {
            prevState = currState.state
            currState = detectState(n[i+1],n[i], currState)
            if (currState.state == prevState) { //means we stepin flat area just continue
                i++;
                continue;
            } else {   
                newN += reverseSimple(n.slice(indStart, i+1))
                indStart = i + 1
                i += 1
                currState = detectState(n[i+1],n[i], currState)
                if (n[i+1]==n[i]) currState.state ="new"
                console.log(newN, currState)
            }
        } 
    }
    newN += reverseSimple(n.slice(indStart, i+1))
    while (newN[0]==0 && newN) {
        newN = newN.slice(1,)
    }

    return sign + newN
}
    

  
num = "133555224466"

console.log(reverseNumber(num))
  //13555432  ---> 55531234
  //133555224466  ---> 555331664422
 
  //-944296080987685186970776058150602324469718894358
  //-944290896876085197086057760812360524461889735894
  
//   -944296080987685186970776058150602324469718894358
//   -944296088760985186970776058150602324469718894358