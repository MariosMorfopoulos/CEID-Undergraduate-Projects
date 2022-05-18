/*Εδώ AJAX για τo HEATMAP.!!!!!! */
const request2 = $.ajax({
    url:"/Edit/Data",
    type:"GET",
    contentType:"application/json",
    dataType:"json"

});
request2.done(UserHeatmap);




function UserHeatmap(response){
var latlongs = response["server_data"].map(function (element){
    //console.log(element);
	return [parseFloat(element["server_lat"]),parseFloat(element["server_long"])];
	//return {"lat": parseFloat(element["server_lat"]), "long": parseFloat(element["server_long"]), "count": "1"}
	
}).filter((latlong) => !isNaN(latlong[0]))


console.log(latlongs);

var map = new L.Map('leaflet', {
	layers: [
		new L.TileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
			'attribution': 'Map data © <a href="http://openstreetmap.org">OpenStreetMap</a> contributors'
		})
	],
	center: [52.352, 4.9392],
	zoom: 12
});

// var poutsa = latlongs.forEach(element => 
// 	L.marker(element).addTo(map)
// );


var heat = L.heatLayer(
	//[[52.352, 4.9392, 14],[ 38.246242,21.735085], [38.323343,21.865082],[38.34381,21.57074],[38.108628,21.502075],[38.123034,21.917725]],
    latlongs,
    //heatmapdata,
	{radius: 40},
	//0.4: 'green', 0.65: 'lime',
	{0.4: 'green', 0.65: 'lime',1: 'red'},
	{minOpacity: 0.4,maxOpacity: 0.8}
).addTo(map);

}