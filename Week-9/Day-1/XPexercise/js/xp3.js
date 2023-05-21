let allBoldItems;

function getBoldItems() {
    let itemList = document.getElementsByTagName('strong')
    //console.log(itemList)
    return itemList
}

let boldList = getBoldItems()

function highlite() {
    itemList = getBoldItems()
    for (item of itemList) {
        item.style.color = "blue"
    }
}


function returnNormal() {
    itemList = getBoldItems()
    for (item of itemList) {
        item.style.color = "black"
    }
}


