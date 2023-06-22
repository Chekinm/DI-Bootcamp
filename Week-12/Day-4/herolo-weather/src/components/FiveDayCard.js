import {useSelector, useDispatch} from 'react-redux';
import React, { useEffect, useState } from 'react';
import axios from 'axios';


const FiveDayCard = (props) => {
    
    const currentCityId = useSelector(state => state.currentCity.id) 
    const currentCityName = useSelector(state => state.currentCity.name) 
    
    const[cityId, setCityId] = useState(currentCityId)
 

    useEffect(() => {
        setCityId(currentCityId)
    },[currentCityId])
    
    const [forecast, setForecast] = useState('')
    
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");

    //const PROXY_PORT = process.env.REACT_APP_BACKEND_SERVER_PORT

    

    useEffect(()=>{
     
        let url= 'http://localhost:5000/api/forecasts/v1/daily/5day/215854?en-us&details=false&metric=true'
        axios.get(url)
            
            
            // `http://localhost:${PROXY_PORT}/currentconditions/v1/${props.city.id}`,
            //         {language: 'en-us', details:'true'})
                .then((response) => {
                setForecast(JSON.stringify(response.data.DailyForecasts));
                setIsLoading(false);
                setError("");
                }).catch(() => {
                setError("An error occured. Please try again.");
                setIsLoading(false);
                })
            },[])



    return  (
        <div>
            
            <div className="list">
                {error && <p>{error}</p>}
                {isLoading && <p className="loading">Loading...</p>}
                <div className="list">
                    {currentCityName} 
                </div>
                <div>
                    {forecast}
                </div> 
            </div>
        </div>
        )
}

export default FiveDayCard
