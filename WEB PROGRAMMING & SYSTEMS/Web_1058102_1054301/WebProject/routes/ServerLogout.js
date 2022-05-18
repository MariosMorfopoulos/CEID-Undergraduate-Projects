const express = require('express');//IMPORT EXPRESS FRAMEWORK
// const { $where } = require('../models/User');
const router  = express.Router();
const app = express();//EXECUTING EXPRESS

router.post('/', (req,res)=>{
        //req.session.user_id = null;
        req.session.destroy();
        res.redirect("/");
});


module.exports = router;
