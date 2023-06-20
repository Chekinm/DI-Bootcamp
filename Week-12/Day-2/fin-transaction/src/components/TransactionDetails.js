
import {useSelector, useDispatch} from 'react-redux';
import {UPDATE, CREATE} from '../redux/reducers'
import { useEffect, useState } from 'react'


const TransactionDetails = () => {
  //firstly we need to made local state of the component
  //we need it be able to set values to form input
  // from  redux state 
  
  const [button,setButton] = useState('Create')
  const [localDetails, setLocalDetails] = useState({id:'',
                                                    accountNumber:'',
                                                    FSC:'',
                                                    accHolderName:'',
                                                    amount:''})


  // connect dispath and details to redux state form store
  const dispatch = useDispatch()
  const details = useSelector(state => state.reducerList.transactionDetails)
  const currentNumber = useSelector(state => state.reducerList.currentNumber)

  // this will handle incoming changes in redux state and 
  // update local state correspondingly
  useEffect(() => {
    if (!details.length) {
      
        const isNew = details.id === undefined
   
        setLocalDetails(details)
        setButton(isNew? 'Create': 'Update')
    }
    
  }, [details])
  
  // this function transfer local state to redux state on click
  const handelClick = (e) => {
    e.preventDefault()
    //check if we are editing or creating
    const isNew = details.id === undefined

    dispatch({type:isNew? CREATE: UPDATE,
              payload: {
                  id: isNew? currentNumber + 1: details.id,  
                  accountNumber: e.target[0].value, 
                  FSC: e.target[1].value, 
                  accHolderName: e.target[2].value,
                  amount:e.target[3].value
            },
            //update counter for next transaction
            currentNumber: currentNumber + 1,
            // clear current item
            currentItem: {
                        accountNumber:'',
                        FSC:'',
                        accHolderName:'',
                        amount:''}
          })
        
        //clear form input
        setLocalDetails({
                        accountNumber:'',
                        FSC:'',
                        accHolderName:'',
                        amount:''})
        }


  // this is workaround to be able to handle both manual input and 
  // input from redux state if we want to update some transaction
  // and substitutes values frin redux state variable

  const handelInputChange = (e) => {
      const isNew = details.id === undefined
      //just to make user experience , tell him what is he doing
      setButton(isNew? 'Create': 'Update')
      setLocalDetails({...localDetails, [e.target.name]:e.target.value})
  }

  return (
    <div style={{display:'inline-block',width:'30%'}}>
    <form onSubmit={handelClick} autoComplete="off"><h1>Transaction details</h1>
      <table>
        <tbody>
        
        <tr>
          <td>Account number:</td>
          <td><input name='accountNumber'
                    type='text' 
                    //  placeholder={localDetails.accountNumber}
                     value={localDetails.accountNumber}
                     onChange={handelInputChange}>
          </input></td>
        </tr>
        
        <tr>
          <td>FSC</td>
          <td><input name='FSC'
                      type='text' 
                      // placeholder={localDetails.FSC}
                      value={localDetails.FSC}
                      onChange={handelInputChange}>
                      </input></td>
        </tr>

        <tr>
          <td>Account holder name: </td>
          <td> <input name='accHolderName'
                      type='text' 
                      // placeholder={localDetails.accHolderName}
                      value={localDetails.accHolderName}
                      onChange={handelInputChange}>
                    </input></td>
        </tr>

        <tr>
          <td>Amount:</td> 
          <td><input  name='amount'
                      type='text' 
                      // placeholder={localDetails.amount}
                      value={localDetails.amount}
                      onChange={handelInputChange}>
              </input></td>
        </tr>
        
        </tbody>
        </table>
        <button type='submit'>{button}</button>
    </form>
    </div>
  )
}
export default TransactionDetails
