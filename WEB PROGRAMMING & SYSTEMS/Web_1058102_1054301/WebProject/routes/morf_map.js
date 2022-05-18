const express = require("express");
const bcrypt = require("bcrypt");
const geoip = require("geoip-lite");

const router = express.Router();

const Morf = require("../models/File");
const { distinct } = require("../models/File");

router.get("/", (req, res) => {
  if (!req.session.admin_id) {
    res.redirect("/admin_login");
  } else {
    res.render("admin_map");
  }
});
router.get("/1", function (req, res) {
  var epas;
  distinct1 = Morf.distinct("user_id").exec(function (err, count) {
    console.log("The number of unique users is: %d", count.length);
  });
  distinct1 = Morf.distinct("lat_lon").exec(function (err, count) {
    console.log("The number of unique lat_lon is: %d", count.length);
  });
  distinct2 = Morf.distinct("serverIPAddress").exec(function (err, count) {
    console.log("The number of unique serverIPAddress is: %d", count.length);
  });

  distinct5 = Morf.find()
    .distinct("serverIPAddress")
    .distinct("lat_lon", function (error, ids) {
      console.log("auto einai to distinct 5");
      console.log(ids);
    });

  const file = Morf.find({}, function (err, result) {
    if (err) {
      console.log(err);
    } else {
      epas = result;
    }
    let data = [];
    let latlon = [];
    let server = [];
    let lat1 = [];
    let lon1 = [];
    let count_method = [];
    let lat_lon = [];
  
    console.log("malakia", lat_lon);
    //console.log(epas)
    //ftiaxnw ena json pou periexei serverIP,lat kai lon
    for (let i = 0; i < epas.length; i++) {
      lat = epas[i].user_lat;
      lon = epas[i].user_lon;
      serverIP = epas[i].serverIPAddress;
      if (serverIP != null && serverIP != "") {
        var geo = geoip.lookup(serverIP);
        var map1 = {
          lat: lat,
          lon: lon,
          server1: serverIP,
          server_ll: geo.ll,
        };
      }
      data.push(map1);
    }
    var realdata = data.filter(function (e) {
      return e != null;
    });
    res.json(realdata);
  });
});

router.get("/2", function (req, res) {
  distinct4 = Morf.find().distinct("user_lat", function (error, ids) {
    console.log("auto einai to distinct 4");
    console.log(ids);
    res.json([ids]);
  });
});
router.get("/4", function (req, res) {
  distinct4 = Morf.find().distinct("user_lon", function (error, ids) {
    console.log("auto einai to distinct 4");
    console.log(ids);
    res.json([ids]);
  });
});
router.get("/3", function (req, res) {
  distinct4 = Morf.find().distinct("serverIPAddress", function (error, ids) {
    geo_ll = [];
    for (let i = 0; i < ids.length; i++) {
      serverIP = ids[i];
      if (serverIP != null && serverIP != "") {
        var geo = geoip.lookup(serverIP);
        geo_ll.push(geo.ll);
      }
    }
    res.json(geo_ll);
  });
});

module.exports = router;
