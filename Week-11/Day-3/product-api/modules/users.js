const {db}  = require('../config/db.js');


const register = (email, password) => {
  return db('users')
  .insert({email,password})
  .returning('*')
}

const login = (email) => {
  return db('users')
  .select('id','email','password')
  .where({email})
}

module.exports = {
  register,
  login
}
