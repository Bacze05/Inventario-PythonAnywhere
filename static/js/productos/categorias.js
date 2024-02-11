// var $ = jQuery.noConflict();

function listarCategorias() {
    // Obtener el nombre de la categoría de la URL
    var nombre = window.location.pathname.split('/').filter(Boolean).pop();


    $.ajax({
        url: `/categorias1/`,
        type: "get",
        dataType: "json",
        success: function (response) {
            $('#tabla_categorias tbody').html("");
            for(let i = 0;i < response.length;i++){
                let fila = '<tr>';
                fila += '<td>' + response[i]["fields"]['name']+'</td>';
                fila += '<td>' + response[i]["fields"]['descripcion'] + '</td>';
                fila += '<td>' + response[i]["fields"]['foto'] + '</td>';
                // Construir la URL dinámicamente utilizando el nombre de la categoría
                const nombreCategoria = response[i]["fields"]['name'];
                const url = `/categorias/list/${nombreCategoria}/`;
                fila += `<td><a href="${url}" class="btn btn-primary">Ver Listado</a></td>`;
                fila += '<td><a href="/categorias/edit/' + response[i]["pk"] + '" class="btn btn-primary"  >Editar </a> <a href="/categorias/eliminado/' + response[i]["pk"] + '" class="btn btn-danger"  >Eliminar </a></td>';
                fila += '</tr>';
                $('#tabla_categorias tbody').append(fila);
            }
            $('#tabla_categorias').DataTable({
                language: {
                    decimal: "",
                    emptyTable: "No hay información",
                    info: "Mostrando START a END de TOTAL Entradas",
                    infoEmpty: "Mostrando 0 to 0 of 0 Entradas",
                    infoFiltered: "(Filtrado de MAX total entradas)",
                    infoPostFix: "",
                    thousands: ",",
                    lengthMenu: "Mostrar MENU Entradas",
                    loadingRecords: "Cargando...",
                    processing: "Procesando...",
                    search: "Buscar:",
                    zeroRecords: "Sin resultados encontrados",
                    paginate: {
                      first: "Primero",
                      last: "Ultimo",
                      next: "Siguiente",
                      previous: "Anterior",
                    },
                  },
                  
                pageLength: 6,
                columnDefs: [
                    { targets: [ 1,2, 3,4], searchable: false ,
                    } ,
                    {
                        "targets": 2, // Índice de la columna que contiene los enlaces de las fotos
                        "render": function(data, type, row) {
                            return '<img src="' + data + '" alt="Foto">';
                        }
                    } // Desactiva la búsqueda para las columnas 0, 2 y 3
                ],
            });
        },
        error: function (error) {
            console.error("Error al obtener productos:", error.responseText);
        }
    });
}


$(document).ready(function () {
    
    listarCategorias();
    
});
