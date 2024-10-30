import mysql.connector

# Connessione al database 'Animali'
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="Animali"
)

mycursor = mydb.cursor()


sql = "INSERT INTO Mammiferi (Id, Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s, %s)"
val = [
    ("0","Fido", "Labrador", 30, 5),
    ("1","Micio", "Persiano", 5, 3),
    ("2","Max", "Golden Retriever", 32, 4),
    ("3","Luna", "Bassotto", 9, 2),
    ("4","Leo", "Rottweiler", 40, 6)
]
mycursor.executemany(sql, val)
mydb.commit()

print("Inserimento completato: ", mycursor.rowcount, "animali aggiunti.")

mydb.close()
