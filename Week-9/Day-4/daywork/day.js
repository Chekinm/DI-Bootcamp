function findMinDistInArr (arr) {

    let indexes = {};
    for (i=0; i < arr.length;i++) {
        //this loop is run for O(n)
        if (arr[i] in indexes) { 
            //this operation runs for O(1) as Object are hashed
            // ussally we prefer to search in obj key rather then 
            //search in arr by value, as it way too faster
            indexes[arr[i]].push(i)
        }else{
            indexes[arr[i]] = [i,]
        }
        }  
    //so we have an hashmapped object wich contain lists of indxes 
    // of any particular number for each number in array
    // it is important that we can searh over object key for O(1)
    // as we goind to do this below. YOu can look on it
    console.log(indexes)

        
    let min = Infinity // which is bigger than any given number
    for (elem in indexes){  
        let len = indexes[elem].length
        while (len-1 > 0) {  
            dist = indexes[elem][len-1]-indexes[elem][len-2]
            if (dist < min) {
                min = dist
            } 
            len--;
        }
        //this two loops also runs for O(n) as we have total n indexes
        //packed in some way, but sum of tow loops will be N  
    }
    
    return min

    // so we have it for O(n)
    }

arr = [1,2,3,4,5,6,7,8,9,3,1,10,3,11,1,]
console.log(findMinDistInArr(arr))




function findSmallestDistance(numbers) {
    let smallestDistance = Infinity;
    let indexMap = {};
  
    for (let i = 0; i < numbers.length; i++) {
      let number = numbers[i];
      if (number in indexMap) {
        let distance = i - indexMap[number];
        smallestDistance = Math.min(smallestDistance, distance);
      }
      indexMap[number] = i;
    }
    console.log(indexMap)
    return smallestDistance === Infinity ? -1 : smallestDistance;
  }

  console.log(findSmallestDistance(arr))