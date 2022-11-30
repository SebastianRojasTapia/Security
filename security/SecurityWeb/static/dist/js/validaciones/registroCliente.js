
function validarRut() {
    var rut = document.getElementById("rut").value;
    
    if (rut.trim().length != 10) {
        error("Largo de rut incorrecto, debe tener 10 caraceteres.")
        return false;
    }
    var suma = 0;
    var num = 3;
    for (let index = 0; index < 8; index++) {
        var car = rut.slice(index, index + 1);
        suma = suma + (num * car);
        num = num - 1;
        if (num == 1) {
            num = 7;
        }
    }
    var resto = suma % 11;
    var dv = 11 - resto;
    if (dv > 9) {
        if (dv == 10) {
            dv = 'K';
        } else {
            dv = 0;
        }
    }
    var dv_usuario = rut.slice(-1).toUpperCase();
    if (dv != dv_usuario) {
        error("Rut Invalido.")
        return false;
    } 
    else {
        success("Rut Valido")
        return true;
    }
}

function validarRazonSocial(){
    var a = document.getElementById("razonSocial").value;
    if (a.trim().length > 2 && a.trim().length < 81) {
        return true;
    }
    error("Largo de la Razon social, debe estar entre 3 y 20 caracteres.")

    return false;
}

function validarNumeroContacto(){
    var a = document.getElementById("numeroContacto").value;
    if (a.includes("+569")) {
        if (a.trim().length == 12) {
            return true;
        }
        error("Error en el Número Telefonico.")
        return false;
    }
    error("Debe Incluir +56 9")
    return false;
}

function validarRubro(){
    var a = document.getElementById("rubro").value;
    console.log(a)
    if (a.trim().length > 0) {
        return true;
    }
    error("Debe Ingresar el Rubro de la empresa")

    return false;
}

function validarCorreo() {
    var e = document.getElementById("correo").value;
    if (e.includes("@")) {
        return true;
    } else {
        error("Correo incorrecto, En su correo debe contener un @.")
        return false;
    }
}

function validarContrasenia() {
    var e = document.getElementById("passRegister").value;
    let ValidPasswd = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-8])(?=.*[!@#\$\^&\*])(?=.{8,})/

    if (ValidPasswd.test(e)){
        return true
    }
    else{
        errorContrasenia('<p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 8 Caracteres.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Mayúscula.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Minuscula.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Número.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Caracter Especial.</p>')
        return false
    }

}

function validarCuenta() {
    resp = validarRut();
    if (resp == false){
        return false;
    }
    resp = validarRazonSocial();
    if (resp == false){
        return false;
    }
    resp = validarNumeroContacto();
    if (resp == false){
        return false;
    }
    resp = validarRubro();
    if (resp == false){
        return false;
    }
    resp = validarCorreo();
    if (resp == false){
        return false;
    }
    resp = validarContrasenia();
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
        footer: 'Vuelve a intetarlo.',
        showClass: {
            popup: 'animate__animated animate__fadeInDown'
          },
          hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
          }
      })
}

function errorContrasenia(html){
    Swal.fire({
        icon: 'error',
        title: 'Oops...',
        html: html,
        footer: 'Vuelve a intetarlo.',
        showClass: {
            popup: 'animate__animated animate__fadeInDown'
          },
          hideClass: {
            popup: 'animate__animated animate__fadeOutUp'
          }
      })
}


