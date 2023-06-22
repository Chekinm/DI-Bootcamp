import {useSelector, useDispatch} from 'react-redux';
import React, { useEffect, useState } from 'react';
import axios from 'axios';


const OneDayCityCard = (props) => {
    
    
    
    const [temperature, setTemperature] = useState('')
    const [sky, setSky] = useState('')
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");

    //const PROXY_PORT = process.env.REACT_APP_BACKEND_SERVER_PORT

    

    useEffect(()=>{
     
        let url= 'http://localhost:5000/api/cities/currentconditions?q=tel&language=en-us'
        axios.get(url)
            `http://localhost:${PROXY_PORT}/currentconditions/v1/${props.city.id}`,
                    {language: 'en-us', details:'true'})
                .then((response) => {
                setTemperature(response.data[0].Temperature.Metric.Value);
                setSky(response.data[0].WeatherText)
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
                    {props.city.name} - {temperature} - {sky}
                </div>
            </div>
        </div>
        )
}

export default OneDayCityCard
