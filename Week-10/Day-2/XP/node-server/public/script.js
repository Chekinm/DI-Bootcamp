const mydiv = document.getElementById("mydiv")


async function loadJson() {
    const resp = await fetch('http://127.0.0.1:3003/users/')
    const jsonData = await resp.json();
        console.log(jsonData);
        mydiv.innerText = JSON.stringify(jsonData)
}
loadJson()

    