let fs = require('fs');
// const fs = require('fs').promises;
let newContent = "Caesar Salad"

// fs.appendFile('menu.txt', newContent + '\n', function (err) {
//     if (err) {
//         console.error(err)
//         return
//     }
// });

// fs.readFile('menu.txt', 'utf-8', function (err, data) {
//     if (err) {
//         console.error(err)
//         return
//     }

//     console.log(data)
// });

console.log("-----Restaurant Menu---------", '\n',);


async function myfile() {
  return  fs.promises.readFile('menu.txt', 'utf-8', function (err, data) {
    if (err) {
        console.error(err)
        return
    }
    });

}

myfile().then((d)=>console.log(d))
// console.log(a, 'from async')
// a.then((data) => {
//     console.log(data,'form then')
// })