const express = require('express');//IMPORT EXPRESS FRAMEWORK
// const { $where } = require('../models/User');
const router  = express.Router();
const bcrypt = require('bcrypt');


const User = require('../models/User');

//H σελίδα του SignUp.
router.get('/', (req,res) =>{
    res.render('SignUp');
}) 


//Orizw Parent endpoint sto arxeio tou Server.
router.post('/',  async (req,res) => {
    //res.send(req.body)
    //console.log("eisai mlks",req.body);
    var username=req.body.username;
    var password=req.body.password;
    var email=req.body.email;
    var hash = await bcrypt.hash(password,12);
    User.findOne({username : username , email : email})
        .then((user)=>{
            if(user != null){
                console.log("ΒΡΕΘΗΚΕ ΙΔΙΟΣ  USER",user);
                //res.send('/SignUp');
                res.send({redirect: '/SignUp'});
            }else if(user == null){
                console.log("ΔΕΝ ΒΡΕΘΗΚΕ ΙΔΙΟΣ USER");
                var newUser = new User({
                    username:username,
                    password:hash,
                    email:email
                })
                newUser.save();
                req.session.user_id = newUser._id;
                console.log( req.session.user_id);
                console.log("Επιτυχής Εγγραφή", newUser);
                console.log("Username: "+username+ "Password: " + hash + "Email: " + email);
                res.send({redirect: '/'});
                // User.insertOne({username : username , password : password , email : email})
                // User.save();
                // res.send({redirect: '/'});
            }    
        }).catch((err)=>{
            console.log("QUERY WRONG!");
            res.send({redirect: '/SignUp'});
        });  
}); 


module.exports = router;


 // var newUser = new User({
    //     username:username,
    //     password:password,
    //     email:email
    // })
    // await  newUser.save();
    // console.log("Επιτυχής Εγγραφή", User);
    // console.log("Username: "+username+ "Password: " + password + "Email: " + email);
    // res.send({redirect: '/'});



// var newUser = new User({
//     username:username,
//     password:password,
//     email:email
// })
// newUser.save();
// console.log("Επιτυχής Εγγραφή", User);
// console.log("Username: "+username+ "Password: " + password + "Email: " + email);
// res.send({redirect: '/'});





        
        // if(!User){
        //     console.log("ΔΕΝ ΒΡΕΘΗΚΕ ΙΔΙΟΣ USER");
        //     res.send({redirect: '/SignUp'});
        // }
          
        //     console.log("ΒΡΕΘΗΚΕ");
        //     res.send({redirect: '/SignUp'});
        // }
        // if(User != null){
        //     var newUser = new User({
        //         username:username,
        //         password:password,
        //         email:email
        //     })
        //     newUser.save();
        //     console.log("Επιτυχής Εγγραφή", User);
        //     console.log("Username: "+username+ "Password: " + password + "Email: " + email);
        //     res.send({redirect: '/'});
        // }
    
//});
 
// var newUser = new User({
//     username:username,
//     password:password,
//     email:email
// })
// newUser.save();
// console.log("Επιτυχής Εγγραφή", User);
// console.log("Username: "+username+ "Password: " + password + "Email: " + email);
// res.send({redirect: '/'});



// var newUser = new User({
    //     username:username,
    //     password:password,
    //     email:email
    // })
    // newUser.save();
    // console.log("Επιτυχής Εγγραφή", User);
    // console.log("Username: "+username+ "Password: " + password + "Email: " + email);
    




// var newUser = new User({
            //     username:username,
            //     password:password,
            //     email:email
            // })
            // newUser.save();
            // console.log("Επιτυχής Εγγραφή", User);
            // console.log("Username: "+username+ "Password: " + password + "Email: " + email);



            // console.log("EISAI MLKAS 3");
            // var newUser = new User({
            //     username:username,
            //     password:password,
            //     email:email
            // })
            // newUser.save();
            // console.log("Επιτυχής Εγγραφή", User);
            // console.log("Username: "+username+ "Password: " + password + "Email: " + email);
            // res.send({redirect: '/'});
        
        // if(User != null && err != null){
        //         console.log("EISAI MLKAS 2")
        //     }    
        // }else{
        //     //console.log("TELOS");
        //     var newUser = new User({
        //         username:username,
        //         password:password,
        //         email:email
        //     })
        //     newUser.save();
        //     console.log("Επιτυχής Εγγραφή", User);
        //     console.log("Username: "+username+ "Password: " + password + "Email: " + email);
        //     res.send({redirect: '/'});
            
            
        //     // User.insertOne({username:username,password:password,email:email}),(err, result) =>{
        //     //     if(err)
        //     //     {
        //     //         console.log("bla bla",err);
        //     //     }else{
        //     //         console.log("Επιτυχής Εγγραφή", result);
        //     //         res.send({redirect: '/'});
        //     //     }
        //     // }    
        // }
        // else{
        //    User.insertOne({username:username,password:password,email:email}),(err, result) =>{
        //     if(err)
        //     {
        //         console.log("bla bla",err);
        //     }else{
        //         console.log("Επιτυχής Εγγραφή", result);
        //         res.send({redirect: '/'});
        //     } 
        // }
        // }

// User.insertOne({username:username,password:password,email:email}),(err, result) =>{
//     if(err){
//         console.log("bla bla",err);
//     }else{
//         console.log("Επιτυχής Εγγραφή", result);
//         res.send({redirect: '/'});
//     }


//newUser = new User({
    //     username:username,
    //     password:password,
    //     email:email
    // })
    // newUser.save();
    // console.log("Επιτυχής Εγγραφή", User);
    // console.log("Username: "+username+ "Password: " + password + "Email: " + email);
    // res.send({redirect: '/'});
            
            // var newUser = new User({
            //     username:username,
            //     password:password,
            //     email:email
            // })
            // newUser.save();
            //  res.send({redirect: '/'});
            // User.insertOne({username : username , password : password , email : email},(err, User)=>{
            //     if(err) throw err;
                
            // })
            // newUser = new User({
            //         username:username,
            //         password:password,
            //         email:email
            //     })
                // newUser.save();
                // res.send({redirect: '/'});
        
        // else {
        //     console.log("Επιτυχής Εγγραφή", User);
        //     newUser = new User({
        //                 username:username,
        //                 password:password,
        //                 email:email
        //             })
        //     newUser.save();
        //     res.send({redirect: '/'});
        // }
    // });
// });
        // var newUser = new User({
        //     username:username,
        //     password:password,
        //     email:email
        // })
        // await newUser.save();
        // res.send({redirect: '/'});

    //Επιτυχής Εγγραφή
    //var query = db.users.find({});
    // const query = User.findOne({username : username , password : password , email : email})
    // console.log(query);
    
    // console.log("Username: "+username+ "Password: " + password + "Email: " + email);
    // var newUser = new User({
    //     username:username,
    //     password:password,
    //     email:email
    // })
    // await newUser.save();
    // res.send({redirect: '/'});

    //newUser.save(function(response){
    // //     response.redirect(`/`)
    // // })
    // await newUser.save();
    // res.send({redirect: '/'});
    
    // newUser.save(function(err) {
    //     if (err) {
    //         if (err.name == 'MongoError')
    //         res.send('unique-error');
    //     } else {
    //         res.send('validation-complete');
    //        
    //     }
    





// routes/bla.js


 // console.log("EISAI MLKAS 2");
            // var newUser = new User({
            //     username:username,
            //     password:password,
            //     email:email
            // })
            // newUser.save();
            // console.log("Επιτυχής Εγγραφή", User);
            // console.log("Username: "+username+ "Password: " + password + "Email: " + email);
            // res.send({redirect: '/'});