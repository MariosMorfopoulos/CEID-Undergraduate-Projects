const mongoose = require('mongoose');//Με αυτή την εντολή το συνδέω με το app.js

//Φτίαχνω το Schema του User
const userSchema = new mongoose.Schema({
    // harcount: {
    //     type: Number,
    //     default: 0
    // },
    username: {
        type: String
        //required:true,
        //unique:true
    },
    password:{
        type: String
        //required:true    
    },
    email:{
        type: String
        //required:true
    },
    // admin:[{
    //     username: String,
    //     password: String,
    // }]
    //,
    // uploaddate:{
    //     type: Date,
    //     default: Date.now
    // }
})

//Το Schema του User το κάνω model για να μπει στην βάση σαν collection(σαν πίνακας.)
//Επίσης οταν δημιουργηθεί το model θα παει σαν πληθυντικο στην βάση users δηλαδή.
const User = mongoose.model('User', userSchema);


//Me το module.exports κάνω εξαγωγή το collection(πίνακα) User οπου θέλω.
module.exports=User;