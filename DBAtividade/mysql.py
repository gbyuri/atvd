import json 
with open('data.json') as data_json:
    data=json.load(data_json)
    
    

import pymysql.cursors
connection = pymysql.connect(host='127.0.0.1',user='root',password='x',database='x')
with connection:
    with connection.cursor() as cursor:
        print("Connected!")
        print(data['-NNDEL_L4QfRInEn5Im6']['datetime'])
        sql = 'INSERT INTO tableteste (dataid) VALUE (%s)'
        cursor.execute(sql,(1))
        
