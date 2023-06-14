const getMyProducts = async () => {
  try {
    const res = await fetch('/api/products/');
    const data = await res.json();
    console.log(data);
    render(data)
  } catch (e) {
    console.log(e);
  }
}

const render = (arr) => {
  const html = arr.map(item => {
    return `<div
    style="display:inline-block;
          border:1px solid #ccc;
          padding:20px;
          margin:20px;">
      <h2>${item.name}</h2>
      <p>${item.price}</h2>
    </div>`;
  })
  document.getElementById('root').innerHTML = html.join('')
}
getMyProducts()
