const { request } = require('express');
const express = require('express');//IMPORT EXPRESS FRAMEWORK
// const { $where } = require('../models/User');
const router  = express.Router();


const Admin = require('../models/Admin');
const Request = require('../models/Requests');


//Η σελίδα του ADMIN.
// rooter.get('/',(req,res) => {
//     res.render('AdminData');
// })

router.get('/',(req,res)=>{

    res.render('AdminIndex');
    
})


router.get('/AdminIndex',(req,res)=>{
    const file = Request.find({}, function (err, result){
        if(err){
            console.log(err);
        }else{
            epas = result;
        }   
    })
    
    
})

// router.post('/',(req,res)=>{
//     var username=req.body.username;
//     var password=req.body.password;
//     res.send(req.body);
//     console.log(req.body);
// })
//     // Admin.findOne({username : username , password : password})
//     //      .then((admin)=>{
//     //         if(admin != null){
//     //             console.log("Υπάρχει ο Admin",admin);
//     //             //AETIOS
//     //             // const token = jwt.sign({ user }, secret);
//     //             // console.log(token);
//     //             //req.session.isAth = true;
//     //             req.session.admin_id = admin._id;
//     //             console.log( req.session.admin_id);
//     //             //Edw prepei na ftiaxnw ena session.!!!!!
//     //             //console.log(req.session.isAth);
//     //             //console.log(req.session.user_id);
//     //             //console.log(req.sessionID);
//     //             //res.send(response.message);
//     //             res.send({redirect: '/AdminData'});
//     //         }else if(admin == null){
//     //             console.log("ΔΕΝ ΥΠΑΡΧΕΙ Ο ADMIN");
//     //             res.send({redirect: '/'});
               
//     //         }    
//     //     }).catch((err)=>{
//     //         console.log("QUERY WRONG!");
//     //         res.send({redirect: '/AdminData'});
//     //     });


// Admin.findOne({username : username , password : password})
//          .then((admin)=>{
//             if(user != null){
//                 console.log("Υπάρχει ο Admin",admin);
//                 //AETIOS
//                 // const token = jwt.sign({ user }, secret);
//                 // console.log(token);
//                 //req.session.isAth = true;
//                 req.session.admin_id = admin._id;
//                 console.log( req.session.admin_id);
//                 //Edw prepei na ftiaxnw ena session.!!!!!
//                 //console.log(req.session.isAth);
//                 //console.log(req.session.user_id);
//                 //console.log(req.sessionID);
//                 //res.send(response.message);
//                 res.send({redirect: '/AdminData'});
//             }else if(admin == null){
//                 console.log("ΔΕΝ ΥΠΑΡΧΕΙ Ο ADMIN");
//                 res.send({redirect: '/'});
               
//             }    
//         }).catch((err)=>{
//             console.log("QUERY WRONG!");
//             res.send({redirect: '/Upload'});
//         });


module.exports = router;
