import { useSelector, useDispatch } from 'react-redux';
import { incrementCounter,decrementCounter } from '../redux/actions'

const Counter = () => {
  const count = useSelector((state) => state.count);
  const dispatch = useDispatch()
  return (
    <>
      <button onClick={() => dispatch(incrementCounter())}> + </button>
      {count}
      <button onClick={() => dispatch(decrementCounter())}> - </button>
    </>
  )
}
export default Counter;

