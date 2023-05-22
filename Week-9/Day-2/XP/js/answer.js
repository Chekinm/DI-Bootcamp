// #1
function funcOne() {
    let a = 5;
    if(a > 1) {
        a = 3;
    }
    alert(`inside the funcOne function ${a}`);
}


//// we don't have a assigned as we don't call the function
//// so we will got an error that a is not defined


// #1.1 - run in the console:
funcOne()

////we will got an allert with value 3.
//// if we will try to access a, we still should get an error   

// #1.2 What will happen if the variable is declared 
// with const instead of let ?

// alert will get 5, other will remain the same.
//try to run, and see that no. We don't have 5 we will get an error
// that we are trying to change const.


//#2
let a = 0;
function funcTwo() {
    a = 5;
}

function funcThree() {
    alert(`inside the funcThree function ${a}`);
}





// #2.1 - run in the console:
funcThree()
// alert with a = 0

funcTwo()
// nothing returns
funcThree()
// alert with a = 5

// #2.2 What will happen if the variable is declared 
// with const instead of let ?

// after funcTwo call there will be an error, that we are 
// trying to change const  

//#3
function funcFour() {
    window.a = "hello";
}


function funcFive() {
    alert(`inside the funcFive function ${a}`);
}

// #3.1 - run in the console:
funcFour()

funcFive()
// we will get doesn't define error, as we specify a 
// parameter of object window. (if you don't mean that we have a 
// defined in previouse exersice, in theis case it will be 0 or 5, 
// depending on if we change declaration to const or not)
//
// and we can actually broke something if we assing things
// to something we don't know, especiall to a high level staff:) 

// run it.......interesting.  Will know.

//#4
let a = 1;
function funcSix() {
    let a = "test";
    alert(`inside the funcSix function ${a}`);
}


// #4.1 - run in the console:
funcSix()

// here we will got test, as we redeclared 
// a inside the function block (scope)

// #4.2 What will happen if the variable is declared 
// with const instead of let ?

// in this case it take no effect, as in scope of funcSix, we 
// redeclared a.


//#5
let a = 2;
if (true) {
    let a = 5;
    alert(`in the if block ${a}`);
}
alert(`outside of the if block ${a}`);

// #5.1 - run the code in the console

// it get 5 then 2 let declaration is valid onlhy inside 
// block


// #5.2 What will happen if the variable is declared 
// with const instead of let ?

// the result willbe the same.
// as block is another scope, we can redeclare variable there.\