const menu = [
  {
    type : "starter",
    name : "Houmous with Pita"
  },
  {
    type : "starter",
    name : "Vegetable Soup with Houmous peas"
  },
  {
    type : "dessert",
    name : "Chocolate Cake"
  }
]
//1
meal1 = {
  type: "dessert",
  name: "tart du pomme"
}

meal2 = {
  type: "main course",
  name: "steak"
}


//1.1
const haveMealWithType = (type)=> (menu.some((elem)=>elem.type==type))
console.log('do we have a desert?',haveMealWithType("dessert"))
//1.2
const isAllMealHaveType = (type) => (menu.every((elem)=>elem.type==type))

console.log('is our meals are all starter?', isAllMealHaveType("starter"))
//1.3
const addMealIfNotInTheMenu = (meal) => (haveMealWithType(meal.type) || menu.push(meal))

addMealIfNotInTheMenu(meal1) // should not add anything
console.log('do we have a main course', haveMealWithType("main course"))
console.log('what is current menu lenght', menu.length) //cannot snapshot the object, 
//if  I console.log it, it will show changed state with 4 meals


addMealIfNotInTheMenu(meal2) //should add steak as main course
console.log('ok. do we have main course now?', haveMealWithType("main course")) //shoudl be true
console.log(menu)

//1.4
const vegetarian = ["vegetable", "houmous", "eggs", "vanilla", "potatoes" ]

const isVegitarian = (str) => {
          let splitedStr = str.split(' ')
          let resp = false
          splitedStr.forEach((word)=> resp = resp || (vegetarian.includes(word.toLowerCase()))) 
          return resp
        }
        

menu.forEach((elem)=>(elem.vegetarian=isVegitarian(elem.name)))
console.log('now we add vegetarian properties\n',menu)


