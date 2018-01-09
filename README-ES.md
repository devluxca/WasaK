<p align="center">
  <img src="https://alivemindset.github.io/projects/WasaK/img/WasaK.png" width="150px"><br/>
  Language:<br/>
  <a href="README-PTBR.md">Português-BR</a> | 
  <a href="README.md">English</a> | 
  <b><i>Spanish</b></i><br/><br/>
  <img src="https://img.shields.io/badge/version-1.3-blue.svg"> &nbsp;
  <img src="https://img.shields.io/badge/python-2.7.12-blue.svg"> &nbsp;
  <img src="https://img.shields.io/badge/OS-Linux-brightgreen.svg">
</p>
<br/>
<h2>Sinopsis</h2>
WasaK - WhatsHack es un chat cliente-servidor desarrollado en python para Hackers. El gran diferencial de WasaK es que permite ejecutar comandos donde el servidor está conectado, siendo así, tiene una mayor eficiencia en sus peines mientras conversa con sus amigos.

<h2>Motivación</h2>
Yo siempre quise conversar con mis amigos sin que alguien nos monitoreara, o la conversación quedara salva, deseaba más anonimidad, entonces surgió la idea de crear un chat único y propio. Una de las cosas que me molestaba, era el hecho de que el chat era sólo un chat, siendo así, decidí poner algo único, fue ahí que creé la oportunidad del usuario ejecutar comandos.

<h2>Instalación</h2>
<h3>Requisitos previos</h3>
<ul>
<li>Python <= 2.7.12</li>
<li>OS Linux</li>
<li>Wget</li>
<li>Git</li>
<li>PyCrypto</li>
</ul>
<h3>Cómo instalar el cliente</h3>
Sólo tienes que ejecutar el siguiente comando en tu terminal.
<pre><code> wget https://raw.githubusercontent.com/alivemindset/WasaK/master/WasaK.py && sudo chmod +x WasaK.py && sudo mv WasaK.py /usr/bin/wasak </code></pre>
<h3>Cómo instalar el servidor</h3>
Sólo tienes que ejecutar el siguiente comando en tu terminal.
<pre><code> git clone https://github.com/alivemindset/WasaK/ </pre></code>

<h2>Uso</h2>
<h3>Cómo utilizar el cliente</h3>
Después de ejecutar el comando informado arriba, necesitamos ejecutar el programa. Para ello, ejecute el comando:
<pre><code>sudo wasak</pre></code>
<p>A continuación, pedirá: <p/>
<ul>
<li>La IP del servidor, si no se informa, se establecerá el valor predeterminado: 127.0.0.1</li>
<li>La PUERTA del servidor, si no se informa, se establecerá el valor predeterminado: 12786</li>
<li>Un NICKNAME para identificarlo, si el mismo no es informado, va a definir un aleatorio.</li>
</ul>
<p align="center"><img src="https://alivemindset.github.io/projects/WasaK/img/exClient.png" width="600px"></p>

<h3>Cómo utilizar el servidor</h3>
<p>No se olvide de abrir los puertos del módem! O bien, utilice ngrok para abrir un servidor externo.</p>
Después de ejecutar el comando informado arriba, necesitamos ejecutar el programa. Para ello, ejecute el comando:
<pre><code>cd WasaK/ && sudo python2 WasaK-server.py</pre></code>
<p>A continuación, pedirá: <p/>
<ul>
<li>La IP del servidor, si no se informa, se establecerá el valor predeterminado: 127.0.0.1</li>
<li>La PUERTA del servidor, si no se informa, se establecerá el valor predeterminado: 12786</li>
<li>NOMBRE DEL SERVIDOR, si el mismo no es informado, va a definir el estándar: WasaK</li>
<li>ARCHIVO CON COMANDOS PROTEGIDO, usado para bloquear algunos comandos. Si no se informa, se utilizará el patrón: ./cmd-protg</li>
<li>MÁX. CONEXIONES, cantidad máxima de usuarios que van a conectar. Si no se informa, se utilizará el patrón: 5</li>
</ul>
<p align="center"><img src="https://alivemindset.github.io/projects/WasaK/img/exServer.png" width="600px"></p>

<h2>Comandos</h2>
<h3>Tipos de comandos</h3>
<ul>
<li><b>#</b>comando</li>
<li><b>!</b>comando</li>
<li><b>$</b>comando</li>
</ul>

<h3>Comando: #</h3>
Los comandos que comienzan con "#" se ejecutarán en la máquina del cliente y se informarán solo al cliente.

<h3>Comando: !</h3>
Los comandos comenzaron con "!" Se ejecutará en la máquina del servidor y devolverá el resultado para todos.

<h3>Comando: $</h3>
Los comandos que comienzan con "$" son específicos del servidor. Algunos comandos:
<ul>
<li><b>$</b>help</li>
<li><b>$</b>users</li>
<li><b>$</b>travar-alvo http://alvo.com</li>
<li><b>$</b>alvo-travado</li>
<li><b>$</b>destravar-alvo</li>
</ul>  
<p align="center">
<img src="https://alivemindset.github.io/projects/WasaK/img/exCommand.png" width="600">
</p>

<h3>Errores/Bugs</h3>
Si encuentra errores o errores, nos informe por: 
<ul>
<li>E-mail: alivemindset@protonmail.com</li>
<li>Facebook: https://www.facebook.com/alivemindset</li>
</ul>
