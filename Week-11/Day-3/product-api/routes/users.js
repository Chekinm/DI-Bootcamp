const express = require('express');
const router = express.Router();

const {_register,_login} = require('../controllers/users.js')


router.post('/register', _register);
router.post('/login', _login);

module.exports = {
  router
}
