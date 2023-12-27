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

document.getElementById('foto').addEventListener('change', checkFile);
document.querySelector('.btn-warning').addEventListener('click', function() {
    document.getElementById('foto').click();
});

function checkFile() {
    var fileInput = document.getElementById('foto');
    var submitButton = document.getElementById('submitFoto');

    if (fileInput.value == '') {
        submitButton.disabled = true;
    } else {
        submitButton.disabled = false;
    }
}

document.getElementById('botonCancelar').addEventListener('click', mostrarEtapa1);
document.getElementById('botonEditar').addEventListener('click', mostrarEtapa2);
document.getElementById('editarFoto').addEventListener('click', mostrarFotoEtapa2);
document.getElementById('cancelar').addEventListener('click', mostrarFotoEtapa1);

function mostrarFotoEtapa1() {
    document.getElementById('etapa1').style.display = 'block';
    document.getElementById('etapa2').style.display = 'none';
}

function mostrarFotoEtapa2() {
    document.getElementById('etapa1').style.display = 'none';
    document.getElementById('etapa2').style.display = 'block';
}

function mostrarEtapa1() {
    document.getElementById('infoEtapa1').style.display = 'block';
    document.getElementById('infoEtapa2').style.display = 'none';
}

function mostrarEtapa2() {
    document.getElementById('infoEtapa1').style.display = 'none';
    document.getElementById('infoEtapa2').style.display = 'block';
}