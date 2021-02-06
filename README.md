<h1>Administración Consorcio</h1>

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementaci%C3%B3n-del-proyecto">Implementación del proyecto</a></li>
  <li><a href="#seguridad">La seguridad es importante</a></li>
</ul>

<h2><a id="user-content-introduccion-al-proyecto" class="anchor" aria-hidden="true" href="#introduccion-al-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Introducción al proyecto</h2>

El cliente nos pide la elaboración de un sistema mas cómodo para la gestión de expensas de un conjunto de departamentos, la idea es poder automatizar ciertas tareas que serian tediosas hacerlas manualmente, en base a esto procedemos a realizar una aplicación web donde cada inquilino pueda acceder al sitio y consultar por medio de la descarga de un PDF la información referente al monto que adeuda.

<h2><a id="user-content-implementación-del-proyecto" class="anchor" aria-hidden="true" href="#implementación-del-proyecto"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Implementación del proyecto</h2>
<ul>
<li><strong>JavaScript / HTML / CSS</strong>: Tecnologias utilizadas para la elaboración del frontend.</li>
<li><strong>Python 3+</strong>: El lenguaje utilizado para la elaboración del código backend.</li>
<li><strong>Django</strong>: Framework utilizado en conjunto con Python para la elaboración del backend.</li>
<li><strong>MySQL</strong>: Gestor de base de datos utilizado.</li>
<li><strong>Flask</strong>: Micro-framework utilizado para la elaboración de la REST API.</li>
</ul>

Adoptamos metodologías agiles de trabajo, escribimos el backlog con diferentes requerimientos que iba a tener el proyecto, posteriormente planteamos los casos de uso, en este proyecto habían dos requerimientos principales a tener en cuenta:
<ul>
<li><strong>Cliente</strong>: Requiere de poder acceder mediante una credencial proporcionada a una url, seguido debería poder descargar un PDF donde de manera detallada se describa en un resumen los gastos y el monto de dinero que adeuda.</li>
<li><strong>Administrador</strong>: Tendría que ser capaz de llenar un único formulario proporcionando solo los datos absolutamente necesarios y que el programa no puede contemplar por factores externos.</li>
</ul>

Empezamos definiendo las tareas que realizaríamos en la semana, le dimos prioridad a las tareas que podíamos realizar y que nos llevarían a un producto tangible, utilizamos Trello para tener una vista amplia del estado del proyecto y Git para trabajar, en mi caso, me toco desarrollar la REST API que se encargaría de gestionar las request de entrada y salida, desde el frontend a la API, de la API a la base de datos, ida y vuelta, para esto primero diseñe y desarrollo una base de datos en MySQL, la misma se iria actualizando y refaccionando a medida que el proyecto avance.

Me encarge de implementar y gestionar las siguientes rutas hasta el momento:

<table>
  <tbody><tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:3000/login" rel="nofollow">http://localhost:3000/login</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>POST
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
</tbody></table>

<table>
  <tbody><tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:3000/create_code" rel="nofollow">http://localhost:3000/create_code</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>POST
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
</tbody></table>

<table>
  <tbody><tr>
   <td><strong>URI</strong>
   </td>
   <td><a href="http://localhost:3000/home" rel="nofollow">http://localhost:3000/home</a>
   </td>
  </tr>
  <tr>
   <td><strong>METHOD</strong>
   </td>
   <td>GET
   </td>
  </tr>
  <tr>
   <td><strong>Request Headers</strong>
   </td>
   <td>-
   </td>
  </tr>
  <tr>
   <td><strong>Request Body</strong>
   </td>
   <td>-
   </td>
  </tr>
</tbody></table>

<h2><a id="user-content-seguridad" class="anchor" aria-hidden="true" href="#seguridad"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>La seguridad es importante</h2>

Contemple la posibilidad de una vulnerabilidad SQL Injection, implemente las medidas correspondientes en cada ruta a la base de datos como por ejemplo la utilización de query parameters.

Implemente un sistema para el cifrado de las sessiones desde el lado del servidor mediante una key.

Realice una buena gestion de las rutas, para asegurar de que se usen para lo que fueron programadas, de esta forma ningun usuario podra utilizarlas de una manera incorrecta.
