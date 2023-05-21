let db = {
    "noun" : [],
    "adjective": [],
    "person": [],
    "verb": [],
    "place": []
}

 




function isValid(form) {
    for (item in db) {
        let isValid = true;
        if (!form[item].value) {
            return false;
        }
    }
    return true;
}


function submitHandler(event) {

    event.preventDefault()
    let form = event.target
    console.log(form)
    if (isValid(form)) {
        for (item in db) {
            db[item].push(form[item].value)
        }
    } else {
        alert ('Enter all value')
    }
        console.log(db)
    }

    function rnd(num) {
        return Math.round(Math.random()*num)
    }


function generateStory(event) {
    console.log('im here')
    num = db["noun"].length-1
    console.log(num)
    console.log(db["person"][0])
    let story = `One upon a time ${db["person"][rnd(num)]} takes ${db["noun"][rnd(num)]} and go to ${db["place"][rnd(num)]} to ${db["verb"][rnd(num)]}`  
    storyPlaceHolder = document.getElementById("story")
    storyPlaceHolder.innerText = story
}