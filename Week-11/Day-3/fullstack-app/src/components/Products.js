import {useState, useEffect} from 'react'


const Products = (props) => {

    const [products, setProducts] = useState([])

    useEffect (() =>{
        all()
    },[])

    const all = async () => {
        
        try {
            const res = await fetch('http://127.0.0.1:3030/api/products');
            const data = await res.json();
            setProducts(data)
        } catch (e) {
            console.log(e)
        }
    }

    const getFiltered = async (searchValue) => {
        
        try {
            const res = await fetch('http://127.0.0.1:3030/api/products');
            const data = await res.json();
            setProducts(data.filter((item)=>item.name.includes(searchValue)))
        } catch (e) {
            console.log(e)
        }
    }


    const searchProduct = (e) => {
        try {
            e.preventDefault();
            const form = e.target;
            const formData = new FormData(form)
            const fromJson = Object.fromEntries(formData.entries())
            console.log(fromJson)
            getFiltered(fromJson.searchValue)
        } catch (e) {
            console.log(e)
        }
    }




    


    return(
        <div>
            <h1>Shop</h1>
            <form onSubmit={searchProduct}>
                <input name='searchValue' type='text'></input>
                <button type='submit'>Search</button>
            </form>
            {
                products.map(item => {
                    return(
                        <div key={item.id} style={{
                                display:'inline-block',
                                padding: '20px',
                                margin:'20px',
                                border:'2px solid black',
                            }}>
                            <h4>{item.name}</h4>
                            <h3>{item.price}</h3>
                        </div>
                    )
                })}
        </div>
    )

}
export default Products