const mongoose = require("mongoose");

const fileSchema = new mongoose.Schema({
    startedDateTime:{
        type: String
    },
    serverIPAddress:{
        type: String
    },
    timings:{
        type: String,
    },
    url:{
        type: String
    },
    method:{
        type: String
    },    
    request_headers:[{
        content_type: String,
        cache_cotrol: String,
        pragma: String,
        expires: String,
        age: String,
        last_modified: String,
        host: String   
    }],
    status:{
        type: String
    },
    statusText:{
        type: String
    },
    response_headers:[{
        content_type: String,
        cache_cotrol: String,
        pragma: String,
        expires: String,
        age: String,
        last_modified: String,
        host: String   
    }],
    user_lat:{
        type: String
    },
    user_lon:{
        type: String
    },
    server_long:{
        type: String
    },
    server_lat:{
        type: String
    },
    user_isp:{
        type: String
    },
    user_city:{
        type: String
    },
    uploaddate:{
        type: Date,
        default: Date.now
    },
    harcount: {
        type: Number,
        default: 0
    },
    user_id:{
        type: mongoose.Schema.Types.ObjectId,
        ref: 'User'
    }
})


const File = mongoose.model('File',fileSchema);

module.exports=File;