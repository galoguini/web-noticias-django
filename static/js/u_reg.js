$(document).ready(function() {
    console.log("El documento está listo");

    $('#terms').change(function () {
        $('#verificar').prop('disabled', !this.checked);
    });

    $('#siguiente').click(function() {
        console.log("Se hizo clic en el botón Siguiente");
        $('#paso1').hide();
        $('#paso2').show();
        $('#siguiente').hide();
        $('#anterior').show();
        $('#verificar').show();
    });

    $('#anterior').click(function() {
        console.log("Se hizo clic en el botón Anterior");
        $('#paso1').show();
        $('#paso2').hide();
        $('#siguiente').show();
        $('#anterior').hide();
        $('#verificar').hide();
    });
});