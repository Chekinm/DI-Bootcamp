import {createStore, applyMiddleware} from 'redux';
import reducer from './reducer';


const myMiddleWare = (store) => (next) => (action) => {
    console.log('Im from idlware delete me if you dont need me');
    next(action)
}
    
const store = createStore(reducer, applyMiddleware(myMiddleWare));

export default store;
