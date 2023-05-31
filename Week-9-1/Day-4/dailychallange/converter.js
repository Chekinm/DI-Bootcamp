async function requestCurrencyApi(endpoint) {

    // function to access api return data dapanding on endpoint 

    let currListJson = await fetch(endpoint)
    return currListJson.json()
} 


async function fillDropDownLists (defaultTo, defaultFrom) {
    //on refresh or on open we need to nest dropdown with avialabel currency
    // probably  it is not a best idea to use API for that but still

    let currListJson = await requestCurrencyApi("https://v6.exchangerate-api.com/v6/94ba9146166334bcfc89aad5/codes")
    //try get list fro API
    
    if (currListJson.result === "success") {
    // if sit eis responding start to biuld out dropdown lists

        dropDownToCurrency = document.getElementById("tocurrency")
        dropDownFromCurrency = document.getElementById("fromcurrency")

        for (curr of currListJson.supported_codes) {
            //iterato over currencies and add the to option to dropw down list
            //select USD and ILS  as default
            //

            let currencyOptonTo = document.createElement('option')
            currencyOptonTo.value = `${curr[0]}`
            if (curr[0]===defaultTo) currencyOptonTo.selected = "selected"
            currencyOptonTo.textContent = `${curr[1]}`

            let currencyOptonFrom  = document.createElement('option')
            currencyOptonFrom.value = `${curr[0]}`
            if (curr[0]===defaultFrom) currencyOptonFrom.selected = "selected"
            currencyOptonFrom.textContent = `${curr[1]}`

            dropDownToCurrency.appendChild(currencyOptonTo)
            dropDownFromCurrency.appendChild(currencyOptonFrom)

        }            
    } else {
        alert ("We expirenced a problem on remote site")
    }


}

fillDropDownLists("USD","ILS")

async function convertCurrency() {
   
    let target = document.getElementById("currency-form") 
    
    let fromCurrency = target[0].value 
    let toCurrency = target[1].value 
    let amount = target[2].value 
    
    let endpoint = `https://v6.exchangerate-api.com/v6/94ba9146166334bcfc89aad5/latest/${fromCurrency}` 

    let allRate = await requestCurrencyApi(endpoint)
    let rate = allRate.conversion_rates[toCurrency]
    
    let result = document.getElementById("result")
    result.value = (rate*amount).toFixed(5) 
    // `${} ${toCurrency}`

}


function switchCurrency () {
    dropDownToCurrency = document.getElementById("tocurrency")
    dropDownFromCurrency = document.getElementById("fromcurrency")
    
    tmpCurr = dropDownFromCurrency.value
    dropDownFromCurrency.value = dropDownToCurrency.value
    dropDownToCurrency.value = tmpCurr
    setToLabel()
    setFromLabel()
    convertCurrency()
}


function setToLabel() {
    let toCurr = document.getElementById("tocurrency").value
    let lable = document.getElementById("to-curr-label")
    lable.innerText = toCurr
    convertCurrency()
    

}

function setFromLabel() {
    let fromCurr = document.getElementById("fromcurrency").value
    let lable = document.getElementById("from-curr-label")
    lable.innerText = fromCurr
    convertCurrency()

    



    
}