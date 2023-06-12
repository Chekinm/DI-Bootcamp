import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import MyAppFunction from './MyAppFunction';
import MyAppClass from './MyAppClass'
//import reportWebVitals from './reportWebVitals';

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <div>
  <React.StrictMode>
    <h1>hello</h1>
    <MyAppFunction MyAppFunctionProps={'ssssssssss'}/>
    <MyAppClass MyAppClassProp={'Hello'+'ReactNOnja'}/>
    
  </React.StrictMode>
  </div>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
//reportWebVitals();
