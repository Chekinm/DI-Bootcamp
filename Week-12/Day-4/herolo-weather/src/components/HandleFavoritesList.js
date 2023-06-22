import {useSelector, useDispatch} from 'react-redux';
import  { ADD_TO_FAVORITE_CITIES_LIST, 
          DELETE_FROM_FAVORITE_CITIES_LIST }  from '../redux/reducer'

import React, { useEffect, useState } from 'react';


const HandleFavoritesList = () => {

    const dispatch = useDispatch()
    const currentCityId = useSelector(state => state.currentCity.id) 
    const currentCityName = useSelector(state => state.currentCity.name) 
    
    const favoriteCitiesList = useSelector(state => state.favoriteCitiesList) 
    const [isInFavoriteList, updateFavoriteList] = useState(true)
    
   
    useEffect(() => {
        updateFavoriteList(Boolean(favoriteCitiesList.find(obj => {
                                        return obj['id'] === currentCityId
                                        }
        )))
        
    },[currentCityId, favoriteCitiesList])
    
    const addToFavoriteList = (e) => {
        dispatch({type: ADD_TO_FAVORITE_CITIES_LIST, 
                  payload:{ id:currentCityId, name: currentCityName}})
    }

    const deleteFromFavoriteList = (e) => {
        dispatch({type: DELETE_FROM_FAVORITE_CITIES_LIST, 
                 payload:{ id:currentCityId, name: currentCityName}})
    }


    return (
        <div>
            <div>Is current city in favorites?:  {JSON.stringify(isInFavoriteList)}</div>
            <button name='handleFavorites' 
                    onClick={isInFavoriteList? deleteFromFavoriteList : addToFavoriteList }>
                {isInFavoriteList? 'Delete from Favorites': 'Add to favorites'}
            </button>    
        </div>
    )
}

export default HandleFavoritesList