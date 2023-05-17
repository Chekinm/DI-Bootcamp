let planets = {
    "Mercury":{
        "size": 2440,
        "moons": []
    },
    "Venus": {
        "size": 6052,
        "moons": []
    },
    "Earth": {
        "size": 6371,
        "moons": ["Moon"]
    },
    "Mars": {
        "size": 3390,
        "moons": ["Phobos", "Deimos"]
    },
    "Jupiter": {
        "size": 69911,
        "moons": ["Io", "Europa", "Ganymede", "Callisto"]
    },
    "Saturn": {
        "size": 58232,
        "moons": ["Mimas", "Enceladus", "Tethys", "Dione", "Rhea", "Titan", "Hyperion", "Iapetus", "Phoebe"]
    },
    "Uranus": {
        "size": 25362,
        "moons": ["Ariel", "Umbriel", "Titania", "Oberon", "Miranda"]
    },
    "Neptune": {
        "size": 24622,
        "moons": ["Triton", "Nereid"]
    }
}


function rnd() {
     return Math.round(Math.random()*255)
}

function createSpaceObject(name, className, size, pos_right, parent) {
    let new_object = document.createElement('div')
    new_object.className=className +' '+name.toLowerCase()
    new_object.style.background = 'rgb(' + rnd() + ',' + rnd() + ',' + rnd() + ')';
    new_object.style.cssText += `width: ${size/50}px;`
    new_object.style.cssText += `height: ${size/50}px;`
    new_object.style.cssText += `right: ${-pos_right/2}px;`
    let plName = document.createTextNode(name)
    new_object.appendChild(plName)
    parent.appendChild(new_object)
    return new_object
}

for (let planet in planets) {
    moon_list = planets[planet].moons
    const solarSystem = document.querySelector('.listPlanets')
    let planet_obj = createSpaceObject(planet, 'planet', planets[planet].size, 0, solarSystem)
    
    for (let moon of moon_list) {
        let moon_obj = createSpaceObject(moon, 'moon', 3000, planets[planet].size/50, planet_obj)

    }
}
const solarSystem = document.querySelector('.listPlanets')
console.log(solarSystem)


