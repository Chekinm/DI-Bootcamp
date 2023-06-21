const axios = require('axios');

const getListFromAutocompleteResponce = async (query) => {
    
    // axios.get('http://localhost:3000/api/cities/autocomplete',
    //                 {params:{q:query, language: 'en-us'}})
    console.log('in function')
   
    await axios.get('http://localhost:5000/api/forecasts/v1/daily/5day/215854?&language=en-us&details=false&metric=true')

    .then(function(response){
      console.log(response)
      
    })
    .catch(function(error) {   
      console.log(error)
      
    })
};

export default getListFromAutocompleteResponce



