import './App.css';
import AppForm from './components/AppForm';
import Home from './components/Home';
import About from './components/About';
import Contact from './components/Contact';
import { Routes, Route, Link } from 'react-router-dom';


function App() {
  return (
    <div className="App">
      <AppForm />
      {/* <Home />
      <About />
      <Contact /> */}

      {/* <nav>
        <Link to='/'>Home</Link>
        <Link to='/about'>About</Link>
        <Link to='/Contact/'>Contact</Link>
      </nav>
      <Routes>
        <Route path='/' element={<Home />} />
        <Route path='/about' element={<About />}/>
        <Route path='/contact/:aaa' element={<Contact />} />
      </Routes> */}

    </div>
  );
}

export default App;
