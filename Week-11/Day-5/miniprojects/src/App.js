import './App.css';
import RandomQuoteApp from './RandomQuote/RandomQuoteApp'
import { useState } from 'react'

function App() {

  const [bgColor, setBgColor] = useState ('rgb(255, 5, 100)')

  return (
      <div style={{
        backgroundColor: bgColor,
        width: '100vw',
        height: '100vh',
        padding: 0,
        margin: 0,
      }}>
        <RandomQuoteApp setColor = {setBgColor} />
      </div>
  );
}

export default App;
