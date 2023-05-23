console.log('---------------------------ex Second----------------')




function mergeWords(string) {
    return function(nextString) {
      if (nextString === undefined) {
        return string;
      } else {
        return mergeWords(string + ' ' + nextString);
      }
    }
   }

// let a = mergeWords('aaa')
// console.log(a)   
// b = a('mike')
// c = b ('john')
// console.log(c(undefined))
console.log(mergeWords('jj')('kk')('kkk')('jjjj')())


//console.log(mergeWords('There')('is')('no')('spoon.')())