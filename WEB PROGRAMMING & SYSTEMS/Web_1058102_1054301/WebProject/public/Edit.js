
/*Εδώ AJAX για τα ΣΤΑΤΙΣΤΙΚΑ ΔΕΔΟΜΕΝΑ.!!!!!! */
const request1 = $.ajax({
    url:"/Edit/Data",
    type:"GET",
    contentType:"application/json",
    dataType:"json",
    //cache:false,
    //processData:false,
    success:function(response){
        //var data = JSON.stringify(response);
        console.log(response)
        $('#HARCOUNT').html('Ο χρήστης έχει υποβάλει ' +response["server_data"][0]["harcount"]+ '  HAR Αρχεία.')
        $('#UPLOADDATE').html('Ο χρήστης έκανε αυτή την ημερομηνία   ' +response["server_data"][0]["uploaddate"]+ ' τελεύταιο upload.')
        $('#COUNT').html('Οι εγγραφές του χρήστη είναι ' +response["count"])
    }         
});

// /*Εδώ AJAX για τo HEATMAP.!!!!!! */
// const request2 = $.ajax({
//     url:"/Edit/Data",
//     type:"GET",
//     contentType:"application/json",
//     dataType:"json"
//     // success:function(response){
        
//     //     // server_lat = response["server_data"][1]["server_lat"];
//     //     var latlongs = response["server_data"].map(function (element){
//     //         return {"lat": element["server_lat"], "long": element["server_long"]}
//     //     })
//     // }
// });
// request2.done(UserHeatmap);




/* EDIT ΟΙ ΠΑΡΑΚΑΤΩ ΣΥΝΑΡΤΗΣΕΙΣ ΕΙΝΑΙ ΓΙΑ ΤΟ ΠΡΩΤΟ ΜΕΡΟΣ ΤΟΥ ΕΡΩΤΗΜΑΤΟΣ 3. */
function EditUser(){
    var username = document.getElementById("username").value;
    var password = document.getElementById("password").value;
    if(username == ""){
        alert("Πρέπει να βάλετε όνομα για τον χρήστη");
        return ;
    }
    if(password == ""){
        alert("Πρέπει να βάλετε κωδικό για τον χρήστη");
        return ;
    }
    
    if(!passwordEditUser(password)){
        return request.function(response);
    }
    $("#EditUser").on("submit", function(event){
        event.preventDefault();
        console.log("Username: "+username+ "Password: " + password);
        const request = $.ajax({
            url:"/Edit",
            method:"POST",
            contentType:"application/json",
            data: JSON.stringify({username: username, password: password}),
            // success:function(response){
            //     if(response.redirect == "/"){
            //         alert("Αλλάξατε επιτυχώς τα στοιχεία του χρήστη σας");
            //         window.location = response.redirect
            //     } 
            // },
            // error: function(response) {
            //     if(response.redirect == "/Edit")
            //     {
            //         alert("Δεν υποβάλατε σωστά στοιχεία παρακαλώ ξανά προσπαθήστε");
            //         window.location = response.redirect
            //     }
            // } 
            
            // success:function(response){
            //     if(response.redirect == "/"){
            //         alert("Αλλάξατε επιτυχώς τα στοιχεία του χρήστη σας");
            //         window.location = response.redirect
            //     } 
            //     else if(response.redirect == "/Edit")
            //     {
            //         alert("Δεν υποβάλατε σωστά στοιχεία παρακαλώ ξανά προσπαθήστε");
            //         window.location = response.redirect
            //     }
            // }           
        });
        request.done(Success);
    })


}
//Συνάρτηση PASSWORD EDIT USER
function passwordEditUser(pass){
    var mistakes = [];//Δηλώνω ένα άδειο array 
    if (pass.search(/[A-Z]/)< 0){
        mistakes.push("Ο κωδικός πρέπει να περιέχει τουλάχιστον ένα κεφαλαίο γράμμα.\n");
    }
    if (pass.search(/[0-9]/)< 0){
        mistakes.push("Ο κωδικός πρέπει να περιέχει τουλάχιστον έναν αριθμό.\n");
    }
    if (pass.length < 8){
        mistakes.push("Ο κωδικός πρέπει να είναι τουλάχιστον 8 χαρακτήρες.\n");
    }
    if (pass.search(/[\\!\\@\\#\\$\\%\\^\\&\\*\\(\\)\\-\\+\\.\\;\\,\\:\\_]/) <  0  ){
        mistakes.push("Ο κωδικός πρέπει να περιέχει τουλάχιστον ένα σύμβολο (π.χ #$*&@)\n");
    }
    if (mistakes.length > 0){
        alert(mistakes.join(" "));
        return false;
    }
    return true;
}

function Success(response){
        if(response.redirect == "/"){
            alert("Αλλάξατε επιτυχώς τα στοιχεία του χρήστη σας");
            window.location = response.redirect
        } 
        else if(response.redirect == "/Edit")
        {
            alert("Δεν υποβάλατε σωστά στοιχεία παρακαλώ ξανά προσπαθήστε");
            window.location = response.redirect
        }
}






// function UserHeatmap(response){
//     var latlongs = response["server_data"].map(function (element){
//         return {"lat": parseFloat(element["server_lat"]), "long": parseFloat(element["server_long"]), "count": 1}
//     })
//     var heatmapdata = {max:latlongs.length, data:latlongs[1]};
//     console.log(heatmapdata);
//     // $('#HEATMAP1').html('');
// 	// $('<div id = "HEATMAP2" style="width:100px; height: 100px;"></div>').appendTo($("#HEATMAP1"));
// 	//var map = new  L.map('HEATMAP2');
// 	// var baseLayer = L.tileLayer('http://{s}.tile.osm.org/{z}/{x}/{y}.png', {
// 	// 	attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors'
// 	// }).addTo(map);
//     var baseLayer = L.tileLayer(
//         'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
//           attribution: 'Map data &copy; <a href="http://openstreetmap.org">OpenStreetMap</a> contributors, <a href="http://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, Imagery © <a href="http://cloudmade.com">CloudMade</a>',
//           maxZoom: 18
//         }
//       );
// 	//map.setView([38.2462420, 21.7350847], 1);
// 	// var drawnItems = new L.FeatureGroup();
// 	// map.addLayer(drawnItems);
//     // var baseLayer = L.tileLayer(
//     //     'http://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png',{
//     //         attribution: '&copy; <a href="http://osm.org/copyright">OpenStreetMap</a> contributors',
//     //       maxZoom:5
//     //     }
//     //   );
//     // var baseLayer = L.tileLayer(
//     // 'https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw',{
//     //     attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
//     //     '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
//     //     'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
//     //     maxZoom: 18,
//     //     id:'mapbox.streets'
//     // }
//     // );

// 	var testData = {
// 		max: 100,
// 		data: response
// 	};
// 	var cfg = {
// 		"radius": 40,
// 		"max_opacity": 0.8,
// 		"scaleRadius": false,
// 		"useLocalExtrema": false,
// 		latField: 'lat',
// 		lngField: 'long',
// 		valueField: 'count'
// 	};
//     //heatmapLayer = new (window as any).HeatmapOverlay(this.cfg);
//     // var heatmapLayer = new HeatmapOverlay(cfg);
//     var heatmapLayer = new HeatmapOverlay(cfg);

//     // var map = new L.Map('HEATMAP2', {
//     //     center: new L.LatLng(25.6586, -80.3568),
//     //     zoom: 4,
//     //     layers: [baseLayer, heatmapLayer]
//     //   });
//     var map = new L.Map('HEATMAP2', {
//         center: new L.LatLng(25.6586, -80.3568),
//         zoom: 4,
//         layers: [baseLayer, heatmapLayer]
//       });
//     map.addLayer(heatmapLayer);
//     heatmapLayer.setData(testData);
//     // var map = new L.map('HEATMAP2', {
//     //     center: new L.LatLng(25.6586, -80.3568),
//     //     zoom: 4,
//     //     layers: [baseLayer, heatmapLayer]
//     //   }); 
// 	// heatmapLayer.setData(heatmapdata);
// }



















