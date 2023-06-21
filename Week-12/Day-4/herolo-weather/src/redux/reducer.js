import { addToLocalStorage, getFromLocalStorage } from "../utils/storage";

export const DEFAULT_CITY = '215854'; // Tel Avie code on accuweather

export const SET_CITY = 'SET_CITY';
export const ADD_TO_FAVORITE_CITIES_LIST = 'ADD_TO_FAVORITE_CITIES_LIST';
export const DELETE_FROM_FAVORITE_CITIES_LIST = 'DELETE_FROM_FAVORITE_CITIES_LIST';
export const LOCAL_STORAGE_UPDATE = 'LOCAL_STORAGE_UPDATE'
export const LOCAL_STORAGE_GET = 'LOCAL_STORAGE_GET' 
export const LOCAL_STORAGE_KEY = 'favoriteCitiesList'

const initState = {
  currentCity: DEFAULT_CITY, 
  favoriteCitiesList: getFromLocalStorage(LOCAL_STORAGE_KEY) || [DEFAULT_CITY,]
}

console.log('favorite list', initState.transactionList)

 const reducer= (state=initState, action={}) => {
  switch (action.type) {

    case SET_CITY:
      console.log('setting new city=>', action.payload);
      return {...state, currentCity:action.payload}

    case DELETE_FROM_FAVORITE_CITIES_LIST:
      console.log('updating favorite list=>', action.payload);
      addToLocalStorage(LOCAL_STORAGE_KEY, 
                  state.favoriteCitiesList.filter((item) => item !== action.payload))
      return {...state, favoriteCitiesList: state.favoriteCitiesList.filter((item) => item !== action.payload )}

    case ADD_TO_FAVORITE_CITIES_LIST:
      console.log('addint to favorites=>', action.payload);
      console.log([...state.favoriteCitiesList])
      addToLocalStorage(LOCAL_STORAGE_KEY, [...state.favoriteCitiesList, action.payload] )
      return {...state, favoriteCitiesList: [...state.favoriteCitiesList, action.payload]} 
                                                     
    default:
      return {...state}
  }
}

export default reducer