import React from'react'
import Counter from './components/Counter'
import './App.css'

function App() {
  return (
    <div className="App">
      <header className="App-header">
        <Counter/>
      </header>
    </div>
    );
}

export default App
























// import {useState} from 'react'
// import Test from './components/Test'
//
// import './App.css';
//
// function App() {
//   const [title, setTitle] = useState('My title')
//   return (
//     <div className="App">
//       <header className="App-header">
//         <Test title={title} setTitle={setTitle}/>
//       </header>
//     </div>
//   );
// }
//
// export default App;
