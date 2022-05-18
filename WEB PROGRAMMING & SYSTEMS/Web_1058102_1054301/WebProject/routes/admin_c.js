const express = require("express");
const bcrypt = require("bcrypt");
const geoip = require("geoip-lite");

const router = express.Router();

const Morf = require("../models/File");

router.get("/", (req, res) => {
  if (!req.session.admin_id) {
    res.redirect("/admin_login");
  } else {
    res.render("admin_c");
  }
});
router.get("/1", function (req, res) {
  var epas;
  const file = Morf.find({}, function (err, result) {
    if (err) {
      console.log(err);
    } else {
      epas = result;
    }
    let data = [];
    let data_age = [];
    let counter_ar = [];

    //ftiaxnw ena json pou periexei serverIP,lat kai lon
    for (let i = 0; i < epas.length; i++) {
      content_type = epas[i].response_content_type;
      response_headers = epas[i].response_headers;
      user_isp = epas[i].user_isp

      //console.log(response_headers);
      if (response_headers != null) {
        for (let j = 0; j < response_headers.length; j++) {
          age = response_headers[j].age;
          expires = response_headers[j].expires;
          last_modified = response_headers[j].last_modified;
          content_type = response_headers[j].content_type;
        }
        if (age == null && expires != null && last_modified != null) {
          const date1 = new Date(expires);
          const date2 = new Date(last_modified);
          const diffTime = Math.abs(date2 - date1);
          const diffDays = Math.ceil(diffTime / (60 * 60 * 24));
          data_age.push(parseInt(diffTime));
          var ttl = {
            content_type: content_type,
            age: parseInt(diffTime),
          };
        } else {
          age = getNum(parseInt(age));
          data_age.push(parseInt(age));
          var ttl = {
            content_type: content_type,
            age: parseInt(age),
          };
        }
        data.push(ttl);
      }
    }
    //console.log("that my max");
    var max = data_age.reduce(function (a, b) {
      return Math.max(a, b);
    }, 0);
    for (var i = 0; i < data_age.length; i++) {
      if (data_age[i] === 0) {
        data_age.splice(i, 1);
      }
    }
    console.log(data_age);
    console.log(data_age.length);
    for (let i = 0; i < 9; i++) {
      let counter = 0;
      let counter1 = 0;
      let counter2 = 0;
      let counter3 = 0;
      let counter4 = 0;
      let counter5 = 0;
      let counter6 = 0;
      let counter7 = 0;
      let counter8 = 0;
      let counter9 = 0;
      for (let j = 0; j < data_age.length; j++) {
        //console.log(data_age[j]);
        if (data_age[j] < max / 10) {
          counter++;
        } else if (max / 10 < data_age[j] && data_age[j] <= (2 * max) / 10) {
          counter1++;
        } else if (
          (2 * max) / 10 < data_age[j] &&
          data_age[j] < (3 * max) / 10
        ) {
          counter2++;
        } else if (
          (3 * max) / 10 < data_age[j] &&
          data_age[j] < (4 * max) / 10
        ) {
          counter3++;
        } else if (
          (4 * max) / 10 < data_age[j] &&
          data_age[j] < (5 * max) / 10
        ) {
          counter4++;
        } else if (
          (5 * max) / 10 < data_age[j] &&
          data_age[j] < (6 * max) / 10
        ) {
          counter5++;
        } else if (
          (6 * max) / 10 < data_age[j] &&
          data_age[j] < (7 * max) / 10
        ) {
          counter6++;
        } else if (
          (7 * max) / 10 < data_age[j] &&
          data_age[j] < (8 * max) / 10
        ) {
          counter7++;
        } else if (
          (8 * max) / 10 < data_age[j] &&
          data_age[j] < (9 * max) / 10
        ) {
          counter8++;
        } else if (
          (9 * max) / 10 < data_age[j] &&
          data_age[j] <= (10 * max) / 10
        ) {
          counter9++;
        }
      }
      counter_ar = [
        counter,
        counter1,
        counter2,
        counter3,
        counter4,
        counter5,
        counter6,
        counter7,
        counter8,
        counter9,
      ];
    }
    var data1 = {
      max: max,
      counter_ar: counter_ar,
      user_isp : user_isp

    };
    //console.log(counter_ar);
    //console.log(data_age.length);
    res.json(data1);
  });
});

function getNum(val) {
  if (isNaN(val)) {
    return 0;
  }
  return val;
}
module.exports = router;
