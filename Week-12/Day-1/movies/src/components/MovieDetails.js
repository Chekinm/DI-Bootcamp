
import {useSelector} from 'react-redux';

const MovieDetails = (props) => {
  const details = useSelector(state => state.reducer_list.movie_detail)

  return (
    <div style={{display:'inline-block',width:'50%'}}>
      <h1>Movie Details</h1>
      <h2>Title: {details.title}</h2>
      <h2>Release Date: {details.releaseDate}</h2>
      <h2>Rating: {details.rating}</h2>
    </div>
  )
}
export default MovieDetails
