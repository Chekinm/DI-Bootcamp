function submitHandler(event) {
    //this is to double check, like if you copy pase something from 
    // outside and submit
    event.preventDefault();
    let form = event.target;
    regex = /^[a-zA-Z]+$/ 
    if (regex.test(form.text1.value)) {
        console.log("Input is valid")
        form.submit
    } else {
        console.log("Input is invalid. ")
        alert("Please use only letters.")
    }
}

function keyPressHandler (event) {
    // this funtion prevent user from entering any chracter 
    // rather then alpha
    event.preventDefault()
    let input = event.target
    regex = /[a-zA-Z]/
    if (regex.test(event.key)) {
        input.value += event.key
    }
}