/* ==========================================================================
   Parroquia Nuestra Señora de Lourdes · La Serena
   Único archivo de JavaScript del sitio.

   Hace tres cosas:
     1. Menú: desplegables en escritorio (CSS) y acordeón en móvil.
     2. Pastorales: muestra una categoría a la vez.
     3. Certificados: envía el formulario y muestra el estado de éxito.

   Sin JavaScript el sitio sigue siendo utilizable: el menú queda abierto,
   las pastorales se muestran todas y el formulario se envía de forma normal.
   ========================================================================== */

/* --------------------------------------------------------------------------
   CONFIGURACIÓN  ·  formulario de certificados
   --------------------------------------------------------------------------
   El sitio es estático, así que el formulario necesita un servicio externo
   que reenvíe los datos al correo de la Secretaría.

   Opción recomendada (gratuita, sin cuenta): FormSubmit.
     1. Escribe aquí:  https://formsubmit.co/ajax/secretariaplourdes@gmail.com
     2. Envía el formulario una vez desde el sitio ya publicado.
     3. Llegará un correo de confirmación a esa casilla: hay que abrirlo y
        pulsar el enlace. Desde ese momento las solicitudes llegan solas.

   Mientras esto esté vacío, el formulario NO envía nada y avisa en pantalla.
   -------------------------------------------------------------------------- */
var ENDPOINT_CERTIFICADOS = "";

(function () {
  "use strict";

  document.documentElement.classList.add("js");

  /* ------------------------------------------------------------------------
     1. Menú
     ------------------------------------------------------------------------ */
  function iniciarMenu() {
    var boton = document.querySelector(".menu__abrir");
    var lista = document.querySelector(".menu__lista");
    if (!boton || !lista) return;

    boton.addEventListener("click", function () {
      var abierto = lista.classList.toggle("menu__lista--abierta");
      boton.setAttribute("aria-expanded", abierto ? "true" : "false");
    });

    // Cada botón "+" abre el submenú de su sección (solo en móvil)
    var desplegables = document.querySelectorAll(".menu__desplegar");
    Array.prototype.forEach.call(desplegables, function (btn) {
      btn.addEventListener("click", function () {
        var item = btn.closest(".menu__item");
        if (!item) return;
        var abierto = item.classList.toggle("menu__item--abierto");
        btn.setAttribute("aria-expanded", abierto ? "true" : "false");
      });
    });

    // Escape cierra lo que esté abierto
    document.addEventListener("keydown", function (e) {
      if (e.key !== "Escape") return;
      lista.classList.remove("menu__lista--abierta");
      boton.setAttribute("aria-expanded", "false");
      Array.prototype.forEach.call(
        document.querySelectorAll(".menu__item--abierto"),
        function (item) {
          item.classList.remove("menu__item--abierto");
          var b = item.querySelector(".menu__desplegar");
          if (b) b.setAttribute("aria-expanded", "false");
        }
      );
    });
  }

  /* ------------------------------------------------------------------------
     2. Pastorales: una categoría a la vez
     ------------------------------------------------------------------------ */
  function iniciarPastorales() {
    var indice = document.querySelector(".indice");
    var categorias = document.querySelectorAll(".categoria");
    if (!indice || !categorias.length) return;

    var enlaces = indice.querySelectorAll(".indice__enlace");

    function mostrar(id, desplazar) {
      var encontrada = false;

      Array.prototype.forEach.call(categorias, function (cat) {
        var visible = cat.id === id;
        cat.hidden = !visible;
        if (visible) encontrada = true;
      });

      // Si el id no existe, se muestra la primera categoría
      if (!encontrada) {
        categorias[0].hidden = false;
        id = categorias[0].id;
      }

      Array.prototype.forEach.call(enlaces, function (a) {
        var activo = a.getAttribute("href") === "#" + id;
        a.classList.toggle("indice__enlace--activo", activo);
        if (activo) a.setAttribute("aria-current", "true");
        else a.removeAttribute("aria-current");
      });

      if (desplazar) {
        var panel = document.getElementById("panel-pastorales");
        if (panel) panel.scrollIntoView({ block: "start" });
      }
    }

    Array.prototype.forEach.call(enlaces, function (a) {
      a.addEventListener("click", function (e) {
        e.preventDefault();
        var id = a.getAttribute("href").slice(1);
        mostrar(id, true);
        // Deja la categoría en la dirección, para poder compartir el enlace
        if (window.history && window.history.replaceState) {
          window.history.replaceState(null, "", "#" + id);
        }
      });
    });

    // Al abrir con #ministerios, o al cambiar el hash desde el menú
    mostrar((window.location.hash || "").slice(1) || categorias[0].id, false);
    window.addEventListener("hashchange", function () {
      mostrar((window.location.hash || "").slice(1), true);
    });
  }

  /* ------------------------------------------------------------------------
     3. Certificados
     ------------------------------------------------------------------------ */
  function iniciarCertificados() {
    var form = document.getElementById("form-certificado");
    var exito = document.getElementById("certificado-enviado");
    if (!form || !exito) return;

    var aviso = form.querySelector(".formulario__aviso");
    var boton = form.querySelector("button[type=submit]");

    function mostrarAviso(texto) {
      if (!aviso) return;
      aviso.textContent = texto;
      aviso.hidden = false;
    }

    function mostrarExito() {
      form.hidden = true;
      var aparte = document.getElementById("aparte-certificados");
      if (aparte) aparte.hidden = true;
      exito.hidden = false;
      exito.setAttribute("tabindex", "-1");
      exito.focus();
      window.scrollTo(0, 0);
    }

    form.addEventListener("submit", function (e) {
      e.preventDefault();

      if (!form.reportValidity()) return;

      if (!ENDPOINT_CERTIFICADOS) {
        mostrarAviso(
          "El formulario todavía no está conectado al correo de la Secretaría. " +
          "Mientras tanto, escribe a secretariaplourdes@gmail.com o llama al +56 9 9280 3442."
        );
        return;
      }

      if (boton) { boton.disabled = true; boton.textContent = "Enviando…"; }

      fetch(ENDPOINT_CERTIFICADOS, {
        method: "POST",
        body: new FormData(form),
        headers: { Accept: "application/json" }
      })
        .then(function (r) {
          if (!r.ok) throw new Error("Respuesta " + r.status);
          mostrarExito();
        })
        .catch(function () {
          if (boton) { boton.disabled = false; boton.textContent = "Enviar solicitud"; }
          mostrarAviso(
            "No pudimos enviar la solicitud. Revisa tu conexión e inténtalo otra vez, " +
            "o escribe a secretariaplourdes@gmail.com."
          );
        });
    });
  }

  /* ------------------------------------------------------------------------ */
  function iniciar() {
    iniciarMenu();
    iniciarPastorales();
    iniciarCertificados();
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", iniciar);
  } else {
    iniciar();
  }
})();
