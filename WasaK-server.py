#!/usr/bin/python2
#-*- coding: utf-8 -*-
import socket
import select
import commands
from thread import *
import os
import sys


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
os.system('clear')
print """\033[1m\033[31m
             
             <BANNER>

\033[0;0m
\n"""

ipaddr = str(raw_input('IP: '))
if ipaddr == '' or ipaddr == ' ':
    ipaddr = '127.0.0.1'
port = int(raw_input('PORTA: '))
if str(port) == '' or str(port) == ' ':
    port = 12786
server.bind((ipaddr, port))
print '[\033[32m*\033[0;0m] Servidor escutando...'
listenqtd = int(raw_input('Máx. Conexões: '))
if listenqtd < 2 or str(listenqtd) == '':
    listenqtd = 5
server.listen(listenqtd)

alvo = 'Nenhum'
users=[]
usersNick = []

def commandexec(nome,commandf, tipo):
    global msgpenv
    print commandf
    commande = ''
    if tipo == False and commandf == 'clear' or commandf.startswith('mkdir') or commandf.startswith('rm') or commandf.startswith('touch') or commandf.startswith('ngrok') or commandf.startswith('echo') or commandf.startswith('nano') or commandf.startswith('vi') or commandf.startswith('leafpad') or commandf.startswith('reboot') or commandf.startswith('halt') or commandf.startswith('wget') or commandf.startswith('nano'):
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m O comando "'+commandf+'" é protegido.'
    elif tipo == True and commandf == 'help':
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m\n\n Para executar um comando \033[1mSERVER-SIDE\033[0;0m, utilizase a exclamação. EX:\n  \033[1m!nmap google.com.br\033[0;0m\n Para usar comandos próprios \033[1mSERVER-SIDE\033[0;0m, utilizase o dólar. EX:\n  \033[1m$travar google.com.br\033[0;0m\n Para executar um comando \033[1mCLIENT-SIDE\033[0;0m, utilizase a tralha. EX:\n \033[1m #nmap google.com.br\033[0;0m\n Não execute comandos \033[1mSERVER-SIDE\033[0;0m que necessitam de decissões, como [Y/n], eles não funcionarão direito.\n '
    elif tipo == True and commandf.startswith('travar '):
        commandexemp, travado = commandf.split(' ')
        alvo = travado
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m\n\n Alvo travado ====> \033[32m%s\033[0;0m\n ' % travado
    elif tipo == True and commandf.startswith('alvo-travado'):
        global alvo
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m\n\n Alvo travado ====> \033[32m%s\033[0;0m\n ' % alvo
    elif tipo == True and commandf.startswith('destravar-alvo'):
        global alvo
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m\n\n Alvo destravado ====> \033[32m%s\033[0;0m\n ' % alvo
        alvo = 'Nenhum'
    elif tipo == True and commandf.startswith('bin'):
        na, commandk = commandf.split('n')
        commande = commands.getoutput('getBin'+commandk+' -c')
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m\n\n' + commande + '\n'
    elif tipo == True and commandf.startswith('users'):
        if len(users) == 1:
            commande = ' Tem ' + str(len(users)) + ' usuario online.\n\n'
        else:
            commande = ' Tem ' + str(len(users)) + ' usuarios onlines.\n\n'

        for user in usersNick:
            commande += ' [\033[32m*\033[0;0m] \033[1m'+user+'\n\033[0;0m'

        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m\n\n' + commande + '\n'
    else:
        commande = commands.getoutput(commandf)
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m\n\n' + commande + '\n'

    if commande == 'sh: 1: '+commandf+': not found':
        msgpenv = '\033[32m\033[1m+B0t3Knall\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m]\033[0;0m O comando "' + commandf + '" não existe.'
    print msgpenv
    enviodemsgs(msgpenv, conn, True)

def userth(conn, addr):
    bemvindo = """\033[1m
    
            <BANNER>
    
    \033[0;0m
     Membros online: %i"""% len(users)+"""          Alvo travado: %s
    """ % alvo
    conn.send(bemvindo)

    while True:
            try:
                msg = conn.recv(4096)
                if len(msg) >= 1:
                    print msg
                    if msg.startswith('@+'):
                        na, nome = msg.split('+')
                        usersNick.append(nome)
                    nome, commbot = msg.rstrip().split('»')
                    if commbot.startswith(' !') or commbot.startswith(' $'):
                        print '<<<<<<<<<<<<<' + nome, commbot + '>>>>>>>>>>>>>'
                        try:
                            na, commandf = commbot.split('!')
                            tipo = False
                        except:
                            na, commandf = commbot.split('$')
                            tipo = True
                        start_new_thread(commandexec, (nome, commandf, tipo))
                    else:
                        env=False
                        msgpenv = msg.rstrip()
                    enviodemsgs(msgpenv,conn, env)
                else:
                    remove(conn)
            except:
                continue

def enviodemsgs(message,connection, verif):
    for clients in users:
        if verif == False:
            if clients!=connection:
                try:
                    clients.send(message)
                except:
                    clients.close()
                    remove(clients)
        else:
            try:
                clients.send(message)
            except:
                clients.close()
                remove(clients)


def remove(connection):
    if connection in users:
        users.remove(connection)

while True:
    conn, addr = server.accept()

    users.append(conn)
    print '[\033[32m+\033[0;0m] '+addr[0] + " conectado."

    start_new_thread(userth,(conn,addr))

conn.close()
server.close()
