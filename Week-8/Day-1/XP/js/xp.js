// ex1

const people = ["Greg", "Mary", "Devon", "James"];

// Part I - Review About Arrays
// Write code to remove “Greg” from the people array.
ind = people.indexOf("Greg")
people.splice(ind, ind+1)
console.log(people)

// Write code to replace “James” to “Jason”.

ind = people.indexOf("James")
people[ind] = "Jason"
console.log(people)

// Write code to add your name to the end of the people array.

people.push('Mike')
console.log(people)

// Write code that console.logs Mary’s index. take a look at the indexOf method on Google.
ind = people.indexOf("Mary")
console.log(ind)

// Write code to make a copy of the people array using the slice method.
// The copy should NOT include “Mary” or your name.
// Hint: remember that now the people array should look like this const people = ["Mary", "Devon", "Jason", "Yourname"];
// Hint: Check out the documentation for the slice method

new_people = people.slice(1,-1)
console.log(new_people)


// Write code that gives the index of “Foo”. Why does it return -1 ?
ind = people.indexOf("foo")
console.log(ind)
//becouse it is a standart answer of indexOf function, when it cannot find the element


// Create a variable called last which value is the last element of the array.
// Hint: What is the relationship between the index of the last element in the array and the length of the array?

last = people[people.length-1]
console.log(last)
console.log(people)


// Part II - Loops
// Using a loop, iterate through the people array and console.log each person.
function myIterFunction(item, index) {
    console.log(item, index)
}
people.forEach(myIterFunction);


// Using a loop, iterate through the people array and exit the loop after you console.log “Jason” .
// Hint: take a look at the break statement in the lesson.
var i = 0
while(true){
    console.log(people[i])
    if (people[i]=="Jason") {
        break
    }
    i++
}   

var i = 0
do {
    console.log(people[i] + '  do loop')
    i++
} while (people[i-1]!="Jason")

//console.log(i)

// 🌟 Exercise 2 : Your Favorite Colors
// Instructions
// Create an array called colors where the value is a list of your five favorite colors.
// Loop through the array and as you loop console.log a string like so: “My #1 choice is blue”, “My #2 choice is red” ect… .
// Bonus: Change it to console.log “My 1st choice”, “My 2nd choice”, “My 3rd choice”, picking the correct suffix for each number.
// Hint : create an array of suffixes to do the Bonus

function numSuffix(num) {
    if (num % 10 == 1) return 'st';
    else if (num % 10 == 2) return 'nd';
    else if (num % 10 == 3) return 'rd';
    else return 'th';
}

let colours = ['green','blue','orange','yellow','pink']
colours[121] = 'red'
colours[243] = 'brown'


function myColorIterFunction(item, index) {
    console.log(`My ${index}${numSuffix(index)} favorite number is ${item}!`)
}
colours.forEach(myColorIterFunction);



// 🌟 Exercise 3 : Repeat The Question
// Instructions
// Prompt the user for a number.
// Hint : Check the data type you receive from the prompt (ie. Use the typeof method)

// While the number is smaller than 10 continue asking the user for a new number.
// Tip : Which while loop is more relevant for this situation?


// 🌟 Exercise 4 : Building Management
// Instructions:
// const building = {
//     numberOfFloors: 4,
//     numberOfAptByFloor: {
//         firstFloor: 3,
//         secondFloor: 4,
//         thirdFloor: 9,
//         fourthFloor: 2,
//     },
//     nameOfTenants: ["Sarah", "Dan", "David"],
//     numberOfRoomsAndRent:  {
//         sarah: [3, 990],
//         dan:  [4, 1000],
//         david: [1, 500],
//     },
// }


// Review About Objects
// Copy and paste the above object to your Javascript file.

// Console.log the number of floors in the building.

// Console.log how many apartments are on the floors 1 and 3.

// Console.log the name of the second tenant and the number of rooms he has in his apartment.

// Check if the sum of Sarah’s and David’s rent is bigger than Dan’s rent. If it is, than increase Dan’s rent to 1200.


// 🌟 Exercise 5 : Family
// Instructions
// Create an object called family with a few key value pairs.
// Using a for in loop, console.log the keys of the object.
// Using a for in loop, console.log the values of the object.


// Exercise 6 : Rudolf
// Instructions
// const details = {
//   my: 'name',
//   is: 'Rudolf',
//   the: 'raindeer'
// }
// Given the object above and using a for loop, console.log “my name is Rudolf the raindeer”


// Exercise 7 : Secret Group
// Instructions
// const names = ["Jack", "Philip", "Sarah", "Amanda", "Bernard", "Kyle"];
// A group of friends have decided to start a secret society. The society’s name will be the first letter of each of their names sorted in alphabetical order.
// Hint: a string is an array of letters
// Console.log the name of their secret society. The output should be “ABJKPS”