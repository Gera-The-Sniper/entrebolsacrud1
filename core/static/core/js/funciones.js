function confirmar2(){
    if (!confirm('¿Desea eliminar el producto?')) {
        alert("El producto no ha sido borrado")
        
      }
    else{
        alert("El producto ha sido borrado exitosamente")
    }
}

function filtro()
{
var tecla = event.key;
if (['.','e','-'].includes(tecla))
   event.preventDefault()
}


function confirmar(valor) {
    Swal.fire({
        "title":"¿Seguro desea eliminarlo?",
        "icon":"warning",
        "showCancelButton":true,
        "cancelButtonText":"No, cancelar",
        "confirmButtonText":"Sí, eliminar",
        "reverseButtons":true
    })
    .then(function(result) {
        if (result.isConfirmed) {
            window.location.href="eliminar1/"+valor

        }
    })
}