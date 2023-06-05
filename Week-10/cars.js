const car = (model, year, color) => {
    let carObj = {
        'model' : model,
        'year' : year,
        'color' : color
    }
    return carObj
}

module.exports = {
    car
}