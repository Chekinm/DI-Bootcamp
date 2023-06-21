import React, { useEffect, useState } from 'react';
import axios from 'axios';

const Home = () => {
  const [data, setData] = useState(null);
  

  const fetchData = () => {
    
    axios.get('http://localhost:5000/api/forecasts/v1/daily/5day/215854?&language=en-us&details=false&metric=true')
    .then(function (response) {
      
      setData(response)
    })
    .catch((error) => {
      
      setData(error)
    })
  
};

  useEffect(() => {
    
    fetchData();
  }, []);

  return (
    
    <div>
      {/* Display the fetched data */}
      {JSON.stringify(data)}
      <button onClick={fetchData}>Fetch</button>
      
    </div>
  );
};

export default Home;
