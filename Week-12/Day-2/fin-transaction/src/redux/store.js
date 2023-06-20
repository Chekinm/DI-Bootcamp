import {createStore, combineReducers, applyMiddleware} from 'redux';
import {reducerList, reducer_detail} from './reducers';

const reducer = combineReducers({
    reducerList,
    reducer_detail
})

const myMiddleWare = (store) => (next) => (action) => {
    console.log('state');
    next(action)
}
    
const store = createStore(reducer, applyMiddleware(myMiddleWare));

export default store;
