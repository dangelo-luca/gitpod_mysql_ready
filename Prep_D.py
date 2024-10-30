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
def insert_animal(nome, razza, peso, eta):
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    sql = "INSERT INTO Mammiferi (Nome_Proprio, Razza, Peso, Eta) VALUES (%s, %s, %s, %s)"
    mycursor.execute(sql, (nome, razza, peso, eta))
    mydb.commit()
    print("Animale inserito con successo!")
    mydb.close()

# Funzione per visualizzare tutti gli animali presenti nella tabella 'Mammiferi'
def display_all_animals():
    mydb = connect_to_db()
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM Mammiferi")
    animali = mycursor.fetchall()
    print("\nAnimali presenti nel database:")
    for animale in animali:
        print(f"Id: {animale[0]}, Nome: {animale[1]}, Razza: {animale[2]}, Peso: {animale[3]} kg, Età: {animale[4]} anni")
    mydb.close()

# Funzione per chiedere i dati all'utente e verificare gli input numerici
def get_animal_data():
    nome = input("Inserisci il nome dell'animale: ")
    razza = input("Inserisci la razza dell'animale: ")

    # Controllo per il campo 'Peso'
    while True:
        try:
            peso = int(input("Inserisci il peso dell'animale (numero intero): "))
            break
        except ValueError:
            print("Errore: il peso deve essere un numero intero.")

    # Controllo per il campo 'Età'
    while True:
        try:
            eta = int(input("Inserisci l'età dell'animale (numero intero): "))
            break
        except ValueError:
            print("Errore: l'età deve essere un numero intero.")

    return nome, razza, peso, eta

# Programma principale: inserimento e verifica
for i in range(5):
    risposta = input(f"Vuoi inserire un nuovo animale? (sì/no) [{i+1}/5]: ").strip().lower()
    if risposta == "sì":
        nome, razza, peso, eta = get_animal_data()
        insert_animal(nome, razza, peso, eta)

# Visualizzazione degli animali nel database
display_all_animals()
