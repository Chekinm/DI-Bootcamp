import React from 'react'

const stylePlanets = {
    color: "black",
    backgroundColor: "white",
    padding: "10px",
    fontFamily: "Arial",
    fontSize: "2rem",
    listStyleType: "none",
    
  };

const planetStyle = {
    padding: "20px",
    border: "solid 1px lightgrey"

}


const Planets = (props) => {
    const planets = props.planets
    console.log(planets)
    return (
        <div> 
            <ul style={stylePlanets}> 
                {planets.map((planet, indx) => {
                    return <li style={planetStyle} key={indx}>{planet}</li>
                })
                }
            </ul>
        </div>
    )

}

export default Planets