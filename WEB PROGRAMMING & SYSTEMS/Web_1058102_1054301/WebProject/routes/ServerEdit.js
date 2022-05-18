const { json } = require('express');
const express = require('express');//IMPORT EXPRESS FRAMEWORK
// const { $where } = require('../models/User');
const bcrypt = require('bcrypt');
const router  = express.Router();

const User = require('../models/User');
const File = require('../models/File');

//ΣΕΛΙΔΑ Upload.
router.get('/', (req,res) =>{
    if(!req.session.user_id){
        res.redirect('/');
    }else{
    res.render('Edit');
   }
})



//ΣΤΑΤΙΣΤΙΚΑ  UPLOAD.
router.get('/Data', async (req,res)=>{
    const statistika = await File.find({});
    const DedomenaHeatmap = await File.countDocuments({}, function(err,count){
        console.log("Plithos",count);
    });
    const TelikoHeatmap = {"server_data":statistika,"count":DedomenaHeatmap};
    res.send(TelikoHeatmap);
})



/*HASH BCRYPT*/
router.post('/', async (req,res,) => {
    var username = req.body.username;
    var password = req.body.password;
    var hash = await bcrypt.hash(password,12);
    User.updateOne({_id:req.session.user_id,$set:{"username":username,"password":hash}})
        .then((user)=>{
            if(user != null){
                console.log("Επιτυχής αλλαγή δεδομένων ",user);
                req.session.user_id = user._id;
                res.send({redirect: '/'});
            }else if(user == null){
                res.send({redirect: '/Edit'});
            }
        }).catch((err)=>{
                console.log("QUERY WRONG!");
                res.send({redirect: '/Edit'});
            });

});


module.exports = router;
