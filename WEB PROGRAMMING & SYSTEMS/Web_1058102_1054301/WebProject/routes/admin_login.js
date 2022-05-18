const express = require("express");
const bcrypt = require("bcrypt");

const router = express.Router();

const Admin = require("../models/Admin");

router.get("/", (req, res) => {
  res.render("admin_login");
});

router.post("/", async (req, res) => {
  const { username, password } = req.body;
  const admin = await Admin.findOne({ username });
  //const validPassword = await compare(password, admin.password);
  if (password == admin.password) {
    req.session.admin_id = admin._id;
    console.log("poutsa")
    res.redirect("morf_stats");
  } else {
    res.send("Try Again");
  }
});

module.exports = router;