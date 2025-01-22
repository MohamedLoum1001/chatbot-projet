from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Arborescence des questions et réponses
faq = {
    "algorithmique": {
        "description": "L'art de concevoir des algorithmes pour résoudre des problèmes complexes.",
        "example": "Exemple : Algorithme de tri par insertion.",
        "related": {
            "c'est quoi un algorithme ?": "Un algorithme est une suite d'instructions définies pour résoudre un problème.",
            "quels sont les types d'algorithmes ?": "Les types incluent les algorithmes de tri, de recherche, et de récursivité."
        }
    },
    "programmation": {
        "description": "L'écriture d'instructions pour que l'ordinateur exécute des tâches.",
        "example": "Exemple : Une boucle for en Python.",
        "related": {
            "qu'est-ce qu'un langage de programmation ?": "C'est un langage utilisé pour écrire des programmes informatiques.",
            "comment débuter en programmation ?": "Commencez par apprendre un langage simple comme Python."
        }
    },
    "langage go": {
        "description": "Un langage de programmation rapide et simple développé par Google.",
        "example": "Exemple : package main; import \"fmt\"; func main() { fmt.Println(\"Hello, World!\") }",
        "related": {}
    },
    "langage python": {
        "description": "Un langage généraliste très utilisé en science des données.",
        "example": "Exemple : print(\"Bonjour le monde !\")",
        "related": {}
    },
    "langage java": {
        "description": "Un langage orienté objet utilisé pour les applications d'entreprise.",
        "example": "Exemple : public class Main { public static void main(String[] args) { System.out.println(\"Hello, World!\"); }}",
        "related": {}
    },
    "infrastructure": {
        "description": "Les bases physiques et logicielles pour exécuter des applications.",
        "example": "Exemple : Configuration d'un serveur Apache.",
        "related": {}
    },
    "sécurité": {
        "description": "Protéger les systèmes et les données contre les menaces.",
        "example": "Exemple : Chiffrement AES.",
        "related": {}
    },
    "base de données": {
        "description": "Organisation et gestion des données.",
        "example": "Exemple : SELECT * FROM etudiants;",
        "related": {}
    }
}

@app.route('/')
def home():
    """Affiche la page principale avec tous les domaines."""
    return render_template('index.html', subjects=faq.keys())

@app.route('/ask', methods=['POST'])
def ask_question():
    """Gère les questions des étudiants."""
    data = request.json
    user_question = data.get('subject', '').lower()

    # Vérifier si le sujet est dans la FAQ
    if user_question in faq:
        related_questions = faq[user_question]["related"]
        related_text = "\n".join([f"- {q}" for q in related_questions.keys()]) if related_questions else "Aucune sous-question disponible."
        
        return jsonify({
            "status": "success",
            "data": {
                "name": user_question.capitalize(),
                "description": faq[user_question]["description"],
                "example": faq[user_question]["example"],
                "related": related_text
            }
        })
    else:
        return jsonify({"status": "error", "message": "Désolé, je n'ai pas d'informations sur ce sujet."})

if __name__ == "__main__":
    app.run(debug=True)
