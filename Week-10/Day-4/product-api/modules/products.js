const {db} = require('../dbconfig/db.js');

const getAllProducts = () => {
    return db('products')
    .select('id','name','price')
    .orderBy('name')
}

const getPoduct = (product_id) => {
    return db('product')
    .select('id','name','price')
    .where({id:product_id})
}   

module.exports = {
    getAllProducts,
    getPoduct
}