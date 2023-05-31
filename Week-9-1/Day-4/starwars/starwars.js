async function getStarWarsApiData (endpoint) {
    // try is catching  network error
    
    try {
        const response = await fetch(endpoint);
        //console.log("response", response)
        let data = await response.json();
        //console.log("data", data.result.properties.height);
        return data;
    } catch (error) {
        networkErrorPrinout(error)
    }
  }





async function showData(event) {
    event.preventDefault();
    let container = document.getElementById("container")
    container.innerHTML = '<div class="fa-3x"><i class="fa-solid fa-sync fa-spin"></i><p>Loading</p></div>' 
    
    let data = await getStarWarsApiData("https://www.swapi.tech/api/people/" + Math.round(Math.random() * 83));
    if (data.message === "ok") {
        charData = data.result.properties
        // process homeworld link ca ll getStarWarsCharacter
        let homeworld = await getStarWarsApiData(charData.homeworld)
        let homeworldName;
        if (homeworld.message === "ok") {
            homeworldName = homeworld.result.properties.name
        } else {homeworldName = "Top secret"}

    
        container.innerHTML = `
                    <span class="name">${charData.name}</span>
                    <p> Height: ${charData.height}</p>
                    <p> Gender: ${charData.gender}</p>
                    <p> Birth year: ${charData.birth_year}</p>
                    <p> HomeWorlds: ${homeworldName}</p>
                    `
    } else if (data.message === "not found") {
        container.innerHTML = `
                    <span class="name">Character not found</span>
                    `
    }
} 


function networkErrorPrinout (error) {
    let container = document.getElementById("container")
    container.innerHTML = `
        <div class="fa-3x"><i class="fa-solid fa-sync fa-spin"></i>
            <div class="error">
                <p>Network Error</p>
                <p>${error}</p>
                <p>Try again later!</p>
            </div>
        </div>
        `
}

