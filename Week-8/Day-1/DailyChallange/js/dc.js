// Create a variable called sentence. The value of the variable 
// be a string that contains the words “not” and “bad”.

let sentence = "Not bad, not bad. The movie is not that bad. I like it. Surely it's not so bad"
a = sentence.toLowerCase() 


while (true) {
    sentenceLowerCase = sentence.toLowerCase()
    let wordNot = sentenceLowerCase.indexOf('not');
    let wordBad = sentenceLowerCase.indexOf('bad');
    let insert = (wordNot == 0) ? 'Good' : 'good'
    if (wordBad > wordNot) {
        sentence = sentence.slice(0,wordNot) + 
                    insert +
                    sentence.slice(wordBad+3, sentence.length);
    }
    else  {
        break;
    }
}

console.log(sentence)

// ---------------DC gold -------------------------


let numOfBranch = 6
let width = (numOfBranch*2)**2  + 3 

function buildDrawLine(size, numOfStar) {
    let drawLine = []
    for (let j=0; j < size; j++) {
        let curSim = (j >= (size - numOfStar)/2 &&  j < (size + numOfStar)/2) ? '*':' '
        drawLine.push(curSim)
        }
    return drawLine.join('')
    }

for (let n=2; n < numOfBranch * 2; n+=2) {
    for (let k=1; k<=3 + n*n ; k += n+2){
        drawLine = buildDrawLine(width,k)
        console.log(drawLine)
        }
   }
