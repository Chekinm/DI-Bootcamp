function isIntOneToTen(value) {
    return (value) && /^[0-9]+$/.test(value) && value < 11 && value > 0;
}

function getUserInput(text, checkFunction) {
    let input
    do {
        input = prompt (text);
        flag = checkFunction(input);
        if (!flag) alert('Wrong input') ;
    } while (!flag);
    return input;
}

function randint(start, end) {
    return Math.round(Math.random() * (end - start) + start);
}

function gameRound() {
    let playerNum = getUserInput('Guess the number fro 1 to 10', isIntOneToTen);
    let compNum = randint(1,10);
    return playerNum == compNum;
}


const NUM_OF_CHANSES = 2;


function  playTheGame() {
    //name function deal with game flow
    heLikeToPlay = confirm('Whould you like to play a game?')
    if (heLikeToPlay) {
        let chances = NUM_OF_CHANSES;
        do { // we do until user want to play, but not more then NUM_OF_CANCE wrong answer
            if (gameRound()) {
                alert('Cool! Your guess is right!');
                let heLikeToPlay = confirm('Whould you like to continue?');
            } else {
                alert ('Bad luck! Try again!');
                chances--;
                let suffix = (chances>1) ? 's':''
                if (chances) alert (`You have ${chances} more attempt${suffix}`);
            }
        } while (chances && heLikeToPlay)
        alert ('No more chances! See you next time!')

    } else {
        alert ('No problem. See you later!')
    }
    
}

