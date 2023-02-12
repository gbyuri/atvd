#bibliotecas para execução
import json
import pymysql.cursors
import datetime
#carrega o arquivo .json onde estão os registro e os coloca na memoria
with open('logger.json') as data_json:
    data = json.load(data_json)
#Conexão com o banco de dados
connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='963258854',
                             database='teste')
cursor = connection.cursor()
registro=[]
print("Connected!")
#para enviar os registros que não possuem "." um ponto na sua formatação
'''for key, list in data.items():
    x=str(list.get('datetime'))
    if (len(x) > 4 and len(x) < 13):
        x= "0"+ x
        x= str(datetime.datetime.strptime(x,"%d%m%Y%H%M%S"))
        x = x.split(' ')
        z=str(x[0])
        y=str(x[1])
        registro.append((str(key),
                        z,
                        y,
                        list.get('hum'),
                        list.get('ledDiff'),
                        list.get('lux'),
                        list.get('temp')
        ))
        print(registro)
        sql= "INSERT INTO dados (id, dia, hora, hum, led, lux, temp) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql, registro)
        connection.commit()
        registro.clear()
connection.close()'''
        
#para enviar os registros que possuem "." um ponto na sua formatação
'''for key, list in data.items():
    x=str(list.get('datetime'))
    if (len(x) > 12):
        x = x.split('.')
        z=str(x[2]+'-'+x[1]+'-'+x[0])
        y=str(x[3]+':'+x[4]+':'+x[5])
        registro.append((str(key),
                        z,
                        y,
                        list.get('hum'),
                        list.get('ledDiff'),
                        list.get('lux'),
                        list.get('temp')
        ))
        print(registro)
        sql= "INSERT INTO dados (id, dia, hora, hum, led, lux, temp) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        cursor.executemany(sql, registro)
        connection.commit()
        registro.clear()
connection.close()'''
#joga pro terminal do python os aquivos
'''sql = "SELECT * FROM dados"
cursor.execute(sql)

result=cursor.fetchall()

for i in result:
    print(i)
connection.close()'''

#contador de registros dentro do arquivo .json
'''t=0
for key, list in data.items():
    t=t+1
print("O arquivo .json possue:",t," registros.")
connection.close()'''

