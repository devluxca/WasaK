#!/usr/bin/python2
#-*- coding: utf-8 -*-

try:
    import socket
    import select
    import commands
    from thread import *
    import os
    import sys
    import datetime
except Exception as err:
    print("ERRO: "+str(err))
    print("Não conseguimos importar as bibliotecas.")


server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
os.system('clear')
print """\033[1m\033[32;1m
                               <Servidor>
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

if commands.getoutput('whoami') != "root":      #Se o usuario não for ROOT, não deixe executar o servidor.
    print '\n\033[1m[\033[31;1m!\033[0;1m] Execute o servidor como ROOT !...'
    print("\033[1m[\033[31;1m*\033[0;1m] Ex.:   sudo " + sys.argv[0])
    exit()

#Algumas variaves
alvo = 'Nenhum'
users=[]
usersNick = []

try:            #Tente
    #################### PEGANDO O IP ####################
    ipaddr = str(raw_input('\033[1m[\033[32;1m*\033[0;1m] IP: '))
    if ipaddr == '' or ipaddr == ' ':
        ipaddr = '127.0.0.1'
        print("\033[1m[\033[33;1m!\033[0;1m] IP padrão definido ==> " + ipaddr)
    else:
        print("\033[1m[\033[32;1m!\033[0;1m] IP definido ==> " + ipaddr)

    #################### PEGANDO PORTA ####################
    port = raw_input('\033[1m[\033[32;1m*\033[0;1m] PORTA: ')
    if str(port) == '' or str(port) == ' ':
        port = 12786
        print("\033[1m[\033[33;1m!\033[0;1m] PORTA padrão definida ==> " + str(port))
    else:
        print("\033[1m[\033[32;1m!\033[0;1m] PORTA definida ==> " + str(port))

    #################### NOME SERVIDO ####################
    nomeserver = raw_input('\033[1m[\033[32;1m*\033[0;1m] Nome do servidor: ')
    if str(nomeserver) == '' or str(nomeserver) == ' ':
        nomeserver = 'WasaK'
        print("\033[1m[\033[33;1m!\033[0;1m] Nome do servidor padrão definido ==> " + nomeserver)
    else:
        print("\033[1m[\033[32;1m!\033[0;1m] Nome do servidor definido ==> " + nomeserver)

    #################### ARQ COM COMANDOS PROTEGIDO ####################
    arqprotgcam = raw_input('\033[1m[\033[32;1m*\033[0;1m] Arquivo com comandos protegido: ')
    if str(arqprotgcam) == '' or str(arqprotgcam) == ' ':
        arqprotgcam = "./cmd-protg"
        print("\033[1m[\033[33;1m!\033[0;1m] Arquivo com comandos protegido padrão definido ==> " + str(arqprotgcam))
    else:
        print("\033[1m[\033[32;1m!\033[0;1m] Arquivo com comandos protegido definido ==> " + str(arqprotgcam))

    #################### QTD MAX. ####################
    listenqtd = raw_input('\033[1m[\033[32;1m*\033[0;1m] Máx. Conexões: ')
    if str(listenqtd) == '' or int(listenqtd) < 2:
        listenqtd = 5
        print("\033[1m[\033[33;1m!\033[0;1m] Máx. Conexões padrão definido ==> " + str(listenqtd))
    else:
        print("\033[1m[\033[32;1m!\033[0;1m] Máx. Conexões definido ==> " + str(listenqtd) + "\n")

    #################### SERVIDOR ABERTO ####################
    server.bind((ipaddr, int(port)))
    print '[\033[32m*\033[0;1m] Servidor ABERTO.'
    server.listen(int(listenqtd))
    print '[\033[32m*\033[0;1m] Servidor escutando...\n\n'

except EOFError:    #CTRL+D
    print '\n[\033[31m-\033[0;1m] Saindo do servidor...'
    exit()
except KeyboardInterrupt:   #CTRL+C
    print '\n[\033[31m-\033[0;1m] Saindo do servidor...'
    exit()

def commandexec(nome,commandf, tipo):
    global msgpenv
    global alvo
    commande = ''

    if tipo == False:           #Se o tipo for um comando para o sistema do servidor
        protg = False           #Protegido começa sendo falso
        arqprotg = open(arqprotgcam, 'r')       #Abre o arquivo com comandos protegido
        for linha in arqprotg.readlines():      #Para cada linha do arquivo
            linha = linha.rstrip()              #Formata o que esta escrito
            if commandf.startswith(linha):      #Se o que a pessoa digitou começar com a linha atual do arquivo
                protg = True                    #Logo é protegido (True)
                msgpenv = '\033[32m\033[1m+B0tWasaK\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n O comando "'+commandf+'" é protegido. \n'      #Envia a mensagem dizendo que é protegido
                continue                        #Continua
            else:                               #Se o que a pessoa digitou NÃO começar com a linha atual do arquivo
                if protg == True:               #Verifica se já foi achado o comando protegido
                    continue                    #Continua
                else:                           #Se não tiver achado ainda
                    protg = False               #Protegido continua sendo falso
                    continue                    #Continua

        if protg == False:                      #Se no final de tudo, o comando não for protegido,
            commande = commands.getoutput(commandf)     #Executa ele.
            msgpenv ='\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n' + commande + '\n'

    elif tipo == True:          #Se o tipo for um comando definido pelo servidor

        if commandf.startswith('help'):     #Se for HELP
            msgpenv = '\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n Para executar um comando \033[1mSERVER-SIDE\033[0;0m, utilizase a exclamação. EX:\n  \033[1m!nmap google.com.br\033[0;0m\n Para usar comandos próprios \033[1mSERVER-SIDE\033[0;0m, utilizase o dólar. EX:\n  \033[1m$travar google.com.br\033[0;0m\n Para executar um comando \033[1mCLIENT-SIDE\033[0;0m, utilizase a tralha. EX:\n \033[1m #nmap google.com.br\033[0;0m\n Não execute comandos \033[1mSERVER-SIDE\033[0;0m que necessitam de decissões, como [Y/n], eles não funcionarão direito.\n '
        ############################################
        elif commandf.startswith('travar-alvo '):
            commandexemp, travado = commandf.split(' ')
            alvo = travado
            msgpenv = '\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n Um novo alvo travado » \033[32m%s\033[0;0m\n ' % alvo
        ############################################
        elif commandf.startswith('alvo-travado'):
            msgpenv = '\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n Alvo travado atualmente » \033[32m%s\033[0;0m\n ' % alvo
        ############################################
        elif commandf.startswith('destravar-alvo'):
            msgpenv = '\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n O alvo foi destravado » \033[32m%s\033[0;0m\n ' % alvo
            alvo = 'Nenhum'
        ############################################
        elif commandf.startswith('users'):
            if len(users) == 1:
                commande = ' Tem ' + str(len(users)) + ' usuario online.\n\n'
            else:
                commande = ' Tem ' + str(len(users)) + ' usuarios online.\n\n'

            for user in usersNick:
                commande += ' [\033[32m*\033[0;0m] \033[1m'+user+'\n\033[0;0m'

            msgpenv = '\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n' + commande + '\n'
        ############################################
        else:
            commande = commands.getoutput(commandf)
            msgpenv = '\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n' + commande + '\n'

    if commande == 'sh: 1: '+commandf+': not found':
        msgpenv = '\033[32m\033[1m+B0tWasak\033[0;0m \033[1m[\033[33m' + nome + '\033[0;0m\033[1m] '+commandf+'\033[0;0m\n\n O comando "' + commandf + '" não existe. \n'
    print msgpenv
    enviodemsgs(msgpenv, conn, True)

def userth(conn, addr):
    env = ''
    msgpenv = ''
    bemvindo = """\033[1m\033[32;1m
    
                                <"""+nomeserver+""">\033[1m\033[32;1m
         __       __                                __    __ 
        |  \  _  |  \                              |  \  /  \\
        | $$ / \ | $$  ______    _______   ______  | $$ /  $$
        | $$/  $\| $$ |      \  /       \ |      \ | $$/  $$ 
        | $$  $$$\ $$  \$$$$$$\|  $$$$$$$  \$$$$$$\| $$  $$  
        | $$ $$\$$\$$ /      $$ \$$    \  /      $$| $$$$$\  
        | $$$$  \$$$$|  $$$$$$$ _\$$$$$$\|  $$$$$$$| $$ \$$\ 
        | $$$    \$$$ \$$    $$|       $$ \$$    $$| $$  \$$\\
         \$$      \$$  \$$$$$$$ \$$$$$$$   \$$$$$$$ \$$   \$$
    
    \033[0;0m
           \033[1mUsuarios online: %i"""% len(users)+"""          Alvo travado: %s
    """ % alvo
    conn.send(bemvindo)

    while True:
            try:
                msg = conn.recv(4096)
                if len(msg) >= 1:
                    print "[ "+str(datetime.datetime.utcnow())+" ] " + msg.rstrip()

                    if msg.startswith('@+'):
                        na, nome = msg.split('+')
                        usersNick.append(nome)
                    elif msg.startswith('@-'):
                        na, nome = msg.split('-')
                        usersNick.remove(nome)

                    nome, commbot = msg.rstrip().split('»')
                    if commbot.startswith(' !') or commbot.startswith(' $'):
                        print "[ "+str(datetime.datetime.utcnow())+" ] " + '$!' + nome, commbot + ' $!'
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
            except Exception as err:
                if str(err).rstrip() == "need more than 1 value to unpack":
                    continue
                else:
                    print('Erro no servidor ==> ' + str(err))
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
    try:
        if len(users) != int(listenqtd):
            conn, addr = server.accept()
        else:
            conn, addr = server.accept()
            conn.send('@-Servidor-FULL')
            continue

        users.append(conn)
        print '[\033[32m+\033[0;0m] '+addr[0] + " conectado."

        start_new_thread(userth,(conn,addr))

    except EOFError:  # CTRL+D
        print '\n[\033[31m-\033[0;1m] Fechando o servidor...'
        enviodemsgs('@-Servidor-OFF', '', False)
        exit()
    except KeyboardInterrupt:  # CTRL+C
        try:
            fimmsgadm = False
            print("""\033[34;1m
    
            1 - Enviar mensagem        
            2 - Fechar servidor
    
                   \033[0;0m""")
            opc = str(raw_input('OPC» '))
            if opc == '1':
                while fimmsgadm == False:
                    msgadm = str(raw_input('\033[1m\033[33mAdmin\033[0;0m» '))
                    if msgadm.rstrip() == '</fim>':
                        fimmsgadm = True
                    else:
                        enviodemsgs('\033[1m\033[33mAdmin\033[0;0m» '+msgadm, '', False)
            elif opc == '2':
                print '\n[\033[31m-\033[0;1m] Fechando o servidor...'
                enviodemsgs('@-Servidor-OFF', '', False)
                server.close()
                exit()
            else:
                continue
        except EOFError:
            print '\n[\033[31m-\033[0;1m] Fechando o servidor...'
            enviodemsgs('@-Servidor-OFF', '', False)
            server.close()
            exit()
        except KeyboardInterrupt:
            print '\n[\033[31m-\033[0;1m] Fechando o servidor...'
            enviodemsgs('@-Servidor-OFF', '', False)
            server.close()
            exit()

conn.close()
server.close()