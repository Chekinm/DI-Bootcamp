let form = document.getElementsByTagName("form")
//console.log(form)
let radius = form[0].radius.value
//console.log(radius)

function handleSubmit(event) {
    event.preventDefault()
    console.log(event)
    let form = event.target
    let radius = form.radius.value
    console.log(radius)
    let volume = 4 * Math.PI * Math.pow(radius,3) / 3   
    form.volume.value = volume
    form.submit


}   