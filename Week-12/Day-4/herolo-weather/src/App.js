import './App.css'
import Home from './components/Home';
import Weather from './components/Weather';
import Favorites from './components/Favorites';
import { Routes, Route, Link } from 'react-router-dom';



function App() {
  return (
    <div className="App">
    {/* <Home />
    <Weather />
    <Favorites /> */}

    <nav>
      <Link to='/'>Home </Link>
      <Link to='/Weather/'>Weather </Link>
      <Link to='/Favorites/'>Favorites </Link>
    </nav>
    <Routes className='nav'>
      <Route className='navlink' path='/' element={<Home />} />
      <Route className='navlink' path='/Weather' element={<Weather />}/>
      <Route className='navlink' path='/Favorites/*' element={<Favorites />} />

    </Routes>

  </div>
  );
}

export default App;
