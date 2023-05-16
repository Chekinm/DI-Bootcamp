// JAVASCTIP TYPES 
// ------------------
// 1. Number
// 2. String
// 3. Boolean
// 4. Undefined
// 5. null

// JAVASCRIPT VARIABLE
// -------------------

// var
// let (new in ECMAScript 6)
// const( new ECMASScript 6)
// let a;
// a = 134555;

// const MY_CONST="CONSTANT"
// let nameMike;

// let str = 'My long string';
// let b = String(a);
// console.log(Number(b.slice(0,3)));
// let c='AaZz'

// let str3 = `${c} ${b}`
// console.log(str3.charCodeAt(0),
//             str3.charCodeAt(1),
//             str3.charCodeAt(2),
//             str3.charCodeAt(3)
//             )



// let addressNumber = 13
// let addressStreet = 'Rashi'
// let country = 'Israel'
// let globalAddress = `${addressNumber} ${addressStreet} ${country}`
// console.log(globalAddress)

// let str = (addressNumber.toString()+'s') 
// console.log(str)

// let a ='aaaaa'

// let f =['a','b',123123, true,[1,2,a]]
// let toString = f.pop()
// console.log(f.toString(), toString)
// console.log(f.pop())

// f.pop()
// console.log(f.toString())
// console.log(f.slice(-1))
// let arra = [1,2,3]
// let a = {
//     x: 1,
//     b: 2,
//     name: 'MIke',
//     arr: [1,2,3],
//     aa: {a:10},
//     f: function(arg) {
//         alert(arg + this.name)
//     }
// }

// console.log(a.aa)
// a.f('Hello ')
// let isBoss = confirm("Are you the boss?");
// alert(isBoss); // true if OK is pressed



// let person1 = {
//     username: 'Mike',
//     password:  '',
// }

// let person2 = {
//     username: 'Jone',
//     password:  '',
// }

// let person3 = {
//     username: 'Fred',
//     password:  '',
// }

// let database = [person1, person2, person3]


// let new1 = {
//     author: database[0],
//     timeline:  '',
// }

// let new2 = {
//     author: database[1],
//     timeline:  '',
// }

// let new3 = {
//     author: database[2],
//     timeline: '',
// }


// let newsfeed = [new1, new2, new3]

// console.log(newsfeed)

// newsfeed[1].timeline = 'news news'

// console.log(newsfeed)



// let page = 1

// switch (page) {
//     case 1:
//         console.log('this is' + 1);
//         break;
//     case 2:
//         console.log('this is' + 2);
//         break;
//     case 3:
//         console.log('this is' + 3);
//         break;
//     default:
//         console.log('this is' + 'default');
//         break;
// }



let person1 = {
    username: 'Mike',
    password:  '',
}

let database = [person1]
//---------------
database[0].password = 'admin'
console.log(database)
console.log(database[0])
console.log(database[0].password)



console.log ('--------------------------------')

if (database[0].password == 'admin') {
    console.log('correct')
    console.log(database[0].password)
}
else{
    console.log('wrong')
    console.log(database[0].password)
}
//--------------------

//--------------------
database[0].password = 'newpass'
console.log(database)


if (database[0].password == 'admin') {
    console.log(database[0].password)
}
else{
    console.log('wrong')
    console.log(database[0].password)
}
//------------------