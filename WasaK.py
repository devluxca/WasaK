#!/usr/bin/python2
#-*- coding: utf-8 -*-

try:
    import socket
    import select
    import sys
    import os
    import time
    import random
except Exception as err:
    print("ERRO: "+err)
    print("Não conseguimos importar as bibliotecas.")

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
os.system('clear')
print """\033[1m\033[32;1m
                                <Cliente>
         __       __                                __    __ 
        |  \  _  |  \                              |  \  /  \\
        | $$ / \ | $$  ______    _______   ______  | $$ /  $$
        | $$/  $\| $$ |      \  /       \ |      \ | $$/  $$ 
        | $$  $$$\ $$  \$$$$$$\|  $$$$$$$  \$$$$$$\| $$  $$  
        | $$ $$\$$\$$ /      $$ \$$    \  /      $$| $$$$$\  
        | $$$$  \$$$$|  $$$$$$$ _\$$$$$$\|  $$$$$$$| $$ \$$\ 
        | $$$    \$$$ \$$    $$|       $$ \$$    $$| $$  \$$\\
         \$$      \$$  \$$$$$$$ \$$$$$$$   \$$$$$$$ \$$   \$$
         
        \033[31mCriado por: \033[0;1mLucas Simoni <alivemindset@protonmail.com>
        
\033[0;0m
"""
try:
    ipaddr = str(raw_input('\033[1m[\033[32;1m*\033[0;1m] IP: '))
    if ipaddr == '' or ipaddr == ' ':
        ipaddr = '127.0.0.1'
        print("\033[1m[\033[33;1m!\033[0;1m] IP padrão definido ==> " + ipaddr)
    else:
        print("\033[1m[\033[32;1m!\033[0;1m] IP definido ==> " + ipaddr)
    port = raw_input('\033[1m[\033[32;1m*\033[0;1m] PORTA: ')
    if str(port) == '' or str(port) == ' ':
        port = 12786
        print("\033[1m[\033[33;1m!\033[0;1m] PORTA padrão definida ==> " + str(port))
    else:
        print("\033[1m[\033[32;1m!\033[0;1m] PORTA definida ==> " + str(port))

    nome = raw_input('\033[1m[\033[32;1m*\033[0;1m] Digite um nickname: ')
    if nome == '' or nome == ' ':
        nome = random.choice(('NoName','Anonimo','SemNome','Guest','Convidado', 'Anonymous'))+random.choice(('1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20'))
        print("\033[1m[\033[33;1m!\033[0;1m] Nickname aleatorio definido ==> "+ nome)
    else:
        print("\033[1m[\033[33;1m!\033[0;1m] Nickname definido ==> " + nome)

    try:
        server.connect((ipaddr, int(port)))
        print '[\033[32m+\033[0;1m] Conectado ao servidor...'
        server.settimeout(5)
        server.setblocking(False)
        server.send('@+' + nome)
        os.system('clear')
    except:
        print '[\033[31m-\033[0;1m] Servidor não existe...'
        exit()
except EOFError:
    print '\n[\033[31m-\033[0;1m] Saindo do cliente...'
    exit()
except KeyboardInterrupt:
    print '\n[\033[31m-\033[0;1m] Saindo do cliente...'
    exit()

ant = False
while True:
    try:
        sockets_list = [sys.stdin, server]
        read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
                if str(message).rstrip().startswith('@-Servidor-OFF'):
                    print('\n\n[\033[31m-\033[0;1m] O servidor foi fechado!')
                    print '[\033[31m-\033[0;1m] Volte logo ' + nome
                    server.close()
                    exit()
                elif str(message).rstrip().startswith('@-Servidor-FULL'):
                    print('\n\n[\033[31m-\033[0;1m] O servidor está lotado!')
                    print '[\033[31m-\033[0;1m] Volte logo ' + nome
                    server.close()
                    exit()
                print '\n '+message
                ant = True
                print " \033[1m\033[31m"+nome+"\033[0;0m» ",
                sys.stdout.flush()
                time.sleep(0.2)
            else:
                if ant == False:
                    ant = True
                    message = sys.stdin.readline()
                else:
                    print "\033[1m\033[31m"+nome+"\033[0;0m» ",
                    message = sys.stdin.readline()

                if message.lower().rstrip().startswith('#'):
                    nothing, comm = message.lower().rstrip().split('#')
                    os.system(comm)
                    ant = True
                    print "\033[1m\033[31m" + nome + "\033[0;0m» ",
                    sys.stdout.flush()
                    time.sleep(0.2)
                    continue

                if message.lower().rstrip() == '':
                    continue

                server.send(nome+"» "+message)
                sys.stdout.flush()
    except KeyboardInterrupt:
        server.send('@-'+nome)
        print '\n\n[\033[31m-\033[0;1m] Volte logo ' + nome
        server.close()
        exit()
    except EOFError:
        server.send('@-'+nome)
        print '\n\n[\033[31m-\033[0;1m] Volte logo ' + nome
        server.close()
        exit()

server.close()
