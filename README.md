<p align="center">
  <img src="https://alivemindset.github.io/projects/WasaK/img/WasaK.png" width="150px"><br/>
  Language:<br/>
  <a href="README-PTBR.md">Português-BR</a> | 
  <b><i>English</i></b> | 
  <a href="README-ES.md">Spanish</a><br/><br/>
  <img src="https://img.shields.io/badge/version-1.3-blue.svg"> &nbsp;
  <img src="https://img.shields.io/badge/python-2.7.12-blue.svg"> &nbsp;
  <img src="https://img.shields.io/badge/OS-Linux-brightgreen.svg">
</p>
<br/>
<h2>Synopsy</h2>
WasaK - WhatsHack is a client-server chat developed in python for Hackers. The great difference of the WasaK is that it allows to execute commands where the server is connected, thus, it has a greater efficiency in its combs while talking with his friends.

<h2>Motivation</h2>
I always wanted to talk to my friends without anyone monitoring us, or the conversation was saved, I wanted more anonymity, so the idea came up to create a unique and personal chat. One of the things that bothered me, was that chat was just a chat, so I decided to put something unique, that's where I created the user's opportunity to execute commands.

<h2>Installation</h2>
<h3>Prerequisites</h3>
<ul>
<li>Python <= 2.7.12</li>
<li>OS Linux</li>
<li>Wget</li>
<li>Git</li>
</ul>

<h3>How to install the client</h3>
Just run the command below on your terminal.
<pre><code> wget https://raw.githubusercontent.com/alivemindset/WasaK/master/WasaK.py && sudo chmod +x WasaK.py && sudo mv WasaK.py /usr/bin/wasak </code></pre>

<h3>How to install the server</h3>
Just run the command below on your terminal.
<pre><code> git clone https://github.com/alivemindset/WasaK/ </pre></code>

<h2>Use</h2>
<h3>How to use the client</h3>
After running the above command we need to run the program. To do this, execute the command:
<pre><code>sudo wasak</pre></code>
<p>Then he will ask: <p/>
<ul>
<li>The IP of the server, if it is not informed, it will set the default: 127.0.0.1</li>
<li>The server PORT, if it is not informed, it will set the default: 12786</li>
<li>A NICKNAME to identify it, if it is not informed, it will set a random.</li>
</ul>
<p align="center"><img src="https://alivemindset.github.io/projects/WasaK/img/exClient.png" width="600px"></p>

<h3>How to use the server</h3>
<p>Do not forget to open the modem ports! Or, use ngrok to open an external server.</p>
After running the above command we need to run the program. To do this, run the command:
<pre><code>cd WasaK/ && sudo python2 WasaK-server.py</pre></code>
<p>Then he will ask: <p/>
<ul>
<li>The IP of the server, if it is not informed, it will set the default: 127.0.0.1</li>
<li>The server PORT, if it is not informed, it will set the default: 12786</li>
<li>NAME OF THE SERVER, if it is not informed, it will set the default: WasaK</li>
<li>COMMAND FILE PROTECT, used to block some commands. If you are not informed, the default: ./cmd-protg</li>
<li>MAX. CONNECTIONS, maximum number of users that will connect. If you are not informed, the default: 5</li>
</ul>
<p align="center"><img src="https://alivemindset.github.io/projects/WasaK/img/exServer.png" width="600px"></p>

<h2>Commands</h2>
<h3>Types of commands</h3>
<ul>
<li><b>#</b>command</li>
<li><b>!</b>command</li>
<li><b>$</b>command</li>
</ul>

<h3>Command: #</h3>
The commands started with "#" will be executed on the client machine and will be informed only to the client.

<h3>Command: !</h3>
The commands started with "!" Will run on the server machine and will return the result for all.

<h3>Command: $</h3>
Commands starting with "$" are server-specific. Some commands:
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

<h3>Errors/Bugs</h3>
If you find errors or bugs, please report us by: 
<ul>
<li>E-mail: alivemindset@protonmail.com</li>
<li>Facebook: https://www.facebook.com/alivemindset</li>
</ul>
