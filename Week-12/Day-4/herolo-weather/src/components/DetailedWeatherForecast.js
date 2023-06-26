import { useSelector } from 'react-redux';
import React, { useEffect, useState } from 'react';
import axios from 'axios';
import reducer from '../redux/reducer';


const DetailedWeatherForecast = () => {

    const currentCityId = useSelector(state => state.currentCity.id) 
    const currentCityName = useSelector(state => state.currentCity.name) 
    
    const[cityId, setCityId] = useState(currentCityId)
    const[forecast, setForecast] = useState({})

    useEffect(() => {
        setCityId(currentCityId)
    },[currentCityId])

    // const PROXY_PORT = process.env.REACT_APP_BACKEND_SERVER_PORT
    // const [isLoading, setIsLoading] = useState(false);
    // const [error, setError] = useState("");

    // const [forecast, setForecast] = useState({}) 
    
    // useEffect (()=>{
    //     console.log(currentCityId)
    //     const id = currentCityId.id
    //     setForecast(() => {
    //         return getForecast(id)
    //  })
    // },[currentCityId])

    // const getForecast = (cityId) => {
        
    //     const url = `http://localhost:${PROXY_PORT}/api` + 
    //                 `/forecasts/v1/daily/5day/` +
    //                 `${cityId}` 

    //     axios.get(url,
    //              {params:{details:'true', metric:'true', language: 'en-us'}})
    //             .then((response) => {
    //             setForecast(response.data);
    //             console.log(response.data)
    //             setIsLoading(false);
    //             setError("");
    //             }).catch(() => {
    //             setError("An error occured. Please try again.");
    //             setIsLoading(false)
    //             });
    //         }


     return (
        <div>
        <h1>{currentCityName}</h1>
        <h2>{currentCityId}</h2>
        </div>

        //  <div className="list">
        //         <h1>{String(error)}, {String(isLoading)}</h1>
        //         {error && <p>{error}</p>}
        //         {isLoading && <p className="loading">Loading...</p>}
        //         <div className="list">
        //             {forecast.DailyForecast.map((item, index) => (
        //                 <div className="list-item"
        //                     key={index}
                           
        //                 >
        //                     {item.Date}
        //                 </div>
        //             ))}
        //         </div>
        //     </div>

       
        
     ) 

}
    
     
export default DetailedWeatherForecast