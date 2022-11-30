
function validarNumeroContacto(){
    var a = document.getElementById("telefono").value;
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

function validarContrasenia() {
    var e = document.getElementById("password").value;
    let ValidPasswd = /(?=.*[a-z])(?=.*[A-Z])(?=.*[0-8])(?=.*[!@#\$\^&\*])(?=.{8,})/

    if (e.trim().length == 0){
        return true
    }
    else{
        
        if (ValidPasswd.test(e)){
            return true
        }
        else{
            errorContrasenia('<p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 8 Caracteres.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Mayúscula.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Minuscula.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Número.</p><p class="mb-2 text-danger text-left ml-4"><i class="fa-solid fa-xmark"></i> Debe contener al menos 1 Caracter Especial.</p>')
            return false
        }
    }

}

function validarModificacionPerfil() {

    resp = validarContrasenia();
    if (resp == false){
        return false;
    }

    resp = validarNumeroContacto();
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


