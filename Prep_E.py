import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="Animali"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM Mammiferi WHERE Peso > 2"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)