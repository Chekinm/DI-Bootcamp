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


