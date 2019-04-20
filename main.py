import sqlite3

def cria():
    print('Para criar deve apagar o ja existente')
    conect = sqlite3.connect('cadastro.db')
    cursor = conect.cursor()
    cursor.execute("""
    CREATE TABLE cliente (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    idade NUMBER,
    cpf     VARCHAR(11) NOT NULL,
    email TEXT NOT NULL
    );
    """)
    conect.close()


def insert():
    conect = sqlite3.connect('cadastro.db')
    cursor = conect.cursor()
    nome = str(input('Nome : '))
    idade = int(input('Idade : '))
    cpf = str(input('Cpf : '))
    email = str(input('Email : '))
    cursor.execute("""
    INSERT INTO cliente(nome, idade, cpf, email)
    VALUES (?,?,?,?)
    """,(nome,idade,cpf,email))
    conect.commit()
    conect.close()



def mostra():
    print(50*'#')
    conect = sqlite3.connect('cadastro.db')
    cursor = conect.cursor()
    cursor.execute("""
    SELECT * FROM cliente;
    """)
    for lx in cursor.fetchall():
        print(lx)
    conect.close()
