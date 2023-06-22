
import { useSelector, useDispatch } from 'react-redux';
import React, { useEffect, useState } from 'react';
import { SET_CITY } from '../redux/reducer';
import { Routes, Route, Link } from 'react-router-dom';
import Weather from './Weather';




const Faivorites = () => {
    const dispatch = useDispatch()
    const favoriteCitiesList = useSelector(state => state.favoriteCitiesList)
    const showDetailed = (e) => {
        console.log(e.target)
        dispatch({type:SET_CITY, payload: {id:e.target.id, name: e.target.innerHTML}})
          
    }
    
    console.log(favoriteCitiesList)
    
    return (
    
         <div className="list">

            <Routes >
            <Route path='/Weather/' element={<Weather />}/>
            </Routes>
                   {/* <h1>{String(error)}, {String(isLoading)}</h1>
                {error && <p>{error}</p>}
                {isLoading && <p className="loading">Loading...</p>} */}
                <div className="list">
                    {favoriteCitiesList.map((item, index) => (
                        <div className="list-item"
                            name={item.id}
                            key={item.id}
                            onClick={showDetailed}>
                            <Link to='/Weather/' id={item.id}>{item.name}</Link>
                        </div>
                    ))}
                </div>
            </div>

       
        
     ) 

}
    
     
export default Faivorites