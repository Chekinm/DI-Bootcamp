import React from 'react'
import reactImage from './react.png'
import './Exercise4.css'

const style_header = {
    color: "white",
    backgroundColor: "DodgerBlue",
    padding: "10px",
    fontFamily: "Arial"
  };


const Exercise4 = (props) => {
    
    return (
        <div>
            <h1 className='header' style={style_header}>This is Header</h1>
            <p className='para'>This is paragraph</p>
            <a href='www.google.com'>This is a link</a>
            <form>
                <h3>This is a form</h3>
                <p>Enter your name</p>
                <input type='text'></input>
                <button type="submit">Submin</button>
            </form>
            <p></p>
            <img src={reactImage} alt='reactimage'></img>
    
            <p>This is a list</p>
            <ul> 
                <li>Coffee</li>
                <li>Tea</li>
                <li>Milk</li>
            </ul>
        </div>
    )

}

export default Exercise4