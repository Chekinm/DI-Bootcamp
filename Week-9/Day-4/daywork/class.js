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

// class C {
//     x=5;
//     constructor (name) {
//         this.name = name
//     }
//     static getX(obj) {
//       return `${obj.x}`;
//     }
//   }
  
// let a = new C('a')
// let b = new C('b')
//   console.log(b.x,a.name); // undefined
//   //console.log(C.getX({})); // TypeError: Cannot read private member #x from an object whose class did not declare it

// function* nums (nums) {
//   let i = 0
//   while (i < 10) {
//     yield i
//     i++
//   }
// }


// let newgen = nums()

// let a =[1,2,3]

// console.log(a.prototype)

const input1 = [1, 2, 4, 591, 392, 391, "2", 5, 10, 2, "1", "1", 1, 20, 20];

const makeOrder = (arr) => {
  let dictObj = {}
  for (num of input1) {
    if (num in dictObj) {
      dictObj[num].push(num)
    } else {
      dictObj[num] = [num,]
    }
  }
  for (let [key, value] of Object.entries(dictObj)) {
    console.log([key,value])
  }
}

makeOrder(input1)


const makeOrderByType = (arr) => {
  let dictObj = {}
  for (num of input1) {
    if (typeof(num) in dictObj) {
      dictObj[typeof(num)].push(num)
    } else {
      dictObj[typeof(num)] = [num,]
    }
  }
  for (let [key, value] of Object.entries(dictObj)) {
    console.log([key,value])
  }
}

makeOrder(input1)
makeOrderByType(input1)


