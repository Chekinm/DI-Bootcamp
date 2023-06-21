import { useSelector } from 'react-redux';
import React, { useEffect, useState } from 'react';
import axios from 'axios';


const DatailedWeatherForecast = () => {

    
    
    const currentCityId = useSelector(state => state.currentCity) 

    const PROXY_PORT = process.env.REACT_APP_BACKEND_SERVER_PORT
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");

    const [forecast, setForecast] = useState(() => {
        setForecast(currentCityId)
    })

    useEffect (()=>{
        setForecast(currentCityId)
    },[currentCityId])

    const getForecast = (cityId) => {
        
        const url = `http://localhost:${PROXY_PORT}`/api`` + 
                    `/forecasts/v1/daily/5day/` +
                    `${cityId}` 

        axios.get(url,
                 {params:{details:'true', metric:'true', language: 'en-us'}})
                .then((response) => {
                setForecast(response.data);
                console.log(response.data)
                setIsLoading(false);
                setError("");
                }).catch(() => {
                setError("An error occured. Please try again.");
                setIsLoading(false);
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

export default DatailedWeatherForecast