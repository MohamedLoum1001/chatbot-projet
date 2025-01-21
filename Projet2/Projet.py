from flask import Flask, request, jsonify, render_template
import mysql.connector
import re

app = Flask(__name__)

def init_db():
    """Initialise la base de données avec des matières."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mouh@med",
        database="school"
    )
    cursor = connection.cursor()

    cursor.execute(''' 
        CREATE TABLE IF NOT EXISTS subjects (
            id INT AUTO_INCREMENT PRIMARY KEY,
            name VARCHAR(255) NOT NULL,
            description TEXT NOT NULL,
            example TEXT NOT NULL
        )
    ''')

    # Insérer des matières si la table est vide
    cursor.execute('SELECT COUNT(*) FROM subjects')
    if cursor.fetchone()[0] == 0:
        subjects = [
            ("Algorithmique", "L'art de concevoir des algorithmes pour résoudre des problèmes complexes.", "Exemple : Algorithme de tri par insertion."),
            ("Programmation", "L'écriture d'instructions pour que l'ordinateur exécute des tâches.", "Exemple : Une boucle for en Python."),
            ("Langage Go", "Un langage de programmation rapide et simple développé par Google.", "Exemple : \npackage main\nimport \"fmt\"\nfunc main() {\n    fmt.Println(\"Hello, World!\")\n}"),
            ("Langage Python", "Un langage généraliste très utilisé en science des données.", "Exemple : \nprint(\"Bonjour le monde !\")"),
            ("Langage Java", "Un langage orienté objet utilisé pour les applications d'entreprise.", "Exemple : \npublic class Main {\n    public static void main(String[] args) {\n        System.out.println(\"Hello, World!\");\n    }\n}"),
            ("Infrastructure", "Les bases physiques et logicielles pour exécuter des applications.", "Exemple : Configuration d'un serveur Apache."),
            ("Sécurité", "Protéger les systèmes et les données contre les menaces.", "Exemple : Chiffrement AES."),
            ("Base de données", "Organisation et gestion des données.", "Exemple : SELECT * FROM etudiants;")
        ]
        cursor.executemany('INSERT INTO subjects (name, description, example) VALUES (%s, %s, %s)', subjects)
    
    connection.commit()
    connection.close()

@app.route('/')
def home():
    """Affiche la page principale avec tous les domaines."""
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mouh@med",
        database="school"
    )
    cursor = connection.cursor()
    cursor.execute('SELECT name FROM subjects')
    subjects = cursor.fetchall()
    connection.close()

    return render_template('index.html', subjects=subjects)

@app.route('/ask', methods=['POST'])
def ask_question():
    """Gère les questions des étudiants."""
    data = request.json
    user_question = data.get('subject', '').lower()

    # Nettoyer la question pour en extraire le sujet
    user_question = re.sub(r'[^\w\s]', '', user_question)  # Supprimer la ponctuation

    # Liste des mots-clés à supprimer (C'est quoi, Qu'est-ce que, etc.)
    keywords = ['cest quoi', 'quest ce que', 'cest', 'quest ce']
    
    # Supprimer les mots-clés de la question
    for keyword in keywords:
        user_question = user_question.replace(keyword, '').strip()

    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mouh@med",
        database="school"
    )
    cursor = connection.cursor()
    
    # Chercher une correspondance exacte dans le nom des matières
    cursor.execute('SELECT name, description, example FROM subjects WHERE LOWER(name) LIKE %s', ('%' + user_question + '%',))
    result = cursor.fetchone()
    connection.close()

    if result:
        return jsonify({
            "status": "success",
            "data": {
                "name": result[0],
                "description": result[1],
                "example": result[2]
            }
        })
    else:
        return jsonify({"status": "error", "message": "Désolé, je n'ai pas d'informations sur ce sujet."})

if __name__ == "__main__":
    init_db()
    app.run(debug=True)
