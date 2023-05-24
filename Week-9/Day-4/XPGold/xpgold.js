function printFullName(person) {
    let {first, last} = person
    return `Your full name is ${first} ${last}`
}


console.log(printFullName({first: 'Elie', last:'Schoppik'})) 
// 'Your full name is Elie Schoppik`



//ex2

const keysAndValues=(obj) => [Object.keys(obj).sort(), Object.keys(obj).sort().map((key)=>obj[key])]
//sorry for that
// we have a kind of challange to write it in on string
// I know that it is not a good way to do things.


console.log(keysAndValues({ b: 2, a: 1, c: 3 }))
console.log(keysAndValues({ a: "Apple", b: "Microsoft", c: "Google" }))
console.log(keysAndValues({ key1: true, key3: undefined, key2: false }))


// ex3 

class Counter {
    constructor() {
      this.count = 0;
    }
  
    increment() {
      this.count++;
    }
  }
  
  const counterOne = new Counter(); // counterOne.count = 0
  counterOne.increment(); // counterOne.count = 1
  counterOne.increment(); // counterOne.count = 2
  
  const counterTwo = counterOne; // i'm not sure, but since class is an object
  // and count is just a properties. And we don't run a new which invoke constructer
  // it shoudl be one and the same object so 
  counterTwo.increment(); //  counterTwo.count = 3 , as well as 
  
  console.log(counterOne.count); //counterTwo.count = 3
