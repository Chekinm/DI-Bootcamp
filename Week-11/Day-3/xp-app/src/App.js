import './App.css';
import React from 'react'
import ErrorBoundary from './components/ErrorBoundary';
import BuggyCounter from './components/BuggyCounter';
import Color from './components/Color';
import ChildShow from './components/ChildShow';


const App = () => {
  return (
    <div>
      <h2>Click on the numbers to increase the counters.
      The counter is programmed to throw error when it reaches 5. This simulates a JavaScript error in a component.
      </h2>
      <hr/>
      <ErrorBoundary>
           <BuggyCounter/>
           <BuggyCounter/>
      </ErrorBoundary>
      <hr/>
      <ErrorBoundary>
           <BuggyCounter/>
      </ErrorBoundary>
      <ErrorBoundary>
           <BuggyCounter/>
      </ErrorBoundary>
      <hr/>
      <BuggyCounter/>
      <hr/>
      <h2>Part 2. Color</h2>
      <Color />
      <hr/>
      <h2>Exercise 3</h2>
      <ChildShow  />

    </div>    
  );
}

export default App;

