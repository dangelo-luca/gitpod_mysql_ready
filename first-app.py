from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

# Funzione per connettersi al database
def connect_to_db():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="Animali"
    )

# Rotta per ottenere il contenuto della tabella 'Mammiferi' in formato JSON
@app.route('/api/mammiferi', methods=['GET'])
def get_mammiferi():
    # Connessione al database
    mydb = connect_to_db()
    mycursor = mydb.cursor(dictionary=True)
    
    # Esecuzione della query per selezionare tutti i dati dalla tabella
    mycursor.execute("SELECT * FROM Mammiferi")
    mammiferi = mycursor.fetchall()
    
    # Chiusura delle connessioni
    mycursor.close()
    mydb.close()
    
    # Restituisce i dati in formato JSON
    return jsonify(mammiferi)

if __name__ == '__main__':
    app.run(debug=True)
