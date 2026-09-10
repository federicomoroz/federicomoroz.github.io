/* =============================================================================
 * Asistente del portfolio.
 *
 * QUE ES: un FAQ con matching de palabras clave sobre una base escrita a mano
 * (_data/asistente.yml + _data/projects.yml). NO hay modelo generativo, ni API,
 * ni backend. Nada de lo que dice se genera: todo sale de un string curado.
 *
 * POR QUE IMPORTA: la garantia de que no contesta una consulta de codigo es
 * estructural, no una instruccion que se pueda esquivar. Aunque alguien burle
 * todos los gates de abajo, lo peor que consigue es un dato del perfil.
 *
 * EL MODO DE FALLA QUE ESTO EVITA
 * Un bot por keywords no inventa Python: lo que hace es peor de leer. Ante
 * "como hago un decorator en Python?" matchea la clave `python` y devuelve
 * "Python es su stack principal: FastAPI, SQLAlchemy...", como si eso fuera la
 * respuesta. Contesta al lado de la pregunta y queda como que no entendio.
 *
 * Por eso los gates corren ANTES del match contra el KB, nunca despues: para
 * cuando `python` matchea, la pregunta ya fue rechazada. Es el mismo orden que
 * usa handoff — las reglas revisan la propuesta antes de que se ejecute.
 *
 * FALLA CERRADO: el default es rechazar. Solo se contesta con un match
 * positivo; sin match no hay respuesta "aproximada", hay derivacion al
 * contacto. Un guardrail que ante la duda deja pasar no es un guardrail.
 * ========================================================================== */

(function ()
{
    'use strict';

    var D = window.__ASISTENTE__;
    if (!D) { return; }

    /* === Normalizacion ====================================================
       Se hace una sola vez por pregunta y todo lo demas trabaja sobre el
       resultado: minusculas, sin acentos y sin puntuacion.

       Las tres sustituciones de arriba van ANTES de comerse la puntuacion,
       porque son justamente nombres donde el simbolo es parte del nombre: si
       se limpia primero, "C#" queda en "c" y ".NET" en "net", que despues
       matchean cualquier cosa. */
    function normalizar(txt)
    {
        return String(txt || '')
            .toLowerCase()
            .replace(/c\s*#|c\s*sharp/g, ' csharp ')
            .replace(/asp\s*\.\s*net/g, ' aspnet ')
            .replace(/\.\s*net/g, ' dotnet ')
            .normalize('NFD').replace(/[\u0300-\u036f]/g, '')
            .replace(/[^a-z0-9+]+/g, ' ')
            .replace(/\s+/g, ' ')
            .trim();
    }

    function tiene(texto, frase)
    {
        var f = normalizar(frase);
        if (!f) { return false; }
        var re = new RegExp('(^| )' + f.replace(/[.*+?^${}()|[\]\\]/g, '\\$&') + '($| )');
        return re.test(texto);
    }

    function alguno(texto, lista)
    {
        for (var i = 0; i < lista.length; i++)
        {
            if (lista[i].test(texto)) { return true; }
        }
        return false;
    }

    /* === Gates ============================================================
       Cada grupo es una razon distinta para frenar. Se separan para poder
       ajustar uno sin tocar los otros. */

    // 1. Intentos de reprogramar al asistente.
    var INYECCION = [
        /\b(ignora|ignore|olvida|forget) (todo|las|lo|tus|your|all|previous)\b/,
        /\b(actua|actuá|act|comportate|pretend|roleplay) (como|as)\b/,
        /\bsystem prompt\b/, /\bprompt del sistema\b/, /\bjailbreak\b/,
        /\bsos (chatgpt|claude|gpt)\b/, /\byou are (chatgpt|claude|gpt)\b/,
        /\bnuevas instrucciones\b/, /\bnew instructions\b/
    ];

    // 2. Marcadores de codigo. Si aparece codigo, no hay ambiguedad posible.
    //
    // OJO: este grupo se evalua contra el texto CRUDO en minuscula, no contra
    // el normalizado. La normalizacion se come toda la puntuacion, y aca la
    // puntuacion ES la senal: contra el normalizado, ninguno de estos patrones
    // podria matchear nunca.
    var CODIGO = [
        /```/, /\bdef\s+[a-z_]/, /\bfunction\s+[a-z_]/, /\bclass\s+[a-z_]/,
        /\bimport\s+[a-z_]/, /\bfrom\s+[a-z_.]+\s+import\b/,
        /\bselect\b[\s\S]*\bfrom\b/, /console\s*\.\s*log/, /\bprint\s*\(/,
        /=>/, /\{\s*$/m, /;\s*$/m, /<\/?[a-z][a-z0-9]*\s*\/?>/,
        /\bnpm\s+(install|run)\b/, /\bpip\s+install\b/,
        /\bgit\s+(clone|commit|push|rebase|merge)\b/
    ];

    // 3. Pedidos de instruccion o de trabajo. El grupo mas delicado: aca es
    //    donde se cuelan los falsos positivos, asi que ver ANCLAS mas abajo.
    var INSTRUCCION = [
        /\bcomo (hago|se hace|puedo|hacer|implemento|instalo|configuro|conecto|creo|uso|escribo|arreglo|soluciono)\b/,
        /\bhow (do|can|to|would) (i|you)\b/,
        /\b(escribime|escribeme|hazme|haceme|armame|generame|dame|pasame|mostrame|codeame|corregime|explicame como)\b/,
        /\b(write|give|show|generate|build) me\b/,
        /\b(ejemplo|example|snippet|tutorial|paso a paso|boilerplate|codigo de ejemplo)\b/,
        /\b(implementa|programa|codea|refactoriza|optimiza|traduci|traduce|resolve|resuelve) \b/,
        // Subjuntivo de pedido ("necesito que me generes...", "quiero que armes...").
        // Estas formas no aparecen fuera de un pedido, asi que no hace falta
        // exigir el verbo introductorio.
        /\b(generes|hagas|escribas|armes|implementes|codees|desarrolles|crees|refactorices|traduzcas|resuelvas|arregles)\b/
    ];

    // 4. Depuracion: alguien trayendo un problema suyo.
    var DEBUG = [
        /\b(error|exception|traceback|stacktrace|stack trace|bug|debug|debuggear)\b/,
        /\bno (me )?(anda|funciona|compila|corre)\b/,
        /\bpor ?que (no )?(anda|funciona|compila|tira|falla)\b/,
        /\b(falla|rompe|revienta) (el|la|mi)\b/,
        /\bdoesn ?t work\b/, /\bnot working\b/
    ];

    /* Las ANCLAS son lo que rescata una pregunta legitima de la regla 3.
       "Como funciona nexo?" y "como hago un circuit breaker?" arrancan igual;
       lo que las separa es que la primera nombra algo del perfil.

       Sin esto el gate se comeria preguntas buenas — y un guardrail que
       rechaza lo que deberia contestar es tan inutil como uno que deja pasar
       todo, solo que falla del otro lado. */
    var ANCLAS = (function ()
    {
        // Nada de pronombres sueltos ("tu", "su", "el"): aparecen en cualquier
        // frase y anclarian todo. Solo marcas inequivocas de que la pregunta
        // es por una persona.
        var base = ['federico', 'palatnik', 'moroz', 'vos', 'usted',
                    'trabajaste', 'trabajo el', 'hiciste', 'hizo', 'tenes',
                    'tiene', 'sabe', 'sabes', 'usaste', 'construyo', 'armo',
                    'resolvio', 'su experiencia', 'tu experiencia',
                    'does he', 'did he', 'has he', 'his experience'];

        // Solo el NOMBRE del proyecto ancla, nunca su stack. Si anclara el
        // stack, "como hago un decorator en Python?" pasaria el gate por la
        // clave `python` y terminaria contestando el perfil: el fallo exacto
        // que estos gates existen para evitar.
        (D.proyectos || []).forEach(function (p)
        {
            (p.ancla || []).forEach(function (c) { base.push(c); });
        });
        return base;
    })();

    function tieneAncla(texto)
    {
        for (var i = 0; i < ANCLAS.length; i++)
        {
            if (tiene(texto, ANCLAS[i])) { return true; }
        }
        return false;
    }

    /* === Decision =========================================================
       Devuelve {tipo, texto, contacto}. tipo: 'ok' | 'tarea' | 'fuera'. */
    function responder(pregunta)
    {
        var crudo = String(pregunta || '').toLowerCase();
        var t = normalizar(pregunta);
        if (!t) { return { tipo: 'fuera', texto: D.rechazo.fuera, contacto: true }; }

        // CODIGO va contra el crudo porque necesita la puntuacion; el resto
        // trabaja sobre el normalizado, que es donde viven las palabras.
        if (alguno(crudo, CODIGO) || alguno(t, INYECCION) || alguno(t, DEBUG))
        {
            return { tipo: 'tarea', texto: D.rechazo.tarea, contacto: true };
        }

        // La unica regla que admite excepcion, y solo con un ancla del perfil.
        if (alguno(t, INSTRUCCION) && !tieneAncla(t))
        {
            return { tipo: 'tarea', texto: D.rechazo.tarea, contacto: true };
        }

        var mejor = null, mejorPuntaje = 0;
        (D.faq || []).concat(D.proyectos || []).forEach(function (e)
        {
            var puntaje = 0;
            (e.claves || []).forEach(function (c)
            {
                // Se puntua por largo de la clave: "spring boot" es una senal
                // mas fuerte que "java", y deberia ganarle si compiten.
                if (tiene(t, c)) { puntaje += normalizar(c).length; }
            });
            if (puntaje > mejorPuntaje) { mejorPuntaje = puntaje; mejor = e; }
        });

        if (!mejor) { return { tipo: 'fuera', texto: D.rechazo.fuera, contacto: true }; }

        return {
            tipo: 'ok',
            texto: mejor.respuesta,
            contacto: mejor.id === 'contacto' || mejor.id === 'disponibilidad'
        };
    }

    // Se expone ANTES de tocar el DOM, a proposito: la logica de decision es
    // lo que hay que poder testear, y no deberia necesitar que el widget este
    // montado para hacerlo. asistente.test.html la usa asi.
    window.__asistenteResponder = responder;

    /* === Render =========================================================== */

    // Solo **negrita** y `codigo`. Cualquier otra cosa se escapa: el texto sale
    // del YAML, pero la pregunta del usuario tambien pasa por aca al ecoarse.
    function formato(txt)
    {
        return String(txt)
            .replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;')
            .replace(/\*\*([^*]+)\*\*/g, '<strong>$1</strong>')
            .replace(/`([^`]+)`/g, '<code>$1</code>');
    }

    var raiz = document.getElementById('asistente');
    if (!raiz) { return; }

    var panel      = raiz.querySelector('.as-panel');
    var lista      = raiz.querySelector('.as-mensajes');
    var form       = raiz.querySelector('.as-form');
    var input      = raiz.querySelector('.as-input');
    var btnAbrir   = raiz.querySelector('.as-lanzador');
    var btnCerrar  = raiz.querySelector('.as-cerrar');
    var sugs       = raiz.querySelector('.as-sugerencias');

    function mensaje(quien, html, conContacto)
    {
        var li = document.createElement('div');
        li.className = 'as-msg as-' + quien;
        li.innerHTML = html + (conContacto ? D.contactoHtml : '');
        lista.appendChild(li);
        lista.scrollTop = lista.scrollHeight;
    }

    function preguntar(texto)
    {
        if (!texto.trim()) { return; }
        mensaje('user', formato(texto), false);
        var r = responder(texto);
        mensaje('bot', formato(r.texto), r.contacto);
        if (sugs) { sugs.hidden = true; }
    }

    function abrir()
    {
        panel.hidden = false;
        raiz.classList.add('abierto');
        btnAbrir.setAttribute('aria-expanded', 'true');
        input.focus();
    }

    function cerrar()
    {
        panel.hidden = true;
        raiz.classList.remove('abierto');
        btnAbrir.setAttribute('aria-expanded', 'false');
        btnAbrir.focus();
    }

    btnAbrir.addEventListener('click', function () { panel.hidden ? abrir() : cerrar(); });
    btnCerrar.addEventListener('click', cerrar);

    document.addEventListener('keydown', function (e)
    {
        if (e.key === 'Escape' && !panel.hidden) { cerrar(); }
    });

    form.addEventListener('submit', function (e)
    {
        e.preventDefault();
        preguntar(input.value);
        input.value = '';
    });

    if (sugs)
    {
        sugs.addEventListener('click', function (e)
        {
            var b = e.target.closest('.as-sug');
            if (b) { preguntar(b.textContent); }
        });
    }

})();
