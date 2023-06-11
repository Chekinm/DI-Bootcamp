import React from 'react'

const UserFavoriteColors = (props) => {

    const animals = props.favAnimals
        
    return (
        animals.map((animal, ind) =><li key={ind}>{animal}</li>)
    )
}

export default UserFavoriteColors