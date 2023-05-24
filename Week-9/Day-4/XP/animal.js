class Animal {
    constructor (name, type, color) {
        this.name = name
        this.type = type
        this.color = color
    }
}

class Mamal extends Animal {
    constructor (name, type, color, sound) {
        super(name, type, color)
        this.sound = sound
    }
    
    present() {
        return `${this.name} is a ${this.color} ${this.type} and it says ${this.sound}`
    }

}

let farmerCow = new Mamal('Emma','cow','black','muuuuuuuu')
console.log(farmerCow.present())