const express = require('express');
require('dotenv').config();
const axios = require('axios');

const autocomplete = require('./datafiles/autoCompleteResponse.json')
const fiveDay = require('./datafiles/fivedayTelAvivDetailsFalse.json')
const oneDay = require('./datafiles/telavivCurrent.json')

const app = express();
const PORT = process.env.REACT_APP_BACKEND_SERVER_PORT;

const cors = require('cors')
app.use(cors())


const API_ACCUWEATHER = 'http://dataservice.accuweather.com'; // Replace with the URL of the external API



const API_KEY = process.env.ACCUWEATHER_APP_API_KEY;
                            

//use files insted of web due to tocken limits
app.get('/api/*', async (req, res) => {
  
  const {path} = req;
  
  
  if (path.includes('5day')) {
      
      res.json(fiveDay)
      
  } else if (path.includes('autocomplete')) {

    res.json(autocomplete)

  } else if (path.includes('currentconditions')) {

    res.json(oneDay)
    
  }  else {
    
    console.log('Worng request')
    res.json('Worng request')
  }  
})



  



// Proxy route
// Uncomment to use web


// app.get('/api/*', async (req, res) => {
  
//   const { query, path } = req;
//   const apiUrl = `${API_ACCUWEATHER}${path.replace('api/', '')}`;
//   console.log(apiUrl)
//   //work for now. need to add react boundary to control error, how?
//   axios.get(apiUrl, {
//       params: { apikey: API_KEY, ...query }
//     })
//   .then(function (response) {
//     res.json(response.data)
//   })
//   .catch((error) => {
//     res.json('error')
//   })
// })


// Start the server
app.listen(PORT, () => {
  console.log(`Server listening on port ${PORT}`);
});
