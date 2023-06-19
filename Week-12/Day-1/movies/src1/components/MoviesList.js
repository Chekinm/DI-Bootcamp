import React from 'react'
import { useSelector} from 'react-redux';


// function MoviesList() {
//   return (
//     <div>Hello</div>
//   )
// }

// export default MoviesList


function MoviesList(props) {
  const list = useSelector (state => state.moviesList)
  return (
    <div style={{display:'inline-block', width:'50%'}}>
      <h1>MovieList</h1>
      {
       list.map((item,indx) => {
        return(
          <div key={indx}>
            {item.title}
            <button>Details</button>
          </div>
        )
       }) 
      }
    </div>
  )
}

export default MoviesList
