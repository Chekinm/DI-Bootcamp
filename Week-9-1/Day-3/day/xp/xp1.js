
  function* asyncFor() {
    for (let i=0;i<20;i++){
        if (i%2 == 0){
          
          yield i
        }
      }
    }
            
 
  async function call(gen) {
    let tmp = await gen.next()
    arr.push(tmp.value)
  }

  

  
  let gen = asyncFor()
    
  let arr = []
  

  for (let i=0;i<5;i++){
   
    call(gen) // .then(res=>arr.push(res))
  }
  
  
  console.log('after')
  setTimeout(()=>console.log(arr),1000)
  
  
  