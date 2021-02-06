<h1>Administración Consorcio</h1>

<h2><a id="user-content-tabla-de-contenido" class="anchor" aria-hidden="true" href="#tabla-de-contenido"><svg class="octicon octicon-link" viewBox="0 0 16 16" version="1.1" width="16" height="16" aria-hidden="true"><path fill-rule="evenodd" d="M7.775 3.275a.75.75 0 001.06 1.06l1.25-1.25a2 2 0 112.83 2.83l-2.5 2.5a2 2 0 01-2.83 0 .75.75 0 00-1.06 1.06 3.5 3.5 0 004.95 0l2.5-2.5a3.5 3.5 0 00-4.95-4.95l-1.25 1.25zm-4.69 9.64a2 2 0 010-2.83l2.5-2.5a2 2 0 012.83 0 .75.75 0 001.06-1.06 3.5 3.5 0 00-4.95 0l-2.5 2.5a3.5 3.5 0 004.95 4.95l1.25-1.25a.75.75 0 00-1.06-1.06l-1.25 1.25a2 2 0 01-2.83 0z"></path></svg></a>Tabla de contenido
</h2>
<ul>
  <li><a href="#introduccion-al-proyecto">Introducción al proyecto</a></li>
  <li><a href="#implementaci%C3%B3n-del-proyecto">Implementación del proyecto</a></li>
  <li><a href="#resultados">Resultados</a></li>
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
<li><strong> </strong>: El cliente requiere de poder acceder mediante una credencial proporcionada, seguido debería poder descargar un PDF donde de manera detallada se describa en un resumen los gastos y el monto de dinero que adeuda.</li>
<li><strong> </strong>: El administrador tendría que ser capaz de llenar un único formulario proporcionando solo los datos absolutamente necesarios y que el programa no puede contemplar por factores externos.</li>
</ul>

Empezamos definiendo las tareas que realizaríamos en la primera semana, le dimos prioridad a las tareas que podíamos realizar y que nos llevarían a un producto tangible, en mi caso, me toco desarrollar la REST API que se encargaría de gestionar las request de entrada y salida, desde el frontend a la API, de la API a la base de datos, ida y vuelta, para esto primero cree una base de datos en MySQL y una tabla de dos columnas 'id' y 'access_code', luego, en la API cree las 2 rutas necesarias, una para que el cliente pueda ingresar su código, la API se encarga de consultar en la base de datos y asegurarse de que es un código valido, de ser así, proporciona acceso a la pagina indicada, la otra ruta permite crear un código de acceso, ahora mismo con motivos de testeo, pero esta ruta y método serán accesibles solo para el administrador en un futuro. Me asegure de que no exista ninguna vulnerabilidad a SQL Injection implementando las practicas necesarias.
