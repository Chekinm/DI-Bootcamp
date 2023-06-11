import React from 'react'
import UserFavoriteColors from './UserFavoriteColors'
import Exercise4 from './Exercise4';

const myelement = <h1>I love JSX</h1>

const user = {
  firstName: 'Bob',
  lastName: 'Dylan',
  favAnimals : ['Horse','Turtle','Elephant','Monkey']
};

function App() {
  return (
    //ex1
  <div>
  <h1>I do not use JSX</h1>

  {/* ex2  */}
  {myelement}

  {/* ex3 */}
  <UserFavoriteColors favAnimals={user.favAnimals} />

  {/* ex4 */}

  <Exercise4 props='ss'/>
  </div>
  );
}

export default App;