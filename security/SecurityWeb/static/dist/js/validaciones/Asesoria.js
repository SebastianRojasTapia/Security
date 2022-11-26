
var descripcion = document.getElementById('descripcion');
var direccion = document.getElementById('direccion');
var cant_asist = document.getElementById('cant_asistentes');
var fecha_inicio = document.getElementById('fecha_inicio');
var fecha_termino = document.getElementById('fecha_termino');
var hora_inicio = document.getElementById('hora_inicio');
var hora_termino = document.getElementById('hora_termino');

function limpiar(){
    descripcion.value = "";
    direccion.value = "";
    cant_asist.value = "";
    fecha_inicio.value = "";
    fecha_termino.value = "";
    hora_inicio.value = "";
    hora_termino.value = "";
}

function carg(elemento) {
    d = elemento.value;

    if(d == "1"){ 
        descripcion.disabled = false;
        cant_asist.disabled = true;
        direccion.disabled = false;
        fecha_inicio.disabled = false;
        fecha_termino.disabled = false;
        hora_inicio.disabled = false;
        hora_termino.disabled = false;
    }
    else if(d == "2"){
        descripcion.disabled = false;
        direccion.disabled = true;
        cant_asist.disabled = true;
        fecha_inicio.disabled = true;
        fecha_termino.disabled = true;
        hora_inicio.disabled = true;
        hora_termino.disabled = true;
    }
    else if(d == "3"){
        descripcion.disabled = false;
        direccion.disabled = false;
        cant_asist.disabled = false;
        fecha_inicio.disabled = false;
        fecha_termino.disabled = false;
        hora_inicio.disabled = false;
        hora_termino.disabled = false;
    }
    else if(d == "4"){
        descripcion.disabled = false;
        direccion.disabled = false;
        cant_asist.disabled = true;
        fecha_inicio.disabled = false;
        fecha_termino.disabled = true;
        hora_inicio.disabled = true;
        hora_termino.disabled = true;
    }
    else if(d == "5"){
        descripcion.disabled = false;
        direccion.disabled = true;
        cant_asist.disabled = true;
        fecha_inicio.disabled = true;
        fecha_termino.disabled = true;
        hora_inicio.disabled = true;
        hora_termino.disabled = true;
    }

limpiar()

}

function validarDescripcion() {
    var a = document.getElementById("descripcion").value;
    if (a.trim().length > 9 && a.trim().length < 101) {
        return true;
    }
    error("Largo de la Descripcion, debe estar entre 10 y 100 caracteres.")
    return false;

}

function validarFechaInicio() {

    var d = document.getElementById("tip_asesoria").value;

    if(d == "1"){ 
        var fecha_inicio =  new Date(document.getElementById("fecha_inicio").value);
        var fecha_termino = new Date(document.getElementById("fecha_termino").value);
        var ahora = new Date()
        
        if(fecha_inicio <= fecha_termino){
            if (ahora < fecha_inicio){

                if (fecha_inicio.setDate(fecha_inicio.getDate() + 3) >= fecha_termino){
                    return true
                }
                else{
                    var fecha = new Date()
                    fecha.setDate(fecha_inicio.getDate() + 1)
                    errorFecha("Solo se puede Extender la Capacitacion 3 Dias. Menor o igual a esta fecha. " + fecha.toLocaleDateString() + " Incluye los fines de semana.")
                    return false;
                }
            }
            else{
                ahora.setDate(ahora.getDate() + 15)
                errorFecha("Para agendar la capacitacion debe tener 15 Dias de anticipacion a la fecha Actual. Desde el día " + ahora.toLocaleDateString() + " puede agendar.")
                return false;
            }

        }
        errorFecha("La Fecha Termino debe ser mayor a la Fecha Inicio.")
        return false;
    }

    if(d == "3"){ 
        var fecha_inicio =  new Date(document.getElementById("fecha_inicio").value);
        var fecha_termino = new Date(document.getElementById("fecha_termino").value);
        var ahora = new Date()
        
        if(fecha_inicio <= fecha_termino){
            if (ahora < fecha_inicio){

                if (fecha_inicio.setDate(fecha_inicio.getDate() + 3) >= fecha_termino){
                    return true
                }
                else{
                    var fecha = new Date()
                    fecha.setDate(fecha_inicio.getDate() + 1)
                    errorFecha("Solo se puede Extender la Capacitacion 3 Dias. Menor o igual a esta fecha. " + fecha.toLocaleDateString() + " Incluye los fines de semana.")
                    return false;
                }
            }
            else{
                ahora.setDate(ahora.getDate() + 15)
                errorFecha("Para agendar la capacitacion debe tener 15 Dias de anticipacion a la fecha Actual. Desde el día " + ahora.toLocaleDateString() + " puede agendar.")
                return false;
            }

        }
        errorFecha("La Fecha Termino debe ser mayor a la Fecha Inicio.")
        return false;
    }
    
}

function validarHora() {
    var d = document.getElementById("tip_asesoria").value;

    if(d == "1"){ 
        var hora_inicio =  document.getElementById("hora_inicio").value;
        var hora_termino = document.getElementById("hora_termino").value;

        if(hora_inicio <= hora_termino){
            if (hora_inicio === hora_termino){
                errorFecha("Las Hora tomadas son iguales. Cambien las Horas en el rango establecido.")
                return false;
            }
            else{
                return true
            }
        }

        else{
            errorFecha("La Hora de Termino debe ser mayor a la Hora de Inicio.")
            return false;
        }
        
    }

    if(d == "3"){ 
        var hora_inicio =  document.getElementById("hora_inicio").value;
        var hora_termino = document.getElementById("hora_termino").value;

        if(hora_inicio <= hora_termino){
            if (hora_inicio == hora_termino){
                errorFecha("Las Hora tomadas son iguales. Cambien las Horas en el rango establecido.")
                return false;
            }
            else{
                return true
            }
        }

        else{
            errorFecha("La Hora de Termino debe ser mayor a la Hora de Inicio.")
            return false;
        }
    }
}

function validarAsistentes() {
    var a = document.getElementById("cant_asistentes").value;
    if (a >= 5 && a <= 50) {
        return true;
    }
    error("La cantidad de asistentes por capacitación son entre 5 a 50 personas.")
    return false;
}

function validarDireccion() {
    var a = document.getElementById("direccion").value;
    if (a.trim().length >= 5 && a.trim().length <= 100) {
        return true;
    }
    error("Largo de la Descripcion, debe estar entre 5 y 100 caracteres.")
    return false;

}

function validarAsesoria() {
    resp = validarDescripcion();
    if (resp == false){
        return false;
    }

    resp = validarFechaInicio();

    if (resp == false){
        return false;
    }

    resp = validarHora();
    if (resp == false){
        return false;
    }

    resp = validarAsistentes();
    if (resp == false){
        return false;
    }

    resp = validarDireccion();
    if (resp == false){
        return false;
    }
    
}

function success(menssaje){
    Swal.fire({
        icon: 'success',
        text: menssaje,
        showClass: {
            popup: 'animate__animated animate__fadeInDown'
          },
          hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
          }
      })
}

function error(menssaje){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: menssaje,
        timer: 2500,
        footer: 'Vuelve a intetarlo.',
        showClass: {
            popup: 'animate__animated animate__fadeInDown'
          },
          hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
          }
      })
}

function errorFecha(menssaje){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: menssaje,
        footer: 'Vuelve a intetarlo.',
        showClass: {
            popup: 'animate__animated animate__fadeInDown'
          },
          hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
          }
      })
}



