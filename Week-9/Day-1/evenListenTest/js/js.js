
function insertRow() {
    let tb = document.getElementById("sampleTable")
    let tbody = tb.firstElementChild
    
    let tr = tbody.lastElementChild
    let td = tr.firstElementChild.textContent
    
    regex = /\d+/
    num = td.match(regex)
    let newCell1 = document.createTextNode(`Row${Number(num)+1} Cell1`);
    let newCell2 = document.createTextNode(`Row${Number(num)+1} Cell2`);
    
    let newRow = tbody.insertRow()
    let newCellE1 = newRow.insertCell(0);
    let newCellE2 = newRow.insertCell(1);
    newCellE1.appendChild(newCell1)
    newCellE2.appendChild(newCell2)
    
 
    
    console.log(num)
}

function insertText() {

    let div1 = document.getElementById("test1")
    let div2 = document.getElementById("test2")
    
    let newText1 = document.createTextNode('This to be added to Test1');
    
    
    div1.appendChild(newText1)
    div2.innerText = "This is text to be add to test2"
    console.log(div1)
}