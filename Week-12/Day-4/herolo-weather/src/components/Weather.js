import SearchCity from "./SearchCity"
import HandleFavoritesList from "./HandleFavoritesList"
import DetailedWeatherForecast from "./DetailedWeatherForecast"
import FiveDayCard from "./FiveDayCard"


const Weather = () => {
    return  (
        <div>
        <SearchCity />
        <HandleFavoritesList />
        <FiveDayCard />
        </div>

    )
}

export default Weather