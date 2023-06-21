import SearchCity from "./SearchCity"
import HandleFavoritesList from "./HandleFavoritesList"

const Weather = () => {
    return  (
        <div>
        <SearchCity />
        <HandleFavoritesList />
        <DatailedWeatherForecast />
        </div>

    )
}

export default Weather