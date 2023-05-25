const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/3?200x200'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/4?200x200'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/5?200x200'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/6?200x200'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/7?200x200'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/8?200x200'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/9?200x200'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/10?200x200'
    }
    ];





// console.log(robotsContaier)
function drawRobots (robotsFiltered) {
    for (let robot of robotsFiltered) {
        
        // get robot card tamplated from html file
        robotTemplate = document.getElementById("template")
        
        // clone it. Got new node robotCard
        let robotCard = robotTemplate.cloneNode(true)

        // fill card with information from robots list
        robotCard.id = robot.id
        robotCard.classList.remove("d-none")
        robotCard.children[0].children[0].src = robot.image
        robotCard.querySelector("p.name").innerText = robot.name
        robotCard.querySelector("a.emaillink").innerText = robot.email
        robotCard.querySelector("a.emaillink").href = `mailto:${robot.email}`
        
        
        // appedn new card to the Parent container
        robotsContaier.appendChild(robotCard)
    }
}


let robotsFiltered = []
let robotsContaier = document.getElementById("robots")

function searchRobot(event) { //on search button

    event.preventDefault()
    
    let searchText = document.getElementById("search-text").value
    robotsFiltered = robots.filter((e)=>e.name.toLowerCase().includes(searchText.toLowerCase()))
    //clear everything befor draw filtered content
    robotsContaier.innerHTML = ""
    //draw filtered list
    drawRobots(robotsFiltered)
 
}

//we need to draw all robots first

drawRobots(robots)