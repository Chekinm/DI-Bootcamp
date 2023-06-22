import { addToLocalStorage, getFromLocalStorage } from "../utils/storage";

export const DEFAULT_CITY_ID = '215854'; // Tel Avie code on accuweather
export const DEFAULT_CITY_NAME = 'Tel Aviv';

export const SET_CITY = 'SET_CITY';
export const ADD_TO_FAVORITE_CITIES_LIST = 'ADD_TO_FAVORITE_CITIES_LIST';
export const DELETE_FROM_FAVORITE_CITIES_LIST = 'DELETE_FROM_FAVORITE_CITIES_LIST';
export const LOCAL_STORAGE_UPDATE = 'LOCAL_STORAGE_UPDATE'
export const LOCAL_STORAGE_GET = 'LOCAL_STORAGE_GET' 
export const LOCAL_STORAGE_KEY = 'favoriteCitiesList'

const initState = {
  currentCity: {id: DEFAULT_CITY_ID, name: DEFAULT_CITY_NAME}, 
  favoriteCitiesList: getFromLocalStorage(LOCAL_STORAGE_KEY)
}

console.log('favorite list', initState.favoriteCitiesList)

 const reducer= (state=initState, action={}) => {
  switch (action.type) {

    case SET_CITY:
      console.log('setting new city=>', action.payload);
      return {...state, currentCity:action.payload}

    case DELETE_FROM_FAVORITE_CITIES_LIST:
      console.log('updating favorite list=>', action.payload);
      addToLocalStorage(LOCAL_STORAGE_KEY, 
                  state.favoriteCitiesList.filter((item) => item.id !== action.payload.id))
      return {...state, favoriteCitiesList: state.favoriteCitiesList.filter((item) => item.id !== action.payload.id )}

    case ADD_TO_FAVORITE_CITIES_LIST:
      console.log('add int to favorites=>', action.payload);
      console.log([...state.favoriteCitiesList])
      addToLocalStorage(LOCAL_STORAGE_KEY, [...state.favoriteCitiesList, action.payload] )
      return {...state, favoriteCitiesList: [...state.favoriteCitiesList, action.payload]} 
                                                     
    default:
      return {...state}
  }
}

export default reducer