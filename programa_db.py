import sqlite3
import main

def menu():
        x = True
        while x == True:
                print('0 - Cria Banco de Dados')
                print('1 - Gravar Dados')
                print('2 - Vizualizar')
                print('3 - Sair')
                r = int(input('Escolha : '))
                if r == 0:
                        main.cria()
                if r == 1:
                        main.insert()
                if r == 2:
                        main.mostra()
                        print(50*'#')
                if r == 3:
                        x = False

menu()







