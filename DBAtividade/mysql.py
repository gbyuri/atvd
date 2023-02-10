import datetime
import json
import pymysql.cursors

with open('logger.json') as data_json:
    data = json.load(data_json)

registro={'id':'',
          'dia':'',
          'hora':'',
          'hum':'',
          'led':'',
          'lux':'',
          'temp':''}

connection = pymysql.connect(host='127.0.0.1',
                             user='root',
                             password='123456789',
                             database='atividadeplanta')
cursor = connection.cursor()
print("Connected!")
for key, list in data.items():
    x=str(list.get('datetime'))
    if len(x) > 12:
        x = x.split('.')
        registro['dia']=x[2],x[1],x[0]
        registro['hora']=x[5],x[4],x[3]
        registro['id']=str(key)
        registro['hum']=list.get('hum')
        registro['led']=list.get('ledDiff')
        registro['lux']=list.get('lux')
        registro['temp']=list.get('temp')
        sql= "INSERT INTO dados (id) VALUES (%s)"
        d1=registro['id']
        cursor.execute(sql, d1)
        connection.commit()

'''sql = "SELECT * FROM teste"
cursor.execute(sql)

result=cursor.fetchall()

for i in result:
    print(i)'''
