import {useSelector, useDispatch} from 'react-redux';
import {SET_CITY, ADD_TO_FAVORITE_CITIES_LIST}  from '../redux/reducer' 
import React, { useEffect, useState } from 'react';
import getListFromAutocompleteResponce from '../utils/utils';
import axios from 'axios';

const Weather = () => {

    const [searchList, setSearchList] = useState([])
    const [query, setQuery] = useState('')
    const [isLoading, setIsLoading] = useState(false);
    const [error, setError] = useState("");

    // connect dispath and details to redux state form store
    const dispatch = useDispatch()
    const currentCity = useSelector(state => state.currentCity) //.reducer.currentCity)
    const favoriteCitiesList = useSelector(state => state.favoriteCitiesList)
    

    const handleInputChange = (e) => {
        const q = e.target.value
        setQuery(q)
        // setSearchList((q) => {
        //     return getListFromAutocompleteResponce(query) //write me
        // })
        
        axios.get('http://localhost:5000/api/locations/v1/cities/autocomplete',
                    {params:{q:q, language: 'en-us'}})
                .then((response) => {
                console.log(response.data[0].Key)
                setSearchList(response.data);
                setIsLoading(false);
                setError("");
                }).catch(() => {
                setError("An error occured. Please try again.");
                setIsLoading(false);
        });
        console.log('isloading:', isLoading)
        console.log('error:', error)
        console.log('searchList:',searchList)
    }

    const onItemSelection = (e) => {
        console.log(e.target)
        const key = e.target.key
        const city = e.target.value
        console.log(key, city)

    }


    const getWeatherFromApi = (e) => {
        e.preventDefault()
        const query = e.target[0].value
        console.log(query)
        return  
    } 




    return  (
        <div>
            <form className='searchForm' onSubmit={getWeatherFromApi}>
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

export default Weather