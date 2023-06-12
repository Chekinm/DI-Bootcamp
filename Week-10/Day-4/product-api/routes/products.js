const express = require('express');

const router = express.Router();
const {_getAllProducts} = require('../controllers/products.js')

router.get('/api/products', _getAllProducts)

module.exports = {
    router
}