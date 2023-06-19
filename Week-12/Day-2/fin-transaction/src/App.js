import TransactionList from './components/TransactionList'
import TransactionDetails from './components/TransactionDetails'
import './App.css'
function App() {
  return (
    <div className='App-header'>
      <TransactionDetails/>
      <TransactionList/>
    </div>
  );
}

export default App;
