const express = require('express');//IMPORT EXPRESS FRAMEWORK
// const { $where } = require('../models/User');
const router  = express.Router();
const app = express();//EXECUTING EXPRESS


//ΓΙΑ ΤΟ API IP
const ipify = require('ipify');
var https = require('https');


// var multer  = require('multer');
// var upload = require("express-fileupload");
// app.use(upload());//Εδω για  να χρησιμοποιω var upload

const fileUpload = require('express-fileupload');
app.use(fileUpload());

app.use(express.urlencoded({ extended: true }));
app.use(express.json());

/*ΠΑΛΙΑ MODELS */
//const Request = require('../models/Requests');
//const RequestHeaders = require('../models/RequestsHeaders');
//const Response = require('../models/Response');
//const ResponseHeaders = require('../models/ResponseHeaders');
//const UserUploadData = require('../models/UserUploadData');
//const Entries = require('../models/Entries');

/*ΤΕΛΙΚΑ MODELS */
const File = require('../models/File');
const User = require('../models/User');
const { callbackify } = require('util');
const { get } = require('./ServerSignUp');
const { timeStamp } = require('console');


//H σελίδα του Upload.
router.get('/', (req,res) =>{
    if(!req.session.user_id){
        res.redirect('/');
    }else{
    res.render('Upload');
    }
})

router.post('/',(req,res) => {
    // res.send(req.files);
    // console.log(req.body);
    // var json = JSON.parse(req.body);
    // console.log(req.body['info']);
    var Entry_Array = req.body['info'];
    Entry_Array.forEach(function(entry){
        var parsedEntry = JSON.parse(entry);//Dictionary(JSON OBJECT)
        //console.log(parsedEntry);
        /*ΦΤΙΑΧΝΩ ΤΑ ΣΤΟΙΧΕΙΑ ΤΟΥ  ΠΙΝΑΚΑ FILES */
        var request = parsedEntry['request'];
        var method = request['method'];
        var url  = request['url'];
        var request_headers = request['headers'];
        /*1o Debug KOMPLE */
        // console.log(request);
        // console.log(url);
        // console.log(method);
        // console.log(request_headers);
        var response = parsedEntry['response'];
        var status = response['status'];
        var statusText = response['statustext'];
        var response_headers = response['headers'];
        /*2o Debug KOMPLE */
        // console.log(response);
        // console.log(status);
        // console.log(statusText);
        // console.log(response_headers);
        var startedDateTime = parsedEntry['startedDateTime'];
        var timings = parsedEntry['timings'];
        var serverIPAddress = parsedEntry['serveripaddress'];
        var user_lat = parsedEntry['user_lat'];
        var user_lon = parsedEntry['user_lon'];
        /*3o Debug KOMPLE */
        // console.log(startedDateTime);
        // console.log(timings);
        // console.log(serverIPAddress);
        // console.log(user_lat);
        // console.log(user_lon);
        /*Εδώ θέλει και αλλα πεδια μετα για το CHART!!!!!!!! */
        /*H SERVERIPADDRESS ΕΙΝΑΙ ΣΕ ΜΟΡΦΗ  [2606:2800:220:1:248:1893:25c8:1946] ΟΠΟΤΕ ΜΕ ΤΗΝ ΠΑΡΑΚΑΤΩ ΕΝΤΟΛΗ ΒΓΑΖΩ ΤΟ ARRAY KAI ΔΙΑΒΑΖΩ ΤΗΝ ΤΙΜΗ.*/
        /*Elegxos an einai IPv6 h IPv4 */
        if (serverIPAddress[0]=="["){
          serverIPAddress=serverIPAddress.substring(1,serverIPAddress.length-1);
        }
        /*4o Debug KOMPLE */
        // console.log(serverIPAddress);
        /*Eisagwgh Stoixeiwn Ston Pinaka*/
        File.insertMany({user_id:req.session.user_id, startedDateTime:startedDateTime, serverIPAddress:serverIPAddress, timings:timings, url:url, method:method, request_headers: request_headers, status:status, statusText:statusText, response_headers:response_headers,user_lat: user_lat, user_lon: user_lon})
            .then(()=>{
              console.log("RANDOM USER  FILES  TABLE 1")
            }).catch((err)=>{
              console.log("QUERY WRONG!");
            })
        /*ΕΔΩ  με την βοηθεια του  geo.ipify και την ServerIPAddress του HAR 
        αρχειου βρισκω τα lantitude-longtitude(πλάτος-μήκος) ΤΟΥ SERVER!!!! ΑΛΛΑ ΚΑΙ ΤΟ ISP ΤΟΥ ΔΗΛΑΔΗ ΤΟΝ ΠΑΡΟΧΟ.*/
        

        var api_key = 'at_O20Q87WMPVvcvLGjS07PNxGkSfTjQ';
        var api_url = 'https://geo.ipify.org/api/v1?';

        var url1  = api_url + 'apiKey=' + api_key + '&ipAddress=' + serverIPAddress;
        var server_long = "";
        var server_lat  = "";
        var user_isp  = "";
        var user_city = "";

        https.get(url1,  function(response) {
            var ipifyresponse = '';
            response.on('data', function(chunk) { ipifyresponse += chunk; });
            response.on('end',  function(){ 
                    //  console.log(str);
                    var parsedipifyresponse = JSON.parse(ipifyresponse);
                    /*ΤΥΠΩΝΩ ΟΛΟ ΤΟ JSON OBJECT*/
                    console.log(parsedipifyresponse); 
                    /*TO JSON OBJECT ΕΧΕΙ  ΣΑΝ KEY IP-LOCATION-ISP-PROXY
                    ΟΜΩΣ ΣΤΟ LOCATION ΥΠΑΡΧΕΙ ΚΑΙ ΑΛΛΟ OBJECT ΟΠΟΤΕ ΘΕΛΕΙ 
                    ΝΑ ΤΟ ΧΕΙΡΙΣΤΩ ΣΑΝ ΔΙΣΔΙΑΣΤΑΤΟ ARRAY.!!!*/         
                    //Για το αλλο ΗΑΡ θέλει
                    //server_long = parsedstr["lng"];
                    //Για το HAR MWRA θέλει 
                    server_long = parsedipifyresponse["location"]["lng"];
                    //Για το αλλο ΗΑΡ θέλει
                    //server_lat  = parsedstr["lat"];
                    //Για το HAR MWRA θέλει 
                    server_lat  = parsedipifyresponse["location"]["lat"];
                    //Για το HAR MWRA θέλει
                    user_city = parsedipifyresponse["location"]["city"];
                    //Για το αλλο ΗΑΡ θέλει
                    //user_city = parsedstr["city"];
                    user_isp  = parsedipifyresponse["isp"];
                    /*5o Debug KOMPLE */
                    console.log(server_long);
                    console.log(server_lat);
                    console.log(user_isp);
                    console.log(user_city);
                    File.insertMany({user_id:req.session.user_id,server_long: server_long, server_lat: server_lat, user_isp: user_isp, user_city: user_city})
                        .then(()=>{
                        console.log("RANDOM USER  FILES  TABLE 2")
                        }).catch((err)=>{
                      console.log("QUERY WRONG!");
                        })
                    File.updateMany({user_id:req.session.user_id,$inc:{"harcount": +1},$set:{"uploaddate": Date.now()}})
                                  .then(()=>{
                                    console.log("RANDOM USER  FILE TABLE  STATISTIKA")
                                  }).catch((err)=>{
                                    console.log("QUERY WRONG!");
                                  })
            /*5o Debug KOMPLE */
             });

        }).end();



    })

  
    
});

module.exports = router;
/*ΦΤΙΑΧΝΩ ΤΑ ΣΤΟΙΧΕΙΑ ΤΟΥ  ΠΙΝΑΚΑΣ REQUEST ΕΧΕΙ ΜΕΣΑ URL METHOD ΑΛΛΑ KAI TA HEADERS ΤΟΥ REQUEST */
        // Request.insertMany({_id:req.session.user_id,url:url,method:method,headers:request_headers})
        //        .then(()=>{
        //            console.log("RANDOM USER INSERT TABLE REQUEST")
        //         }).catch((err)=>{
        //             console.log("QUERY WRONG!");
        //         })
/*ΦΤΙΑΧΝΩ ΤΑ ΣΤΟΙΧΕΙΑ ΤΟΥ  ΠΙΝΑΚΑΣ RESPONSE ΕΧΕΙ ΜΕΣΑ STATUS STATUSTEXT ΑΛΛΑ KAI TA HEADERS ΤΟΥ RESPONSE  */
        // Response.insertMany({_id:req.session.user_id,status:status,statusText:statusText,headers:response_headers})
        //        .then(()=>{
        //             console.log("RANDOM USER INSERT TABLE REQUEST")
        //         }).catch((err)=>{
        //             console.log("QUERY WRONG!");
        //         })
/*ΦΤΙΑΧΝΩ ΤΑ ΣΤΟΙΧΕΙΑ ΤΟΥ  ΠΙΝΑΚΑΣ ENTRIES  ΕΧΕΙ ΜΕΣΑ STARTEDDATETIME SERVERIPADDRESS TIMINGS(WAIT). */
        // Entries.insertMany({_id:req.session.user_id,startedDateTime:startedDateTime, serverIPAddress:serverIPAddress,timings:timings})
        //        .then((request)=>{
        //            console.log("RANDOM USER  ENTRIES TABLE")
        //         }).catch((err)=>{
        //             console.log("QUERY WRONG!");
        //         })
/*ΚΟΜΠΛΕ ΜΕΧΡΙ ΕΔΩ!!!! */

        // User.updateOne({$inc:{"harcount": +1}})
        // .then((user)=>{
        //     console.log("gea");
        // }).catch((err)=>{
        //    console.log("QUERY WRONG!");
        // });
/* */
                    // UserUploadData.updateOne({$inc:{"harcount": +1}})
                    //               .then(()=>{
                    //                 console.log("RANDOM USER  USERUPLOADDATA HAR COUNT TABLE")
                    //               }).catch((err)=>{
                    //                 console.log("QUERY WRONG!");
                    //               })
                    //_id:req.session.user_id,
                    // File.insertMany({_id:req.session.user_id,startedDateTime:startedDateTime, serverIPAddress:serverIPAddress,timings:timings,url:url,method:method,request_headers:request_headers,status:status,statusText:statusText,response_headers:response_headers,userlong:user_long, userlat:user_lat, userisp:user_isp , usercity: user_city,$inc:{"harcount": 1},$set:{"uploaddate":Date.now()}})
                    //               .then(()=>{
                    //                 console.log("RANDOM USER  USERUPLOADDATA TABLE")
                    //               }).catch((err)=>{
                    //                 console.log("QUERY WRONG!");
                    //               })
/* */
        //}
        //$inc:{"useruploadharcount":+1},$set:{"uploaddate":Date.now()}
        // console.log(long);
        //console.log(startedDateTime);
        //console.log(timings);
        //console.log( serverIPAddress);
        // Entries.insertMany({user_id:req.session.user_id,startedDateTime:startedDateTime, serverIPAddress:serverIPAddress,timings:timings})
        //        .then((request)=>{
        //            console.log("RANDOM USER  ENTRIES TABLE")
        //         }).catch((err)=>{
        //             console.log("QUERY WRONG!");
        //         })
        // /*ΦΤΙΑΧΝΩ ΕΝΑ FIELD ΣΤΟ SCHEMA USERS ΑΝΑΛΟΓΑ ΜΕ ΤΑ UPLOADHAR ΠΟΥ ΕΧΕΙ ΚΑΝΕΙ ΚΑΙ ΤΗΝ ΩΡΑ ΠΟΥ ΤΟ ΚΑΝΕΙ */
