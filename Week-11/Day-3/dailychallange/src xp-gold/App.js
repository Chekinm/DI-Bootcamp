
import './App.css';
import ErrorBoundary from './ErrorBoundary';
import CrashButton from './CrashButton';
 
function App() {

  return (
    <div className="App">
      <header className="App-header">
        <ErrorBoundary>
          <CrashButton />
        </ErrorBoundary>
      </header>
    </div>
  );
}

export default App;
