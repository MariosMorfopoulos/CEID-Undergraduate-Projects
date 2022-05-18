const express = require("express");
const bcrypt = require("bcrypt");

const router = express.Router();

const Morf = require("../models/File");
const Users = require("../models/User");

router.get("/", (req, res) => {
  if (!req.session.admin_id) {
    res.redirect("/admin_login");
  } else {
    res.render("admin_stats");
  }
});
router.get("/1", (req, res) => {
  const file = Morf.find({}, function (err, result) {
    if (err) {
      console.log(err);
    } else {
      epas = result;
    }
    console.log("auto einai to length");
    console.log(epas.length);
    let method = [];
    let status = [];
    let users = [];
    let url = [];
    let count_method = [];
    let count_status = [];
    let count_status_counter = [];
    let age = [];
    let content_type = [];
    let c_response = [];
    let count_age_c_t = [];
    let av_life = [];

    
    for (let i = 0; i < epas.length; i++) {
      method.push(epas[i].method);
      status.push(epas[i].status);
      users.push(epas[i].user_id);
      url.push(epas[i].url);
      response_headers = epas[i].response_headers;
      request_headers = epas[i].request_headers;

      if (response_headers != null) {
        for (let j = 0; j < response_headers.length; j++) {
          content_type.push(response_headers[j].content_type);
          age.push(response_headers[j].age);
        }
      }
      if (request_headers != null) {
        for (let k = 0; k < request_headers.length; k++) {
          content_type.push(request_headers[k].content_type);
          age.push(request_headers[k].age);
        }
      }
    }
    console.log(content_type);
    //ftiaxnoume unique methods
    var unique_method = method.filter((v, i, a) => a.indexOf(v) === i);
    var unique_url = url.filter((v, i, a) => a.indexOf(v) === i);
    var unique_status = status.filter((v, i, a) => a.indexOf(v) === i);
    var unique_users = users.filter((v, i, a) => a.indexOf(v) === i);
    var unique_content_type = content_type.filter(
      (v, i, a) => a.indexOf(v) === i
    );
    console.log("Auto einai to unique content");
    console.log(unique_content_type.length);
    //dimiourgw ena pinaka me ta eidi methodwn kai to poses fores emfanizontai
    for (var j = 0; j < unique_method.length; ++j) {
      var counter_method = 0;
      for (var k = 0; k < method.length; ++k) {
        if (method[k] == unique_method[j]) {
          counter_method++;
        }
      }
      count_method.push([unique_method[j], counter_method]);
    }
    //dimiourgw ena pinaka me ta eidi twn status kai to poses fores emfanizontai
    for (var j = 0; j < unique_status.length; ++j) {
      var counter_status = 0;
      for (var k = 0; k < status.length; ++k) {
        if (status[k] == unique_status[j]) {
          counter_status++;
        }
      }
      status_point = "Status " + String(unique_status[j]);
      count_status.push(status_point);
      count_status_counter.push(counter_status);
    }
    console.log(count_status);
    console.log("pali to unique content type");
    console.log(unique_content_type);

    //dimiourgw ena pinaka poy periexei ta monadika content type, tin mesi ilikia kathe web object kai to count tou kathe response content type
    for (var j = 0; j < unique_content_type.length; ++j) {
      var counter_response = 0;
      var result = 0;
      for (var k = 0; k < content_type.length; ++k) {
        if (content_type[k] == unique_content_type[j]) {
          counter_response++;
          if (age[k] === undefined || age[k] === null) {
            age[k] = 0;
          } else {
            result = result + parseInt(age[k]);
          }
        }
      }
      count_age_c_t.push(unique_content_type[j]);
      av_life.push(result / counter_response);
    }
    var data = {
      username_len: unique_users.length,
      method_len: count_method,
      status_len: count_status,
      status_counter: count_status_counter,
      url_len: unique_url.length,
      web_object_a_a: count_age_c_t,
      aver_life: av_life,
    };

    res.json(data);
  });
});
router.get("/2", function (req, res) {
  distinct1 = Users.distinct("_id").exec(function (err, count) {
    console.log("The number of unique users is: %d", count.length);
    res.json(count.length);
  });
});
module.exports = router;
