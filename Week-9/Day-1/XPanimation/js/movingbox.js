function setBoxLeftPostion(left) {
    let box = document.getElementById("animate")
    box.style.left = left + "px"
}

let moving
function myMove() {
    let left = 0
    moving = setInterval(function iterLeft(){
        setBoxLeftPostion(left);
        left ++;
        console.log(left)
        if (left >= 350) {
            clearInterval(moving);
        }
    },
    20
    )
}

function StopMyMove() {
    clearInterval(moving)
}

