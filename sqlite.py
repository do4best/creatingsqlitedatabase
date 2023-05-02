import  sqlite3

items_names={'01',"Beakers 500ml","17-04-23"}
connect = sqlite3.connect('myfile.db')
cur = connect.cursor()
cur.execute(''' insert into  ITEMS(ID ,item_name ,item_date VALUES (?,?,?),items_names)''')
cur.close()
connect.close()