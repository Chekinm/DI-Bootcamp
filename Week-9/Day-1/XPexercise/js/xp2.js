// 1 
console.log("------------------ex2 part1---------------------")

form = document.getElementsByTagName("form")
console.log(form)

//2 
console.log("-----------------ex2 part2----------------------")

let fname = document.getElementById("fname")
console.log(fname)

let lname = document.getElementById("lname")
console.log(lname)

let submit = document.getElementById("submit")
console.log(submit)


//3
console.log("-----------------ex2 part3----------------------")

let fname_name = document.getElementsByName("fname")
console.log(fname)

let lname_name = document.getElementsByName("lname")
console.log(lname)

//4
console.log("-----------------ex2 part4----------------------")


function handleSubmit(event) {
    event.preventDefault();
    let form = event.target;
    let fname = form[0].value;
    let lname = form[1].value;
    console.log(fname);
    console.log(lname);
    if (fname && lname) {
        let li1 = document.createElement('li');
        let li2 = document.createElement('li');
        li1.innerText = fname;
        li2.innerText = lname;
    parentEl = document.getElementsByClassName("usersAnswer");
    parentEl[0].appendChild(li1)
    parentEl[0].appendChild(li2)
    console.log(parentEl[0])
    }
}
    


      





