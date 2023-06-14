import './App.css';
import { useState } from 'react'
import React from 'react'

const App = () => {
  const [name, setName] = useState('John')
  
  const handleSubmit = (e) => {
    e.preventDefault();
    const form = e.target
    const formData = new FormData(form)
    const fromJson = Object.fromEntries(formData.entries())
    console.log(fromJson)
  }

  return (
    <div>
      <form onSubmit={handleSubmit} method='POST'>
        <label>
          Username: <input type="text" name="name" />
        </label>
        <label>
          password: <input type="text" name="password" />
        </label>
        <input type='submit' value='send'/>

      </form>
     {name}
    </div>
  );
}

export default App;
