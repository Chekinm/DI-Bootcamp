// //1.1
// let landscape = function() {

//     let result = "";
   
//     let flat = function(x) {
//       for(let count = 0; count<x; count++){
//         result = result + "_";
//       }
//     }
   
//     let mountain = function(x) {
//       result = result + "/"
//       for(let counter = 0; counter<x; counter++){
//         result = result + "'"
//       }
//       result = result + "\\"
//     }
   
//     flat(4);   // result ="____" //4 times _
//     mountain(4); //result = "____/''''\"  as result is global (second slash is just to decorate)
//     flat(4) ////result = "____/''''\____"  as result is global
   
//     return result; // result = "____/''''\____"
//    }
   
//    landscape()  //nothin happen as we don't assing return anywhere
   
   // ex2

let landscape =() => {

    let result = "";
   
    let flat =(x)=> {
      for(let count = 0; count<x; count++){
        result = result + "_";
      }
    }
   
    let mountain = (x) => {
      result = result + "/"
      for(let counter = 0; counter<x; counter++){
        result = result + "'"
      }
      result = result + "\\"
    }
   
    flat(4);   
    mountain(4); 
    flat(4) 
    return result; 
   }
   
landscape() 

//EX2
const addTo = x => y => x + y;
const addToTen = addTo(10); //return function aaToTen = y => 10+y
addToTen(3); // 13


//EX3

const curriedSum = (a) => (b) => a + b
curriedSum(30)(1) //returns 31



//ex4

const curriedSumnew = (a) => (b) => a + b
const add5 = curriedSumnew(5) //returns (b) => 5+b
add5(12) // 17 


//ex5

const compose = (f, g) => (a) => f(g(a));
const add1 = (num) => num + 1;
const add5 = (num) => num + 5;
compose(add1, add5)(10)

// g(a) - add5(10) = 15
//f(g(a)) add1(g(a))=add1(15)=
//shoudl return 16
