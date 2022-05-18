async function getData() {
  const response = await fetch("/morf_map/1");
  const data = await response.json();
  const response1 = await fetch("/morf_map/2");
  const data1 = await response1.json();
  const response2 = await fetch("/morf_map/3");
  const data2 = await response2.json();
  const response3 = await fetch("/morf_map/4");
  const data3 = await response3.json();
  console.log(data1);
  console.log(data3);
  // Making a map and tiles
  const mymap = L.map("mapid").setView([0, 0], 1);
  const attribution =
    '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors';

  const tileUrl = "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png";
  const tiles = L.tileLayer(tileUrl, { attribution });
  tiles.addTo(mymap);
  // console.log(data1[0][0]);
  // console.log(data2.length);
  let data4 = [];
  let counters = [];
  for (let n = 0; n < data3.length; n++) {
  for (let j = 0; j < data1.length; j++) {
    for (let k = 0; k < data2.length; k++) {
      let counter = 0;
      for (let i = 0; i < data.length; i++) {
        lat = data[i].lat;
        lon = data[i].lon;
        server_ll = data[i].server_ll;
        if (
          lat == data1[j] &&
          lon == data3[n] &&
          server_ll[0] == data2[k][0] &&
          server_ll[1] == data2[k][1]
        ) {
          console.log(lat);
          console.log(lon);
          console.log(server_ll);
          counter++;
          var map = {
            lat: lat,
            lon: lon,
            server_ll: server_ll,
            counter: counter,
          };
        } else {
          console.log("geaa");
        }
      }
      data4.push(map);
      counters.push(counter);
    }
  }
}
  console.log(data4);
  console.log(counters);
  max = Math.max(...counters);
  console.log(max);
  for (let i = 0; i < data4.length; i++) {
    lat = data4[i].lat;
    lon = data4[i].lon;
    server_ll = data4[i].server_ll;
    counter = (max - data4[i].counter) / max;
    marker1 = new L.marker([lat, lon]).addTo(mymap);
    marker2 = new L.marker([server_ll[0], server_ll[1]]).addTo(mymap);

    var latlngs = Array();

    //Get latlng from first marker
    latlngs.push(marker1.getLatLng());

    //Get latlng from first marker
    latlngs.push(marker2.getLatLng());

    //From documentation http://leafletjs.com/reference.html#polyline
    var polyline = L.polyline(latlngs, {
      color: "red",
      weight: counter,
    }).addTo(mymap);

    // // zoom the map to the polyline
    mymap.fitBounds(polyline.getBounds());
  }
  //console.log(data2);
}
getData();
