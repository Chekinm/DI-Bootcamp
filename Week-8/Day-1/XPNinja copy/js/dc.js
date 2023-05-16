person1 = {
    name:'Peter',
    mass: 88,
    hight: 187,
    bmi: function (this) {
        return (this.mass / (this.height * this.height))
    }
}

console.log(person1.bmi())