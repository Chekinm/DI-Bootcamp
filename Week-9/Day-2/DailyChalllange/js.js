const gameInfo = [
    {
      username: "john",
      team: "red",
      score: 5,
      items: ["ball", "book", "pen"]
    },
    {
      username: "becky",
      team: "blue",
      score: 10,
      items: ["tape", "backpack", "pen"]
    },
    {
      username: "susy",
      team: "red",
      score: 55,
      items: ["ball", "eraser", "pen"]
    },
    {
      username: "tyson",
      team: "green",
      score: 1,
      items: ["book", "pen"]
    },
   ];
//1
let userinfo = []
gameInfo.forEach((user)=>userinfo.push(`${user.username}!`))
console.log(userinfo)

//2
let winners = []
gameInfo.forEach((user)=>(user.score<=5 && winners.push(user.username)))
console.log(winners)

//3
let total = 0
gameInfo.forEach((user)=>(total +=user.score))
console.log(total)
