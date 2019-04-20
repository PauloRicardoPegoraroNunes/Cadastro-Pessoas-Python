import sqlite3
import defs

def menu():
        
        while True:
                print('0 - Cria Banco de Dados')
                print('1 - Gravar Dados')
                print('2 - Vizualizar')
                print('3 - Sair')
                r = int(input('Escolha : '))
                if r == 0:
                        defs.cria()
                if r == 1:
                        defs.insert()
                if r == 2:
                        defs.mostra()
                        print(50*'#')
                if r == 3:
                        break
menu()







