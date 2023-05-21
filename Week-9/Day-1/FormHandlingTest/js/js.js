function handleSubmit(e) {

    e.preventDefault();
    let form = e.target
    let userName = form[0].value
    let pwd1 = form[1].value
    let pwd2 = form[2].value
    regex = /^[A-Za-z0-9]+$/
    if (pwd1.length>7 && regex.test(pwd1)) {
        if (pwd1 === pwd2) {
        alert('ok')
        form.submit
        } else { alert("Password doesn't match!")}    
    } else {      
        alert ('password is bad') 
    }
}