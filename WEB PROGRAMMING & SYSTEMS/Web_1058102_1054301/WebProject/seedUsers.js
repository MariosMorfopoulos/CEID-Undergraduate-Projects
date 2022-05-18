//Σε αυτό το script βάζω data στην βάση δεδομένων.
const mongoose = require('mongoose');

const User = require('./models/User');

mongoose.connect('mongodb://localhost:27017/WebDatabase', {useNewUrlParser: true, useUnifiedTopology: true})
    .then(() => {
        console.log("MONGO CONNECTION OPEN!!!")
    })
    .catch(err => {
        console.log("OH NO MONGO CONNECTION ERROR!!!!")
        console.log(err)
    })

const seedUsers = [
    {   
        username: 'marios',
        password: 'A!1asdfg',
        email: 'morfop@gmail.com',
       
    },{
        username: 'admin',
        password: '1234',
        email: 'admin@gmail.com'
    }
    
// // admin:{
//     username: 'admin',
//     password:"1234"
// }
 ]

User.insertMany(seedUsers)
    .then(res =>{
        console.log(res)
    })
    .catch(e =>{
        console.log(e) 
    })

