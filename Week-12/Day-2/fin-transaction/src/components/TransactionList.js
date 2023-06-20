import {useSelector, useDispatch} from 'react-redux';
import {DETAIL, DELETE} from '../redux/reducers'
// import {showDetails} from '../redux/actions'

const TransactionList = (props) => {

  const list = useSelector(state => state.reducerList.transactionList);
  console.log(list)
  
  const dispatch = useDispatch();
  if (list.length) {
    return (
      <div style={{display:'inline-block',width:'60%', verticalAlign: 'top'}}>
        <h1>Transaction list</h1>
        <table>
        <tbody>
        {
          list.map((item, indx) => {
            return(
              <tr key={indx}>
                <td> {item.accountNumber || '-'}</td>
                <td> {item.FSC || '-'} </td>
                <td> {item.accHolderName || '-'}</td>
                <td> {item.amount || '-'} </td>
                <td> <button onClick={() => dispatch({type:DETAIL, payload: item}) }>UPDATE</button></td>
                <td> <button onClick={() => dispatch({type:DELETE, payload: String(indx)}) }>DELETE</button></td>
              </tr>
            )
          })
        }
        </tbody>
        </table>
      </div>
    )
  } else {
  return (<div style={{display:'inline-block',width:'60%', verticalAlign: 'top'}}>
             <h1>Transaction list</h1>
           </div>
          )
  }
}

export default TransactionList
