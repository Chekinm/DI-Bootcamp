import SearchCity from "./SearchCity"
import HandleFavoritesList from "./HandleFavoritesList"
import DetailedWeatherForecast from "./DetailedWeatherForecast"

const Weather = () => {
    return  (
        <div>
        <SearchCity />
        <HandleFavoritesList />
        <DetailedWeatherForecast />
        </div>

    )
}

export default Weather