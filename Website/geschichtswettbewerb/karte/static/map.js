//create the map centered on muenster
const attribution = '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
const map = L.map('map', {
  center: [51.961748,7.625063],
  minZoom: 2,
  zoom: 14,
});

L.tileLayer('https://{s}.tile.openstreetmap.de/{z}/{x}/{y}.png', { attribution: attribution }).addTo(map);

//add the markers to the map
const markers = JSON.parse(document.getElementById('markers-data').textContent);

let feature = L.geoJSON(markers).bindPopup(function (layer)
{ return layer.feature.properties.ortbezeichnung + ' <a href="' + layer.feature.properties.pk + '" target="_blank">' + 'Detailansicht</a>';
});
map.addLayer(feature);
