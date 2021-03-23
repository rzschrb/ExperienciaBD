import os
import cx_Oracle

os.environ['PATH']='D:\\oraclexe\\app\\oracle\\instantclient_19_10'
# Criar conexão
connection = cx_Oracle.connect('aluno/aluno@localhost/xe')
cursor = connection.cursor()

sql= ("select user from dual")
for i in cursor.execute(sql):
    print(i)

cursor.close()
connection.close()
