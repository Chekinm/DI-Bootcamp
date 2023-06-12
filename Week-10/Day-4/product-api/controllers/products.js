const { getAllProducts,
       getProduct
    } = require('../modules/products.js')


const _getAllProducts = (req, res) => {
    getAllProducts()
    .then(data => {
        res.json(data)
    })
    .catch(err=>{
        console.log(err);
        res.status(404).json({msg:err.message})
    })
}

module.exports = {
    _getAllProducts
}