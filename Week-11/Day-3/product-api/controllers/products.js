const { getAllProducts,
        getProduct,
        searchProduct,
        insertProduct,
        deleteProduct,
        updateProduct
      } = require('../modules/products.js');

// READ - GET all get all products
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

const _getAllProductsEjs = (req, res) => {
  getAllProducts()
  .then(data => {
    res.render('shop', {
      data
    })
  })
  .catch(err=>{
    console.log(err);
    res.render('404')
    // res.status(404).json({msg:err.message})
  })
}



const _getProduct = (req,res) =>{
  const id = req.params.id;
  getProduct(id)
  .then(data => {
    res.json(data)
  })
  .catch(err=>{
    console.log(err);
    res.status(404).json({msg:err.message})
  })
}

const _searchProduct = (req,res) => {
  searchProduct(req.query.name)
  .then(data => {
    res.json(data)
  })
  .catch(err=>{
    console.log(err);
    res.status(404).json({msg:err.message})
  })
}

const _insertProduct = (req, res) =>{
  insertProduct(req.body)
  .then(data => {
    res.json(data)
  })
  .catch(err=>{
    console.log(err);
    res.status(404).json({msg:err.message})
  })
}

const _deleteProduct = (req, res) =>{
  deleteProduct(req.params.id)
  .then(data => {
    res.json(data)
  })
  .catch(err=>{
    console.log(err);
    res.status(404).json({msg:err.message})
  })
}

const _updateProduct = (req, res) => {
  updateProduct(req.params.id, req.body)
  .then(data => {
    res.json(data)
  })
  .catch(err=>{
    console.log(err);
    res.status(404).json({msg:err.message})
  })
}

module.exports = {
  _getAllProducts,
  _getProduct,
  _searchProduct,
  _insertProduct,
  _deleteProduct,
  _updateProduct,
  _getAllProductsEjs
}
