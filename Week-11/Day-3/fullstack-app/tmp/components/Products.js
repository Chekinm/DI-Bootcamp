import {useState, useEffect} from 'react';

const Products =(props) => {
  const [products, setProducts] = useState([]);
  const [search, setSearch] = useState('');
  const [name, setName] = useState('')
  const [price, setPrice] = useState('')

  useEffect(()=>{
    // const all = async () => {
    //   try {
    //     const res = await fetch('http://localhost:3030/api/products');
    //     const data = await res.json();
    //     setProducts(data)
    //   } catch (e) {
    //     console.log(e);
    //   }
    // }
    all()
  },[])

  const all = async () =>{
    try {
      const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/products`);
      const data = await res.json();
      setProducts(data)
    } catch (e) {
      console.log(e);
    }
    // fetch('http://localhost:3030/api/products')
    // .then(res => res.json())
    // .then(data => {
    //   setProducts(data)
    // })
    // .catch(err => {
    //   console.log(err);
    // })
  }

  const searchProduct = async () => {
    try {
      const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/search?name=${search}`);
      const data = await res.json();
      setProducts(data)
    } catch (e) {
      console.log(e);
    }
  }

  const add = (e) => {
    e.preventDefault();
    const fetchData = async () => {
      try {
        const res = await fetch(`${process.env.REACT_APP_BASE_URL}/api/products`,{
          method:'POST',
          headers:{
            'Content-type':'application/json'
          },
          body:JSON.stringify({name,price})
        });
        const data = await res.json();
        // console.log(data);
        // all()
        setProducts(data)
      } catch (e) {
        console.log(e);
      }
    }
    fetchData()
  }
  return(
    <div>
      <h1>Shop</h1>
      <div>
        <input type="text"
              onChange={(e)=>setSearch(e.target.value)}
              />
        <button onClick={searchProduct}>Search</button>
      </div>
      <div>
        <form onSubmit={add}>
          Name: <input type="text"
                onChange={(e)=>setName(e.target.value)}
                />
          Price: <input type="text"
onCh          onChange={(e)=>setPrice(e.target.value)}
              />
          <input type="submit" value="Add"/>
        </form>
      </div>
      {
        products.map(item => {
          return(
            <div key={item.id} style={{
              display:'inline-block',
              padding: '20px',
              margin:'20px',
              border:'1px solid #fff',
            }}>
              <h4>{item.name}</h4>
              <h5>{item.price}</h5>
            </div>
          )
        })
      }
    </div>
  )
}
export default Products
