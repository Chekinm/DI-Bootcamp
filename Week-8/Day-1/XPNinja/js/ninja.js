//ex1





person1 = {
    name:'Peter',
    mass: 188,
    height: 1.87,
    bmi: function() {
        return (this.mass / (this.height * this.height))
    }
}

person2 = {
    name:'John',
    mass: 68,
    height: 1.67,
    bmi: function() {
        return (this.mass / (this.height * this.height))
    }
}

person3 = {
    name:'Gerome',
    mass: 78,
    height: 1.82,
    bmi: function() {
        return (this.mass / (this.height * this.height))
    }
}

function ltBmi (pers1, pers2) {
    return (pers1.bmi() < pers2.bmi()) 
    //less bmi better bmi so 
}

arr = [person1, person2, person3]

bestbmi = person1
for (per of arr) {
    if (ltBmi(per, bestbmi)) bestbmi=per
}  
console.log (`Best bmi (${bestbmi.bmi()}) has ${bestbmi.name}`)


// ex2

//from xpgold
function sumArr(arr) {
    if (arr.length){
        sum = 0
        for (num of arr) {
            if (num.isNaN) return NaN
            else sum = sum + num 
        }
        return sum
    }
    else{
        return NaN
    }
}



person1 = {
    name:'Harry',
    grades : [45,10,44,33,88,17,99,100],
    averageGrades : function () {
        if (this.grades.length){
            return sumArr(this.grades)*1.0/this.grades.length
        }
        else return NaN
    }
}

person2 = {
    name:'Hermiona',
    grades : [88,76,99,88,88,87,96,98,57],
    averageGrades : function () {
        if (this.grades.length){
            return sumArr(this.grades)/this.grades.length
        }
        else return NaN
    }
    }

function isGood(person) {
    if (person.averageGrades() > 65) return `${person.name}, you are accepted`
    else return `${person.name}, you are not accpeted`
}  

console.log(person1.averageGrades())

console.log(person2.averageGrades())

console.log(isGood(person1))
console.log(isGood(person2))

