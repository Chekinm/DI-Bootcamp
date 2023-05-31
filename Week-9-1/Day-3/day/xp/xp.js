async function* asyncFor1() {
  for (let j=0;j<200;j++){
       if (j%2 == 0){
        
        
        
        yield (j+' '+ await fetchSunRise("https://api.sunrise-sunset.org/json?lat=32.0853&lng=34.7818"), arr);

      }
    }
  }

async function* asyncFor2() {
  for (let i=0;i<2000000000;i++){
      if (i%20000000 == 0){
        
        
        yield i
      }
    }
  }
          


async function call1(gen) {
  let tmp1 = await gen.next()
  arr.push(tmp1.value)
}
async function call2(gen) {
  let tmp2 = await gen.next()
  arr.push(tmp2.value)
}



c


let gen1 = asyncFor1()

let gen2 = asyncFor2()

let arr = []


console.log('first')


for (let k=0;k<50;k++){
  
  call1(gen1) //.then(res=>arr.push(res))
}
setTimeout(()=>console.log('tt0'),0)
for (let i=0;i<50;i++){
 
  call2(gen2) // .then(res=>arr.push(res))
}
setTimeout(()=>console.log('tt10'),10)


console.log('after')
setTimeout(()=>console.log(arr),2000)


