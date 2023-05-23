

const searchWord = (str, pattern) => {
    counter = 0
    let splitedStr = str.split(' ')
    splitedStr.forEach((word)=> word == pattern && counter++) 
    return (counter) ? `${pattern} was found ${counter} times`:`${pattern} was not found`
  }
  
console.log(searchWord('The quick brown fox', 'fox')); 
  