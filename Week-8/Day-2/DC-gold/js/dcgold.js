function isAlpha (value) {
    return (value) && /^[a-zA-Z]+$/.test(value);
}

function isNumeric(value) {
    return (value) && !isNaN(value) 
}

function getUserInput(text, checkFunction) {
    let input;
    do {
        input = prompt (text);
    } while (!checkFunction(input));
    return input;
};

function buildString(word, box_size) {
    numOfSpases = box_size - word.length - 3
    stringToPrint = '*' + ' ' + word + ' '.repeat(numOfSpases) + '*'
    return stringToPrint
    }

const NUM_OF_INPUT = getUserInput('How many word woudl you like to enter: ', isNumeric);
let arrWords = [];
let max_len = 0;

for (i=0; i<NUM_OF_INPUT; i++) {
    let word = getUserInput('Enter word', isAlpha);
    max_len = Math.max(max_len, word.length);
    arrWords.push(word);
};

console.log('*'.repeat(max_len+4))
for (let word of arrWords) {
    console.log(buildString(word, max_len+4))
}
console.log('*'.repeat(max_len+4))

