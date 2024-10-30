import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
)

mycursor = mydb.cursor()

mycursor.execute("CREATE DATABASE IF NOT EXISTS Animali")
mycursor.execute("USE Animali")
mycursor.execute("CREATE TABLE IF NOT EXISTS Mammiferi (Id INT AUTO_INCREMENT PRIMARY KEY, Nome_Proprio VARCHAR(50),Razza VARCHAR(50),Peso INT,Eta INT)")