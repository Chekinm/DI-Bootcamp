import {useSelector, useDispatch} from 'react-redux';
import reducer, { DEFAULT_CITY, 
                  ADD_TO_FAVORITE_CITIES_LIST, 
                  DELETE_FROM_FAVORITE_CITIES_LIST }  from '../redux/reducer'

import React, { useEffect, useState } from 'react';
import axios from 'axios';


const HandleFavoritesList = () => {

    const dispatch = useDispatch()
    const currentCityId = useSelector(state => state.currentCity) 
    // const favoriteCitiesList = useSelector(state => state.favoriteCitiesList)
    const favoriteCitiesList = useSelector(state => state.favoriteCitiesList) 
    const [isInFavoriteList, updateFavoriteList] = useState(true)
        // ()=>{
        //                                     favoriteList.includes(currentCityId)})
    
   
    useEffect(() => {
        console.log('check favotites')
        console.log(favoriteCitiesList)
        updateFavoriteList(favoriteCitiesList.includes(currentCityId))
        
    },[currentCityId, favoriteCitiesList])
    
    const addToFavoriteList = (e) => {
        dispatch({type: ADD_TO_FAVORITE_CITIES_LIST, payload:currentCityId})
        console.log(favoriteCitiesList)
    }

    const deleteFromFavoriteList = (e) => {
        dispatch({type: DELETE_FROM_FAVORITE_CITIES_LIST, payload:currentCityId})
        console.log(favoriteCitiesList)
    }


    return (
        <div>
            <div>Is current city in favorites?:  {String(isInFavoriteList)}</div>
            <button name='handleFavorites' 
                    onClick={isInFavoriteList? deleteFromFavoriteList : addToFavoriteList }>
                {isInFavoriteList? 'Delete from Favorites': 'Add to favorites'}
            </button>    
        </div>
    )
}

export default HandleFavoritesList