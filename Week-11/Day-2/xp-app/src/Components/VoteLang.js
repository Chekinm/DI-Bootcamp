import React from "react";
import { useState } from "react";
import './VoteLang.css'

const VoteLang = (props) => {

    const [state, setState] = useState({
                    votes: props.lang.votes,
                    name: props.lang.name
                })
    console.log(state)

    const vote = () => {
        setState({
            votes: state.votes + 1,
            name: state.name
        })
    }
    
    return (
        <div className='container'>
        <div>{state.votes}</div> 
        <div>{state.name}</div> 
        <div id='clickable' onClick={vote}>Click Here</div>
        </div>
    )     
}

export default VoteLang