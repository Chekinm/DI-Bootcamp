const moveBoxLeft1px = (maxLeft) => {
    let box = document.getElementById("animate")
    let newLeft
    const rect = box.getBoundingClientRect(); //get position poperties object
    newLeft = rect.left > maxLeft ? 0 : rect.left + 1
    
    box.style.left = newLeft + "px"
    return newLeft
    
}

let moving
function myMove() {
    const maxLeft = 350
    let left = 0
    console.log(moving)
    if (moving !== undefined) {
        clearInterval(moving);
        }

    moving = setInterval(() => {
        left = moveBoxLeft1px(maxLeft);
        if (left >= maxLeft) {
            clearInterval(moving);
            }
        },
        200
        )
        
}
const stopMyMove = () => {
    clearInterval(moving)
}

