import { DEFAULT_CITY_ID, DEFAULT_CITY_NAME } from "../redux/reducer"

export const addToLocalStorage = (key, value) => {
    window.localStorage.setItem(key, JSON.stringify(value))
}

export const getFromLocalStorage = (key) => {
    return JSON.parse(window.localStorage.getItem(key)) || [{id:DEFAULT_CITY_ID, name: DEFAULT_CITY_NAME}]
}