var menuHolder = document.getElementById('menuHolder')
var siteBrand = document.getElementById('siteBrand')
function menuToggle() {
    if (menuHolder.className === "drawMenu") menuHolder.className = ""
    else menuHolder.className = "drawMenu"
}
if (window.innerWidth < 426) siteBrand.innerHTML = "NF"
window.onresize = function () {
    if (window.innerWidth < 420) siteBrand.innerHTML = "NF"
    else siteBrand.innerHTML = "NOTICIAS INFORMATORIO"
}

$(document).ready(function () {
    var apiKey = '1606c1d329b643f6bbc60107232312';
    var ciudad = 'Resistencia';
    var url = 'http://api.weatherapi.com/v1/current.json?key=' + apiKey + '&q=' + ciudad;

    $.ajax({
        url: url,
        method: 'GET',
        success: function (data) {
            $('#clima').html(ciudad + ': ' + data.current.temp_c + '°C ');
            $('#condicion-icono').html('<img src="' + data.current.condition.icon + '" alt="Icono del tiempo">');
        },
        error: function (error) {
            console.log('Error: ', error);
        }
    });
});