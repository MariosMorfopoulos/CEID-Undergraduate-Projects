//Σε αυτό το script βάζω data στην βάση δεδομένων.
const mongoose = require('mongoose');

const Admin = require('./models/Admin');

mongoose.connect('mongodb://localhost:27017/WebDatabase', {useNewUrlParser: true, useUnifiedTopology: true})
    .then(() => {
        console.log("MONGO CONNECTION OPEN!!!")
    })
    .catch(err => {
        console.log("OH NO MONGO CONNECTION ERROR!!!!")
        console.log(err)
    })

const seedAdmins = [
    {   
        // upload_har_count:
        username: 'admin',
        password: '1234',
        //email: 'morfop@gmail.com'
    }
 ]

Admin.insertMany(seedAdmins)
    .then(res =>{
        console.log(res)
    })
    .catch(e =>{
        console.log(e) 
    })