import os  # Importando a biblioteca os, utilizada depois para executar o comando do sistema: ping
import time  # Importando a biblioteca time,
# utilizada depois para definir o tempo de sleep entre a execução de um comando e outro

with open('hosts.txt') as file:  # Abrindo o arquivo hosts.txt, criado antes com os hosts a serem verificados
    dump = file.read()
    dump = dump.splitlines()

    for ip in dump:  #
        print('Verificando o IP: ', ip)
        print('-' * 60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' * 60)
        time.sleep(5)
