<p align="center">
  <img src="https://alivemindset.github.io/projects/WasaK/img/WasaK.png" width="150px"><br/>
  Language:<br/>
  <b><i>Português-BR</b></i> | 
  <a href="README.md"><b><i>English</i></b></a> | 
  <a href="README-ES.md">Spanish</a><br/><br/>
  <img src="https://img.shields.io/badge/version-1.0-blue.svg"> &nbsp;
  <img src="https://img.shields.io/badge/python-2.7.12-blue.svg"> &nbsp;
  <img src="https://img.shields.io/badge/OS-Linux-brightgreen.svg">
</p>
<br/>
<h2>Sinopse</h2>
WasaK - WhatsHack é um chat cliente-servidor desenvolvido em python para Hackers. O grande diferencial do WasaK é que ele permite executar comandos aonde o servidor está ligado, sendo assim, tem uma maior eficiência em seus pentests enquanto conversa com seus amigos.

<h2>Motivação</h2>
Eu sempre quis conversar com meus amigos sem que alguém nos monitorassem, ou a conversa ficasse salva, desejava mais anônimidade, então, surgiu a ideia de criar um chat único e próprio. Uma das coisas que me incomodava, era o fato de o chat ser apenas um chat, sendo assim, decidi colocar algo único, foi ai que criei a oportunidade do usuario executar comandos.

<h2>Instalação</h2>
<h3>Pré-requisitos</h3>
<ul>
<li>Python <= 2.7.12</li>
<li>OS Linux</li>
<li>Wget</li>
<li>Git</li>
</ul>
<h3>Como instalar o cliente</h3>
Basta executar o comando abaixo em seu terminal.
<pre><code> wget https://raw.githubusercontent.com/alivemindset/WasaK/master/WasaK.py && sudo chmod +x WasaK.py && sudo mv WasaK.py /usr/bin/wasak </code></pre>
<h3>Como instalar o servidor</h3>
<pre><code> git clone https://github.com/alivemindset/WasaK/ </pre></code>

<h2>Uso</h2>
<h3>Como usar o cliente</h3>
Após executar o comando informado a cima, nós precisamos executar o programa. Para isto, execute o comando:
<pre><code>sudo wasak</pre></code>
<p>Em seguida ele ira pedir: <p/>
<ul>
<li>O IP do servidor, se o mesmo não for informado, ele vai definir o padrão: 127.0.0.1</li>
<li>A PORTA do servidor, se o mesmo não for informado, ele vai definir o padrão: 12786</li>
<li>UM NICKNAME para identifica-lo, se o mesmo não for informado, ele vai definir um aleatorio.</li>
</ul>
<p align="center"><img src="https://alivemindset.github.io/projects/WasaK/img/exClient.png" width="600px"></p>

<h3>Como usar o servidor</h3>
<p>Não se esqueça de abrir as portas do modem! Ou então, utilize o ngrok para abrir um servidor externo.</p>
Após executar o comando informado a cima, nós precisamos executar o programa. Para isto, execute o comando:
<pre><code>cd WasaK/ && sudo python2 WasaK-server.py</pre></code>
<p>Em seguida ele ira pedir: <p/>
<ul>
<li>O IP do servidor, se o mesmo não for informado, ele vai definir o padrão: 127.0.0.1</li>
<li>A PORTA do servidor, se o mesmo não for informado, ele vai definir o padrão: 12786</li>
<li>NOME DO SERVIDOR, se o mesmo não for informado, ele vai definir o padrão: WasaK</li>
<li>ARQUIVO COM COMANDOS PROTEGIDO, usado para bloquear alguns comandos. Se não for informado, será utilizado o padrão: ./cmd-protg</li>
<li>MÁX. CONEXÕES, quantidade máxima de usuarios que vão conectar. Se não for informado, será utilizado o padrão: 5</li>
</ul>
<p align="center"><img src="https://alivemindset.github.io/projects/WasaK/img/exServer.png" width="600px"></p>

<h3>Errors/Bugs</h3>
Se achar erros ou bugs, nos informe por: 
<ul>
<li>E-mail: alivemindset@protonmail.com</li>
<li>Facebook: https://www.facebook.com/alivemindset</li>
</ul>
