import mysql.connector

# Funzione per la connessione al database 'Animali'
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Animali"
    )

# Funzione per inserire un nuovo animale nel database
def insert_animal():
    nome, razza, peso, eta = get_animal_data()
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, (nome, razza, peso, eta))
    mydb.commit()
    print("Animale inserito con successo!")
    mydb.close()

# Funzione per visualizzare tutti gli animali
def display_all_animals():
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Mammiferi")
    animali = mycursor.fetchall()
    print("\nAnimali presenti nel database:")
    for animale in animali:
        print(f"Id: {animale[0]}, Nome: {animale[1]}, Razza: {animale[2]}, Peso: {animale[3]} kg, Età: {animale[4]} anni")
    mydb.close()

# Funzione per eliminare un animale tramite l'ID
def delete_animal():
    id_to_delete = input("Inserisci l'ID dell'animale da eliminare: ")
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "DELETE FROM Mammiferi WHERE Id = %s"
    mycursor.execute(sql, (id_to_delete,))
    mydb.commit()
    if mycursor.rowcount > 0:
        print("Animale eliminato con successo.")
    else:
        print("Nessun animale trovato con l'ID specificato.")
    mydb.close()

# Funzione per modificare i dati di un animale tramite l'ID
def update_animal():
    id_to_update = input("Inserisci l'ID dell'animale da modificare: ")
    nome, razza, peso, eta = get_animal_data()
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "UPDATE Mammiferi SET Nome_Proprio = %s, Razza = %s, Peso = %s, Eta = %s WHERE Id = %s"
    mycursor.execute(sql, (nome, razza, peso, eta, id_to_update))
    mydb.commit()
    if mycursor.rowcount > 0:
        print("Animale aggiornato con successo.")
    else:
        print("Nessun animale trovato con l'ID specificato.")
    mydb.close()

# Funzione per chiedere i dati all'utente e verificare gli input numerici
def get_animal_data():
    nome = input("Inserisci il nome dell'animale: ")
    razza = input("Inserisci la razza dell'animale: ")

    # Verifica che 'Peso' sia un numero intero
    while True:
        try:
            peso = int(input("Inserisci il peso dell'animale (numero intero): "))
            break
        except ValueError:
            print("Errore: il peso deve essere un numero intero.")

    # Verifica che 'Eta' sia un numero intero
    while True:
        try:
            eta = int(input("Inserisci l'età dell'animale (numero intero): "))
            break
        except ValueError:
            print("Errore: l'età deve essere un numero intero.")

    return nome, razza, peso, eta

# Menu principale
def main_menu():
    while True:
        print("\nMenù Utente:")
        print("Premi 1 per inserire un nuovo animale")
        print("Premi 2 per visualizzare tutti gli animali")
        print("Premi 3 per eliminare un animale")
        print("Premi 4 per modificare un animale")
        print("Premi 0 per uscire")

        scelta = input("Seleziona un'opzione: ")

        if scelta == "1":
            insert_animal()
        elif scelta == "2":
            display_all_animals()
        elif scelta == "3":
            delete_animal()
        elif scelta == "4":
            update_animal()
        elif scelta == "0":
            print("Uscita dal programma.")
            break
        else:
            print("Opzione non valida. Riprova.")

# Avvio del programma
main_menu()
