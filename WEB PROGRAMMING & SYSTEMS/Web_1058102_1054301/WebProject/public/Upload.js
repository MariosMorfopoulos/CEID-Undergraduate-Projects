
// const { $where } = require("../models/User");

// const { request } = require("express");

var dedomena = {};//Ορίζω 'dedomena' ως κενό  αντικείμενο  

function FileUpload(){
    var File_Input = document.getElementById("FileChosen");//Εδω ορίζω το File_Input να ειναι το ιδιο με το id της HTML
    if(File_Input.files.length == 0){
        alert("Πρέπει να επιλέξετε ένα Αρχείο");//Αν ειναι 0 δεν εχω επιλεξει αρχειο HAR
    }
    else{
        var Reader  = new FileReader();//Διαβασμα Αρχειου
        var newinfo = [];//Kenos pinakas
        var json = "";
        Reader.onload = function(event){
            json = event.target.result;
        }
        Reader.onloadend = function () {
            var result = JSON.parse(json);//HAR arxeio se JSON OBJECT
            //Gia kathe log kai entrie kalo thn FROMJSON
            result.log.entries.forEach(function(entry){
                const url_text = entry.request.url;
                let domain = (new URL(url_text));
                var requestheader = CreateHeaders(entry.request.headers);
                var responseheader = CreateHeaders(entry.response.headers);
                var request = {method: entry.request.method, url:domain.hostname,headers:requestheader};
                var response = {status: entry.response.status, statustext:entry.response.statusText, headers:responseheader};
                let newentry = {request: request , response:response, timings:entry.timings.wait, serveripaddress: entry.serverIPAddress, startedDateTime: entry.startedDateTime, user_lat: user_lat, user_lon: user_lon};
                
                newinfo.push(newentry);
                
            });
            //AJAX!!!!!!!
            var dedomena = new FormData();
            dedomena.append('info',JSON.stringify(newinfo));
            $.ajax({
                type:"post",
                url:"/Upload",
                dataType:"json",
                data: JSON.stringify({'info':newinfo.map(JSON.stringify)}),//Edw mporei na thelei anallages
                cache:false,
                contentType:'application/json',
                processData: false,
                // success: function(response){
                //     console.log(dedomena);
                // }
            });
            // console.log(newinfo);        
        }
        //console.log(json);
        //console.log(responseheader);
        //console.log(dedomena);
        console.log(newinfo);
        Reader.readAsText(File_Input.files[0], "UTF-8");
        console.log(dedomena['info']);

        console.log(JSON.stringify(newinfo));
        console.log(JSON.stringify({'info':newinfo.map(JSON.stringify)}))
        var text =  JSON.stringify({'info':newinfo.map(JSON.stringify)})
        var data = new Blob([text], { type: "application/json" });
        var url = window.URL.createObjectURL(data);
        document.getElementById("download_link").href = url;
    }
}
/*Gia to USER_LAT USER_LONG */
if ("geolocation" in navigator) {
    console.log("geolocation available");
    navigator.geolocation.getCurrentPosition(async (position) => {
      user_lat = position.coords.latitude;
      user_lon = position.coords.longitude;
      console.log(user_lat);
      console.log(user_lon);
    });
}
// console.log(newinfo);
//code to download the file as a link into our computer



function CreateHeaders(headers){
    let NewHeaders = {
        content_type: null,
        cache_control: null,
        pragma: null,
        expires: null,
        age: null,
        last_modified: null,
        host: null
    };
    for(var header of headers){
        if(header.name.toLowerCase() === "content-type"){
            NewHeaders.content_type = header.value;
        }
        else if(header.name.toLowerCase() === "cache-control"){
            NewHeaders.cache_control = header.value;
        }
        else if(header.name.toLowerCase() === "pragma"){
            NewHeaders.pragma = header.value;
        }
        else if(header.name.toLowerCase() === "expires"){
            NewHeaders.expires = header.value;
        }
        else if(header.name.toLowerCase() === "age"){
            NewHeaders.age = header.value;
        }
        else if(header.name.toLowerCase() === "last-modified"){
            NewHeaders.last_modified = header.value;
        }
        else if(header.name.toLowerCase() === "host"){
            NewHeaders.host = header.value;
        }
    }
    if(NewHeaders.content_type == null && NewHeaders.cache_control == null && NewHeaders.pragma == null &&
    NewHeaders.expires == null && NewHeaders.age == null && NewHeaders.last_modified == null && NewHeaders.host == null ){
        return null;
    }
    return NewHeaders;
}