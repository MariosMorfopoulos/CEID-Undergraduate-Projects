const mongoose = require('mongoose');//Με αυτή την εντολή το συνδέω με το app.js


const entriesSchema = new mongoose.Schema({
    startedDateTime:{
        type: String
    },
    serverIPAddress:{
        type: String
    },
    timings:{
        type: String,
    },
    user_id:{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User'

    }
})


const Entries = mongoose.model('Entries',entriesSchema);

module.exports=Entries;