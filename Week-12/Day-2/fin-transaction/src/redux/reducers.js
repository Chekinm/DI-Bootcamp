export const DETAIL = 'DETAIL';
export const UPDATE = 'UPDATE';
export const CREATE = 'CREATE';
export const DELETE = 'DELETE';

const initState = {
  currentNumber: 1,
  transactionList: [],
  transactionDetails: {}
}

export const reducer_detail = (state=initState, action={}) => {
  
      return {...state}
  }


export const reducerList = (state=initState, action={}) => {
  switch (action.type) {

    case DETAIL:
      console.log('item=>', action.payload);
      return {...state, transactionDetails:action.payload}

    case UPDATE:
      console.log('updating=>', action.payload, action.currentItem);
      return {...state, transactionList: state.transactionList.map((item) => {
                                  return item.id === action.payload.id ?  action.payload : item
                                   }),
                        transactionDetails:action.currentItem
        }

    case CREATE:
      console.log('creating=>', action.payload);
      return {...state, transactionList: [...state.transactionList, action.payload], currentNumber: action.currentNumber} 
    
    case DELETE:
      console.log('delete=>', action.payload);
      return {...state, transactionList: state.transactionList.filter((item, ind) => ind !== Number(action.payload))} 
     
 
    default:
      return {...state}
  }
}
