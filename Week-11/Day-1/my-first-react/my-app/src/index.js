import React from 'react';
import ReactDOM from 'react-dom/client';
import './index.css';
import App from './App';
import reportWebVitals from './reportWebVitals';


// const root = ReactDOM.createRoot(document.getElementById('root'));
// let myStr= 'My string'
// let myUrl = 'https://pibig.info/uploads/posts/2022-11/thumbs/1668750427_1-pibig-info-p-kotik-na-belom-fone-instagram-2.jpg'
// const element = (
//   <div>
//   <h1>My First Element</h1>
//   <img src={myUrl} width="400"></img>
//   </div>
// )

const root = ReactDOM.createRoot(document.getElementById('root'));
root.render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);

// If you want to start measuring performance in your app, pass a function
// to log results (for example: reportWebVitals(console.log))
// or send to an analytics endpoint. Learn more: https://bit.ly/CRA-vitals
reportWebVitals();
