const morse = `{
  "0": "-----",
  "1": ".----",
  "2": "..---",
  "3": "...--",
  "4": "....-",
  "5": ".....",
  "6": "-....",
  "7": "--...",
  "8": "---..",
  "9": "----.",
  "a": ".-",
  "b": "-...",
  "c": "-.-.",
  "d": "-..",
  "e": ".",
  "f": "..-.",
  "g": "--.",
  "h": "....",
  "i": "..",
  "j": ".---",
  "k": "-.-",
  "l": ".-..",
  "m": "--",
  "n": "-.",
  "o": "---",
  "p": ".--.",
  "q": "--.-",
  "r": ".-.",
  "s": "...",
  "t": "-",
  "u": "..-",
  "v": "...-",
  "w": ".--",
  "x": "-..-",
  "y": "-.--",
  "z": "--..",
  ".": ".-.-.-",
  ",": "--..--",
  "?": "..--..",
  "!": "-.-.--",
  "-": "-....-",
  "/": "-..-.",
  "@": ".--.-.",
  "(": "-.--.",
  ")": "-.--.-"
}`



const toJSON = (JSONstr) => new Promise ((resolve,reject)=>{ 
  let morseObj;
  try {
    morseObj = JSON.parse(JSONstr)
  } catch (error) {
    reject("we have brocken JSON")
  }
  resolve(morseObj)
}) 

const userInput = (morseObj) => new Promise ((resolve,reject)=>{
    let textArr = prompt("Enter your text").trim().split(' ')
    let morsedArr = []
    let i = 0;
    for (word of textArr) {
      morsedArr.push([])
      for (char of word) {
        if (!(char in morseObj)) {
          reject(`${char} is not in morse code table`)
        } else {
          morsedArr[i].push(morseObj[char])
        }
      }
      i++;
    }
    resolve(morsedArr)
})

const makeArrPrintable = (morsedArr) => {
  let tempArr = []
  for (morsedWord of morsedArr) { 
    //join char in word using line break
    tempArr.push(morsedWord.join('\n'))
    //add empty element between word
    tempArr.push(' ')
  }
  //create final text  
  return tempArr.join('\n')
  
}

toJSON(morse)
.then(morseObj=>{
  return userInput(morseObj) 
})
.then((morsedArr) => {
  
  return makeArrPrintable(morsedArr)
})
.then(res => console.log(res))

.catch(err=>console.log(err))