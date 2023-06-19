import {createStore, combineReducers} from 'redux';
import {reducer_list, reducer_detail} from './reducers';

const reducer = combineReducers({
    reducer_list,
    reducer_detail
})
    


const store = createStore(reducer);

export default store;
