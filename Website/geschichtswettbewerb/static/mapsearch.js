const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {
  center: [51.94986285, 7.60407079384229],
  minZoom: 4,
  zoom: 12,
});

L.tileLayer('https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);

const markers = JSON.parse(document.getElementById('markers-data').textContent);

var clusters = L.markerClusterGroup();
var searchLayer = new L.LayerGroup();
var feature = L.geoJSON(markers).bindPopup(function (layer)
{ return layer.feature.properties.ortbezeichnung + ' <a href="' + layer.feature.properties.pk + '" target="_blank">' + 'Detailansicht</a>';
}).addTo(searchLayer);
//clusters.addLayer(feature);
map.addLayer(searchLayer);

map.addControl(new L.Contol.Search({layer: searchLayer}));
map.addLayer(clusters);

map.fitBounds(feature.getBounds(), { padding: [100, 100] });

map.fitWorld();
//  {{ markers|json_script:"markers-data" }}
