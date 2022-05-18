const express = require("express");
const bcrypt = require("bcrypt");
const geoip = require("geoip-lite");

const router = express.Router();

const Morf = require("../models/File");

router.get("/", (req, res) => {
    if(!req.session.user_id){
        res.redirect('/');
    }else{
    res.render("Heatmap");
   }
});

module.exports = router;
