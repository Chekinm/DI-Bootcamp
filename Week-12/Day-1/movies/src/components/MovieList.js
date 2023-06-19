import {useSelector, useDispatch} from 'react-redux';
import {DETAIL} from '../redux/reducers'
// import {showDetails} from '../redux/actions'

const MovieList = (props) => {

  const list = useSelector(state => state.reducer_list.movies_list);

  const dispatch = useDispatch();

  return (
    <div style={{display:'inline-block',width:'50%'}}>
      <h1>Movie List</h1>
      {
        list.map((item,indx) => {
          return(
            <div key={indx}>
              {item.title}
              <button onClick={()=> dispatch({type:DETAIL, payload:item}) }>Details</button>
            </div>
          )
        })
      }
    </div>
  )
}
export default MovieList
// const mapStateToProps = state => {
//   return {
//     list: state.movies_list
//   }
// }

// const mapDispatchToProps = dispatch => {
//   return {
//     show: (item) => dispatch(showDetails(item))
//   }
// }
// export default connect(null, mapDispatchToProps)(MovieList)
