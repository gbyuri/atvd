import json 
with open('data.json') as data_json:
    data=json.load(data_json)
    
    

import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',user='root',password='x',database='x')
with connection:
    with connection.cursor() as cursor:
        print("Connected!")
        
        
 for key, list in data.items():
    sql= "INSERT INTO dados (id, data_hora, hum,led, lux, temp) VALUES (%s, %s, %s, %s, %s, %s)"
    d1=(str(key),
        int(list.get('datetime')),
        list.get('hum'),
        list.get('ledDiff'),
        list.get('lux'),
        list.get('temp'))
    cursor.execute(sql, d1)
    connection.commit()
    print("INSERTED")
        
