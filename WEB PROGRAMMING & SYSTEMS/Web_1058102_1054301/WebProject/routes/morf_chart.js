const express = require("express");
const bcrypt = require("bcrypt");

const router = express.Router();

const Morf = require("../models/File");

router.get("/", (req, res) => {
  if (!req.session.admin_id) {
    res.redirect("/admin_login");
  } else {
    res.render("admin_chart");
  }
});
router.get("/1", (req, res) => {
  const file = Morf.find({}, function (err, result) {
    if (err) {
      console.log(err);
    } else {
      epas = result;
    }

    let method = [];
    let timing = [];
    let content_type = [];
    var dt = [];
    var td_final = [];

    for (let i = 0; i < epas.length; i++) {
      method.push(epas[i].method);
      timing.push(epas[i].timings);
      dt.push(epas[i].startedDateTime);
      response_headers = epas[i].response_headers;
      request_headers = epas[i].request_headers;
      if (response_headers != null) {
        for (let j = 0; j < response_headers.length; j++) {
          content_type.push(response_headers[j].content_type);
        }
      }
      //console.log(request_headers);
      if (request_headers != null) {
        for (let j = 0; j < request_headers.length; j++) {
          content_type.push(request_headers[j].content_type);
        }
      }
    }
    var unique_content_type = content_type.filter(
      (v, i, a) => a.indexOf(v) === i
    );
    var unique_method = method.filter((v, i, a) => a.indexOf(v) === i);
    var filtered_dt = dt.filter(e => e != null);
    //console.log(dt)
    //αν το dateTime εχει παραπανω απο ενα στοιχειο
    for (let k = 0; k < filtered_dt.length; k++) {
      upo_method = method[k];
      upo_timing = timing[k];
      upo_content_type = content_type[k];
      //console.log(filtered_dt[k])
      //epexergasia datetime
      str = filtered_dt[k].toString()
      const time = str.split("T");
      const mera = time[0].split(":");
      //gia na paroyme tin mera tis evdomadas
      const birthday = new Date(mera);
      const day1 = birthday.getDay();
      //gia na paroume tin wra tis imeras
      const wra = time[1].split(":");

      var timing_day = {
        time: wra[0],
        day: day1,
        timing: upo_timing,
        method: upo_method,
        content_type: upo_content_type,
        unique_response_content_type: unique_content_type,
        unique_method: unique_method,
      };
      td_final.push(timing_day);
    }
    console.log(td_final)
    const data1 = { td_final };
    res.json(data1);
  });
});
module.exports = router;
