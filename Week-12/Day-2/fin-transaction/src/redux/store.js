import {createStore, combineReducers} from 'redux';
import {reducerList, reducer_detail} from './reducers';

const reducer = combineReducers({
    reducerList,
    reducer_detail
})
    
const store = createStore(reducer);

export default store;
