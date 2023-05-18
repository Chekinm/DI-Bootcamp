function isIntOneTo99(value) {
    return (value) && /^[0-9]+$/.test(value) && value < 100 && value > 0;
}

function getUserInput(text, checkFunction) {
    let input
    do {
        input = prompt (text);
        flag = checkFunction(input);
        if (!flag) alert('Wrong input') ;
    } while (!flag);
    console.log(input)
    return input;
}

function setText(numbOfButtle,toDrink) {

    if (toDrink >= numbOfButtle){
        suffix = (numbOfButtle == 1) ? 's':''
        plural = (numbOfButtle == 1) ?  'them' : 'it'
        text = `Last ${numbOfButtle} buttle${suffix} remain one the wall. We pass all around, and no more at all. all--all--all! all--all--all! Now we drunk all--all--all!`
        return {text:text,flag:false}
    } else {
        suffix = (toDrink == 1) ? 's':''
        plural = (toDrink == 1) ? 'it' : 'them'
        text = `Last ${numbOfButtle} buttle${suffix} remain one the wall. We pass ${toDrink} around. Now ${numbOfButtle-toDrink} bottles of beer, on, the wall.`
        return {text:text,flag:true}
    }   
}

function sayText(text) {
    var u = new SpeechSynthesisUtterance();
    u.text = text;
    u.lang = 'en-US';
    u.rate = 1.2;
    //u.onend = function(event) { alert('Finished in ' + event.elapsedTime + ' seconds.'); }
    speechSynthesis.speak(u);
}


function singASong() {

    let numbOfButtle = getUserInput ("How many buttle we have? ", isIntOneTo99)
    toDrink = 1
    let response
    do  {
        response = setText(numbOfButtle, toDrink)
        console.log(response.text)
        sayText (response.text)
        numbOfButtle = numbOfButtle - toDrink
        toDrink++
    } while (response.flag)
}
    
audio = document.getElementById("audio");
audio.volume = 0.3;


