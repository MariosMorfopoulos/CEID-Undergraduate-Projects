const express = require('express');//IMPORT EXPRESS FRAMEWORK
const router  = express.Router();//IMPORT ROUTES
const bcrypt = require('bcrypt');


/* MODEL USER */
const User = require('../models/User');




// router.post('/',  (req,res) =>{
//     //res.send(req.body);
//     //console.log("eisai mlks",req.body);
//     var username = req.body.username;
//    // var password = req.body.password;
//    //, password : password
//     test = User.findOne({username : username })
//         .then((user)=>{
//             if(user != null){
//                 console.log("ΒΡΕΘΗΚΕ ΙΔΙΟΣ  USER",user.username);
//                     // if(user.username == 'admin'){
//                     //     res.send({redirect:'/AdminIndex'});
//                     //     //Edw prepei na mpei session
//                     //     console.log("marios1");
//                     // }else
//                     //{
//                         req.session.test_id = test._id;
//                         console.log("poutsa");
//                         res.send({redirect: '/Upload'});

//                         //res.redirect("Upload");
//                         //req.session.user_id = user._id;
//                        console.log( req.session.user_id);
//                        console.log("kwlos");
//                     //}
                
//                 //console.log( req.session.user_id);
//                 //Edw prepei na ftiaxnw ena session.!!!!!
//                 //console.log(req.session.isAth);
//                 //console.log(req.session.user_id);
//                 //console.log(req.sessionID);
//                 //res.send(response.message);
                
//             }else if(user == null){
//                 console.log("ΔΕΝ ΒΡΕΘΗΚΕ ΙΔΙΟΣ USER");
//                 res.send({redirect: '/'});
               
//             }    
//         }).catch((err)=>{
//             console.log("QUERY WRONG!");
//             res.send({redirect: '/Upload'});
//         });
// });

router.post('/', async (req,res)=>{
    var username = req.body.username;
    var password = req.body.password;
    const user = await User.findOne({username}) 
    const validpassword = await bcrypt.compare(password,user.password)   
    if(validpassword){
        req.session.user_id = user._id;
        console.log( req.session.user_id);
        res.send({redirect: '/Upload'});
    }else{
        console.log("ΔΕΝ ΒΡΕΘΗΚΕ ΙΔΙΟΣ USER");
        res.send({redirect: '/'});
    }

})

// router.post('/', (req,res)=>{
//     var username = req.body.username;
//     var password = req.body.password;
//     User.findOne({username : username , password : password})
//         .then(()=>{
//             if(user != null){
//                 console.log("ΒΡΕΘΗΚΕ ΙΔΙΟΣ  USER",user);
//                 // if(user.username == 'admin'){
//                 //     res.send({redirect:'AdminIndex'});
//                 // }
//                 req.session.user_id = user._id;
//                 console.log( req.session.user_id);
//                 //Edw prepei na ftiaxnw ena session.!!!!!
//                 //console.log(req.session.isAth);
//                 //console.log(req.session.user_id);
//                 //console.log(req.sessionID);
//                 //res.send(response.message);
//                 res.send({redirect: '/Upload'});
//             }else if(user == null){
//                 console.log("ΔΕΝ ΒΡΕΘΗΚΕ ΙΔΙΟΣ USER");
//                 res.send({redirect: '/'});
               
//             }    
//         }).catch((err)=>{
//             console.log("QUERY WRONG!");
//             res.send({redirect: '/Upload'});
//         });
// });

// app.post("/logout", (req, res) => {
//     //req.session.user_id = null;
//     req.session.destroy();
//     res.redirect("/login");
// });


// router.post('/get-docs', checkIfLogin, async (req, res) => {
//     const user = req.user;
  
//     console.log(user);
//     console.log(user.username);
  
//     const docs = await Doc.find({ username: user.username });
  
  
//     return res.send({ docs });
// });
// function checkIfLogin(req, res, next) {
//     const token = req.headers['authorization'];
//     const user = jwt.verify(token, secret);
  
//     if (!user) return res.status(401);
//     if (!user.isAdmin) return res.status(401);
  
//     req.user = user.user;
//     next();
// }





module.exports = router;

