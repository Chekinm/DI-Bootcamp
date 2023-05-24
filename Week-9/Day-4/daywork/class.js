// class Animal {
//     #name
//     constructor(name="PrototAnimal") {
//         this.#name = name;
//     }
//     speak () {
//         console.log(`${this.#name} makes noise`)
//     }
//     getName(){
//         return this.#name
//     }
// }


// class Dog extends Animal {

//     speak () {
//         console.log(`${this.name} barks`)
//     }

// }
// class Cat extends Animal {

//     speak () {
//         console.log(`${this.name} meow`)
//     }

// }


// let b = new Dog("archi")

// let an = new Animal
// b.speak()
// console.log(an.name)
// console.log(b.getName())
// console.log(b instanceof Cat)

class C {
    x=5;
    constructor (name) {
        this.name = name
    }
    static getX(obj) {
      return `${obj.x}`;
    }
  }
  
let a = new C('a')
let b = new C('b')
  console.log(b.x,a.name); // undefined
  //console.log(C.getX({})); // TypeError: Cannot read private member #x from an object whose class did not declare it
