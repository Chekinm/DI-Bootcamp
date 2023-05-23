//1
[1, 2, 3].map(num => {
    if (typeof num === 'number') return num * 2;
    return ;
  })

//if we assign it to variabel will got [2,4,6]

//2

[[0, 1], [2, 3]].reduce(
    (acc, cur) => {
      return acc.concat(cur);
    },
    [1, 2],
  );

 //  returns [1, 2, 0, 1, 2, 3]


 // 3 
const arrayNum = [1, 2, 4, 5, 8, 9];
const newArray = arrayNum.map((num, i) => {
    console.log(num, i);
    alert(num);
    return num * 2;
})

// console whould be
// 1, 0
// 2, 1
// 4, 2
// 5, 3
// 8, 4
// 9, 5
// alerts would be 1, 2, 4, 5, 8, 9.
// newArray whould be  [2,4,8,10,16,18]