#-*- coding: utf-8 -*-
import socket
import select
import sys
import os
import time

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
os.system('clear')
print """\033[1m\033[31m
             
             <BANNER>

\033[0;0m
"""

ipaddr = str(raw_input('IP: '))
if ipaddr == '' or ipaddr == ' ':
    ipaddr = '127.0.0.1'
port = int(raw_input('PORTA: '))
if port == '' or port == ' ':
    port = 12786
try:
    server.connect((ipaddr, port))
    print '[\033[32m+\033[0;0m] Conectado ao servidor...'
    server.setblocking(False)
except:
    print '[\033[32m-\033[0;0m] Servidor não existe...'
    exit()
nome = raw_input('Digite um nickname: ')
server.send('@+'+nome)
os.system('clear')

ant = False
while True:
    try:
        sockets_list = [sys.stdin, server]
        read_sockets,write_socket, error_socket = select.select(sockets_list, [], [])
        for socks in read_sockets:
            if socks == server:
                message = socks.recv(2048)
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

                server.send(nome+"» "+message)
                sys.stdout.flush()
    except KeyboardInterrupt:
        print 'Volte logo ' + nome
        server.close()
        exit()
    except EOFError:
        print 'Volte logo ' + nome
        server.close()
        exit()
server.close()
