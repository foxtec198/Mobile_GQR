from mysql.connector import connect
from datetime import datetime

conn = connect(
    host='192.168.1.198',
    user='guilherme.breve',
    password='84584608@Gui',
    database='pdv_01'
)
c = conn.cursor()

class addUser:
    def __init__(self):
        self.user()
        self.add(self.cpf, self.nome, self.email, self.senha, self.data)
        
    def user(self):
        self.cpf = input('cpf:')
        self.nome = input('Nome:')
        self.email = input('email:')
        self.senha = input('senha:')
        self.data = datetime.now()
    
    def add(self, cpf, nome, email, senha, data):
        c.execute(f'insert into usuarios(CPF, Nome, Email, Pwd, Data de Cadastro) values("{cpf}","{nome}","{email}","{senha}", "{data}")')
        conn.commit()
        print(f'Usuário {self.nome} adicionado')

c.execute('select * from usuarios')
user = c.fetchall()
print(user)