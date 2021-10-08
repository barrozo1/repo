import mysql.connector
from mysql.connector import Error


try:
    conexao = mysql.connector.connect(host='localhost',
                                      database='petx',
                                      user='root',
                                      password='')
    if (conexao.is_connected()):
        print("Conectou")
        cursor = conexao.cursor()
        cursor.execute("Select * from usuarios")

except Error as erro:
    print("Erro: ", erro)

finally:
    if (conexao.is_connected()):
        cursor.close()
        conexao.close()
        print("conexao encerrada")