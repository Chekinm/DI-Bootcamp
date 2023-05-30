const promise1 = Promise.resolve(3);
const promise2 = 42;
const promise3 = new Promise((resolve, reject) => {
  setTimeout(resolve, 3000, 'foo');
});
// expected output: Array [3, 42, "foo"]

const collector = (arr) => Promise.all(arr)

collector([promise1,promise2,promise3])
.then(res=>console.log(res))

//ex2 supposed to be a printable representation of array=[2,4,6]