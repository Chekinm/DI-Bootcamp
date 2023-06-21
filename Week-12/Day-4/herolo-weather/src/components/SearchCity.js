import {useSelector, useDispatch} from 'react-redux';
import {SET_CITY, DEFAULT_CITY}  from '../redux/reducer' 
import React, { useEffect, useState } from 'react';
import axios from 'axios';

const SearchCity = () => {
    
    const [searchList, setSearchList] = useState([])
    const [query, setQuery] = useState('')
    const [cityId, setCityId] = useState(DEFAULT_CITY)
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");
    const PROXY_PORT = process.env.REACT_APP_BACKEND_SERVER_PORT


    // connect  redux state 
    const dispatch = useDispatch()
    const currentCityId = useSelector(state => state.currentCity) 
    useEffect(() => {
        //monitor cityId change from another part of app
        setCityId(currentCityId)
    },[currentCityId])


    const handleInputChange = (e) => {
        const q = e.target.value
        setQuery(q)
        
        axios.get(`http://localhost:${PROXY_PORT}/api/locations/v1/cities/autocomplete`,
                    {params:{q:q, language: 'en-us'}})
                .then((response) => {
                setSearchList(response.data);
                setIsLoading(false);
                setError("");
                }).catch(() => {
                setError("An error occured. Please try again.");
                setIsLoading(false);
        });
    }

    const onItemSelection = (e) => {
        console.log(e.target)
        const id = e.target.id
        const city = e.target.innerText
        console.log(id, city)
        setQuery(city)
        setCityId(id)
        setSearchList([]);

    }


    const setCityGlobal = (e) => {
        e.preventDefault()    
        dispatch({type:SET_CITY, payload: cityId})
        return  
    } 

    return  (
        <div>
            <form className='searchForm' onSubmit={setCityGlobal}>
                <input name='query' 
                        onChange={handleInputChange} 
                        value={query}>
                </input>
                <button type='submit'>Get Weather</button>
            </form>
        
            <div className="list">
                {error && <p>{error}</p>}
                {isLoading && <p className="loading">Loading...</p>}
                <div className="list">
                    {searchList.map((item, index) => (
                        <div className="list-item"
                            key={index}
                            id={item.Key}
                            onClick={onItemSelection}
                        >
                            {item.LocalizedName}
                        </div>
                    ))}
                </div>
            </div>
        
        </div>
        )
}

export default SearchCity