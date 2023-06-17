import React from "react";


const AnswersApp = (props) => {
    console.log('heelo form answer',props.data)
    const data = props.data
    return (
        <div>
            <p>First name: {data.firstName}</p>
            <p>Last name: {data.lastName}</p>
            <p>Favorite color: {data.favoriteColor}</p>
            <ul>Favorite drinks:
                <li>beer: {(data.beer)? 'yes':'no'}</li>
                <li>wine: {(data.wine)? 'yes':'no'}</li>
                <li>vodka: {(data.vodka)? 'yes':'no'}</li>
            </ul>
            <p>Gender: {data.gender}</p>
        </div>
    )
} 
export default AnswersApp