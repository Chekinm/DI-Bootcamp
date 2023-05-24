// Ex 1

const person = {
    name: 'John Doe',
    age: 25,
    location: {
        country: 'Canada',
        city: 'Vancouver',
        coordinates: [49.2827, -123.1207]
    }
}

const {name, location: {country, city, coordinates: [lat, lng]}} = person;

console.log(`I am ${name} from ${city}, ${country}. Latitude(${lat}), Longitude(${lng})`);


// I am Jone Doe from  Vancouver, Canada. Latitude(49.2827), Longitude(-123.1207)

//2 

function displayStudentInfo(objUser){
    let {first, last} = objUser 
    return `Your full name is ${first} ${last}`
}

console.log(displayStudentInfo({first: 'Elie', last:'Schoppik'}));

// Ex3.1 - 3.2 (remove *2 on line 37 to get 3.1 back) 

const users = { user1: 18273, user2: 92833, user3: 90315 }


const getArr = (users) =>{ 
    let result = []
    for (let [key, value] of Object.entries(users)) {
        result.push([key,value*2])  // 
    }
    return result
}

let a = getArr(users)
console.log(a)

//Ex4

class Person {
    constructor(name) {
      this.name = name;
    }
  }
  
  const member = new Person('John');
  console.log(typeof member);
  console.log(member instanceof Person)
  

  // it returns object, i've tryied it in class. To check if it is insance of Person
  // you need to call (member instanceof Person)


  //ex5
class Dog {
    constructor(name) {
        this.name = name;
    }
};

// part 1

// number 2 does the job well

  // 2
  class Labrador extends Dog {
    constructor(name, size) {
      super(name);
      this.size = size;
    }
  };


  // ex 
console.log('---------------------------Ex6------------------------')

console.log('{} === {}', {} === {}) 
console.log('[] === []', [] === [])
//that's ok
//i'm wonder why next is false???
console.log('{} == {}', {} == {}) 
console.log('[] == []', [] == [])

console.log('[2]==[2]', [2]==[2])

a = {1:2}
b = a
console.log(a === b) //this gives true obvously

a = {1:2}
b = structuredClone(a)
console.log(a === b)

// by the way in python it will be the == got 'true' for objects with equal content
// and is function (which is analogue for ===) is getting false, which is a little
// bit more logical. But ok. will see. 


// 2

const object1 = { number: 5 }; 
const object2 = object1; 
const object3 = object2; 
const object4 = { number: 5};

object1.number = 4;
//(set the value of object1.number to 4)
console.log(object1.number)

console.log(object2.number)
// this gives us 4 as we change it step before and object 2 is a copy of obje 1

/console.log(object3.number)

// same.  this gives us 4 

console.log(object4.number)
// this gives us 5 as object4 is compitly different object.

