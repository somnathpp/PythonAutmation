import mysql.connector as mqc

con=mqc.connect(host="localhost",user="root",password="root",database="saki")
cursor=con.cursor()
cursor.execute("insert into actor values(201,'somnath','potdar','2006-02-15 04:34:33')")
con.commit()
con.close()