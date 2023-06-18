const initState = {
  
  count: 100,
}

export const reducer = (state = initState, action={}) => {
  switch (action.type) {
    case 'INCREMENT_COUNTER':
      console.log('INCREMENT_COUNTER');
      return {...state, count: state.count + 1}
    case 'DECREMENT_COUNTER':
      console.log('DECREMENT_COUNTER');
      return {...state, count: state.count - 1}
    default:
      return {...state}
  }
}
