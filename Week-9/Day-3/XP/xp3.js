const epic = ['a', 'long', 'time', 'ago', 'in a', 'galaxy', 'far far', 'away'];

let realEpicString = "May the force be with you!" //just kidding

let epicString = epic.reduce((total, word)=>total+=word+' ').trim()
console.log(epicString)