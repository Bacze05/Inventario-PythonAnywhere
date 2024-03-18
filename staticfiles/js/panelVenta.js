// Inicializa DataTables para las dos tablas fuera de las funciones
$(document).ready(function () {
  // Limpia las tablas al cargar la página
  limpiarTabla("#tabla_venta tbody");
  limpiarTabla("#tabla_subtotal tbody");

  // Agrega un event listener para el evento keydown en el campo de código de barras
  $("#bar_code").on("keydown", function (event) {
    // Verifica si la tecla presionada es Enter
    if (event.key === "Enter") {
      event.preventDefault(); // Previene el comportamiento por defecto de la tecla Enter
      listarVentaProductos(); // Llama a la función para listar los productos de venta
      listarVentaDetalle();   // Llama a la función para listar los detalles de venta
    }
  });

  // Agrega un event listener para el evento submit del formulario de venta
  $("#formularioVenta").on("submit", function(event) {
    event.preventDefault(); // Previene el comportamiento por defecto de enviar el formulario
    enviarVenta();           // Llama a la función para enviar la venta
  });
});

// Función para limpiar una tabla
function limpiarTabla(tabla) {
  $(tabla).html(""); // Limpia el contenido HTML de la tabla especificada
}

// Función para mostrar un mensaje en la página
function mostrarMensaje(mensaje) {
  $("#mensaje")                 // Selecciona el elemento con el id 'mensaje'
    .text(mensaje)              // Establece el texto del mensaje
    .fadeIn()                   // Hace aparecer gradualmente el elemento
    .delay(3000)                // Espera 3 segundos
    .fadeOut();                 // Hace desaparecer gradualmente el elemento
}

function listarVentaProductos() {
  var bar_code = $("#bar_code").val();
  $.ajax({
    url: "/venta/listaVenta/",
    type: "get",
    data: { bar_code: bar_code },
    dataType: "json",
    success: function (response) {
      console.log("Respuesta del servidor:", response); // Agregar este console.log para depurar
      if (response.length > 0) {
        response.forEach(function (producto) {
          console.log("Producto:", producto); // Agregar este console.log para depurar
          agregarFila("#tabla_venta tbody", producto, false);
        });
        $("#bar_code").val("");
      } else {
        mostrarMensaje("Código de barras no encontrado.");
        $("#bar_code").val("");
      }
    },
    error: function (error) {
      console.error("Error al obtener productos:", error.responseText);
    },
  });
}

// Función para listar los detalles de venta
function listarVentaDetalle() {
  var bar_code = $("#bar_code").val();  // Obtiene el código de barras ingresado
  $.ajax({
    url: "/venta/listaVenta/",          // URL del endpoint para obtener los detalles de venta
    type: "get",                        // Tipo de petición HTTP
    data: { bar_code: bar_code },       // Datos enviados con la petición
    dataType: "json",                   // Tipo de datos esperados en la respuesta
    success: function (response) {      // Función que se ejecuta si la petición es exitosa
      if (response.length > 0) {        // Verifica si se recibieron detalles de venta
        response.forEach(function (producto) {
          agregarFila("#tabla_subtotal tbody", producto, true);  // Agrega cada detalle de venta a la tabla de subtotal
        });
        $("#bar_code").val("");         // Limpia el campo de código de barras después de listar los detalles de venta
      } else {
        mostrarMensaje("Código de barras no encontrado.");  // Muestra un mensaje si el código de barras no existe
      }
    },
    error: function (error) {           // Función que se ejecuta si hay un error en la petición
      console.error("Error al obtener productos:", error.responseText);  // Muestra el error en la consola del navegador
    },
  });
}

// Función para actualizar el total de la venta
function actualizarTotal() {
  var total = 0;
  // Itera sobre las filas de la tabla de subtotales y suma los valores
  $("#tabla_subtotal tbody tr").each(function () {
    var subtotal = parseFloat($(this).find("td.subtotal").text().replace("$", "").trim());
    total += isNaN(subtotal) ? 0 : subtotal;
  });
  // Actualiza el valor en el elemento totalCalculadora
  $("#totalCalculadora").text(total.toFixed(0)); // Puedes ajustar el número de decimales según tu necesidad
}

// Lista para almacenar los productos agregados
var productos = [];

// Función para agregar una fila a una tabla
function agregarFila(tabla, producto, esSubtotal) {
  var cantidad = 1; // Define la cantidad según tu lógica
  var subtotal = cantidad * producto.price_sold;
  var filaExistente = $(`${tabla} tr[data-producto="${producto.bar_code}"]`);

  if (producto && producto.id && filaExistente.length > 0 && esSubtotal) {
      // Si el objeto producto está definido y tiene la propiedad 'id' y ya existe una fila para este producto en la tabla subtotal, actualiza la cantidad y el subtotal
      cantidad = parseInt(filaExistente.find("td.cantidad").text()) + 1;
      filaExistente.find("td.cantidad").text(cantidad);

      subtotal = cantidad * producto.price_sold;
      filaExistente.find("td.subtotal").text(`$${subtotal}`);
      actualizarTotal();

      // Actualiza los campos ocultos en el formulario de venta solo si es el producto deseado
      var ultimoProducto = productos[productos.length - 1]; // Obtener el último producto agregado
      if (producto.id === ultimoProducto.id) {
          $("#producto_id").val(producto.id);
          $("#bar_code").val(producto.bar_code);
          $("#cantidad").val(cantidad);
          $("#subtotal").val(subtotal);
      }
      return;
  }

 
     var fila = `<tr data-producto="${producto.bar_code}"> <input type="hidden" value="${producto.id}" name="producto_id" />
                      <td>${producto.name}</td>`;
 
     if (!esSubtotal) {
         fila += `<td>${producto.bar_code}</td>
                   <td>${producto.stock}</td>`;
     }
 
     fila += `<td >$${producto.price_sold}</td> <input type="hidden" value="${producto.price_sold}" name="price_sold" />`;
 
     if (esSubtotal) {
      fila += `<td class="cantidad">${cantidad}</td> 
           <td class="subtotal">$${subtotal}</td>`;
  }
  
     $(tabla).append(fila);  // Agrega la fila a la tabla especificada
     productos.push(producto); // Agrega el producto a la lista
}
// Función para enviar la venta
function enviarVenta() {
  // Verificar si hay productos para enviar
  if (productos.length === 0) {
    mostrarMensaje("No hay productos para enviar."); // Muestra un mensaje si no hay productos en la lista
    return; // Sale de la función si no hay productos
  }

  // Obtener el token CSRF
  var csrftoken = getCookie('csrftoken');

  // Realiza la petición AJAX para enviar la venta
  $.ajax({
    url: "/venta/panelVenta/",         // URL del endpoint para enviar la venta
    type: "POST",                       // Tipo de petición HTTP
    data: {
      csrfmiddlewaretoken: csrftoken, // Agrega el token CSRF
      productos: JSON.stringify(productos) // Convierte la lista de productos a JSON
    },
    dataType: "json",                   // Tipo de datos esperados en la respuesta
    success: function(response) {
      console.log('Solicitud POST exitosa:', response);
    },
    error: function (error) {           // Función que se ejecuta si hay un error en la petición
      console.error("Error al enviar la venta:", error); // Muestra el error en la consola del navegador
      mostrarMensaje("Error al enviar la venta.");       // Muestra un mensaje de error al usuario
    },
  });
}

// Función para obtener el valor de una cookie por su nombre
function getCookie(name) {
  var cookieValue = null;
  if (document.cookie && document.cookie !== '') {
    var cookies = document.cookie.split(';');
    for (var i = 0; i < cookies.length; i++) {
      var cookie = cookies[i].trim();
      // ¿Esta cadena de cookie comienza con el nombre que queremos?
      if (cookie.substring(0, name.length + 1) === (name + '=')) {
        cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
        break;
      }
    }
  }
  return cookieValue;
}

