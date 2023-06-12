import React from 'react';
import { useState, useEffect} from 'react';
import './App.css';
import Card from './Card';
import 'tachyons'
// import robots from './robots'


const App = () => {
    
    const [state, setState] = useState([]) 

    let searchValue = ''

    const fetchUsers = (state,searchValue) => {
        fetch('https://jsonplaceholder.typicode.com/users')
        .then((data)=> data.json())
        .then((data)=> {
            console.log('searchValue=',searchValue)
            state = setState(data.filter(robot => robot.name.includes(searchValue)))
        })
        // state = setState(robots)
    }

    

    const filterRobots = (e) => {
        searchValue = e.target.value
        fetchUsers (state,searchValue)
    }
    
    return(  
        <div>
            <div className='header tc f1 pa2'>ROOBOTS</div>
            <div className='tc f1' >
                <input type="text" placeholder='Filter Robots' onChange={(e)=>filterRobots(e)}></input>
            </div>
            { state.map((robot,indx) => {
                return <Card properties={robot} key={indx}/>
                })
            } 
            <button onClick={filterRobots}>FetchUsers</button>
        </div>)

}

export default App