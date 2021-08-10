const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {
  center: [51.961748,7.625063],
  minZoom: 2,
  zoom: 14,
});

L.tileLayer('https://geo.stadt-muenster.de/basiskarte/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);
//https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png
//https://geo.stadt-muenster.de/basiskarte/{z}/{x}/{y}.png
const markers = JSON.parse(document.getElementById('markers-data').textContent);

let feature = L.geoJSON(markers).bindPopup(function (layer)
{ return layer.feature.properties.ortbezeichnung + ' <a href="' + layer.feature.properties.pk + '" target="_blank">' + 'Detailansicht</a>';
});//.addTo(map);
map.addLayer(feature);

//map.fitBounds(feature.getBounds(), { padding: [100, 100] });

//map.fitWorld();
//map.setView(center: [51.94986285, 7.60407079384229], zoom: 10);
//map.panTo(L.latLng(51.94986285, 7.60407079384229));
//{{ markers|json_script:"markers-data" }}

//    <script src="{% static 'leaflet.mapcluster.js' %}"></script>
//{{ ort.location.y }}, {{ ort.location.x }}
//{{ ort.location.y }}, {{ ort.location.x }}
