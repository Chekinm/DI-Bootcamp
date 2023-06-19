
import {useSelector, useDispatch} from 'react-redux';

import {UPDATE, CREATE} from '../redux/reducers'


const TransactionDetails = (props) => {

  const dispatch = useDispatch()

  const details = useSelector(state => state.reducerList.transactionDetails)
  const currentNumber = useSelector(state => state.reducerList.currentNumber)
  console.log('idlist')
  const handelClick = (e) => {
    e.preventDefault()
    const isNew = details.id === undefined
    dispatch({type:isNew? CREATE: UPDATE,
              payload: {
                  id: isNew? currentNumber + 1: details.id,  
                  accountNumber: e.target[0].value, 
                  FSC: e.target[1].value, 
                  accHolderName: e.target[2].value,
                  amount:e.target[3].value
            },
            currentNumber: currentNumber + 1
          })
        }
  
  return (
    <div style={{display:'inline-block',width:'30%'}}>
    <form onSubmit={handelClick}><h1>Transaction details</h1>
      
        <table>
        
        <tr>
          <td>Account number:</td>
          <td><input type='text' placeholder={details.accountNumber}></input></td>
        </tr>
        
        <tr>
          <td>FSC</td>
          <td><input type='text' placeholder={details.FSC}></input></td>
        </tr>

        <tr>
          <td>Account holder name: </td>
          <td> <input type='text' placeholder={details.accHolderName}></input></td>
        </tr>

        <tr>
          <td>Amount:</td> 
          <td><input type='text' placeholder={details.amount}></input></td>
        </tr>
        
        </table>
        <button type='submit'>Update</button>
    </form>
    </div>
  )
}
export default TransactionDetails
