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
            "comment débuter en programmation ?": "Commencez par apprendre un langage simple comme Python.",
            "quelle est la différence entre compilé et interprété ?": "Un langage compilé est transformé en code machine, alors qu'un langage interprété est exécuté ligne par ligne."
        }
    },
    "langage go": {
        "description": "Un langage de programmation rapide et simple développé par Google.",
        "example": "Exemple : package main; import \"fmt\"; func main() { fmt.Println(\"Hello, World!\") }",
        "related": {
            "quels sont les avantages de Go ?": "Simplicité, performance, et concurrence native.",
            "où utiliser Go ?": "Pour les systèmes distribués, les serveurs web, et les outils CLI.",
            "quelle est la différence entre Go et Python ?": "Go est conçu pour la performance et la simplicité, tandis que Python est plus orienté vers la polyvalence et l'analyse de données."
        }
    },
    "langage python": {
        "description": "Un langage généraliste très utilisé en science des données.",
        "example": "Exemple : print(\"Bonjour le monde !\")",
        "related": {
            "pourquoi Python est populaire ?": "Python est facile à apprendre et possède une grande communauté.",
            "où Python est-il utilisé ?": "Dans le développement web, les données, et l'intelligence artificielle.",
            "qu'est-ce qu'une bibliothèque en Python ?": "Une bibliothèque est un ensemble de modules et de fonctions prêtes à l'emploi pour effectuer des tâches spécifiques."
        }
    },
    "langage java": {
        "description": "Un langage orienté objet utilisé pour les applications d'entreprise.",
        "example": "Exemple : public class Main { public static void main(String[] args) { System.out.println(\"Hello, World!\"); }}",
        "related": {
            "qu'est-ce que Java ?": "Java est un langage portable et robuste.",
            "qu'est-ce que la JVM ?": "La JVM (Java Virtual Machine) est une machine virtuelle qui exécute le bytecode Java.",
            "où utilise-t-on Java ?": "Java est utilisé pour les applications mobiles, les logiciels d'entreprise, et les serveurs web."
        }
    },
    "infrastructure": {
        "description": "Les bases physiques et logicielles pour exécuter des applications.",
        "example": "Exemple : Configuration d'un serveur Apache.",
        "related": {
            "qu'est-ce que l'infrastructure informatique ?": "C'est l'ensemble des composants nécessaires pour exécuter des applications.",
            "quels outils pour gérer l'infrastructure ?": "Docker, Kubernetes, Terraform.",
            "qu'est-ce qu'un serveur cloud ?": "Un serveur cloud est une ressource de calcul virtuelle hébergée sur internet."
        }
    },
    "sécurité": {
        "description": "Protéger les systèmes et les données contre les menaces.",
        "example": "Exemple : Chiffrement AES.",
        "related": {
            "qu'est-ce que le chiffrement ?": "C'est une méthode pour sécuriser les données en les rendant illisibles sans une clé spécifique.",
            "qu'est-ce qu'une attaque par phishing ?": "C'est une tentative de vol de données en se faisant passer pour une entité fiable.",
            "comment renforcer la sécurité d'un mot de passe ?": "Utilisez des mots de passe longs, complexes, et uniques pour chaque compte."
        }
    },
    "base de données": {
        "description": "Organisation et gestion des données.",
        "example": "Exemple : SELECT * FROM etudiants;",
        "related": {
            "qu'est-ce qu'une base de données ?": "C'est un ensemble structuré de données accessibles via un logiciel.",
            "quels sont les types de bases de données ?": "Bases relationnelles (SQL) et non relationnelles (NoSQL).",
            "qu'est-ce qu'une clé primaire ?": "Une clé primaire est un identifiant unique pour chaque enregistrement dans une table."
        }
    }
}

@app.route('/')
def home():
    """Affiche la page principale avec tous les domaines."""
    return render_template('index.html', subjects=list(faq.keys()))  # Conversion en liste pour éviter l'erreur JSON

@app.route('/ask', methods=['POST'])
def ask_question():
    """Gère les questions des étudiants."""
    data = request.json
    user_question = data.get('subject', '').lower()

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

@app.route('/related_question', methods=['POST'])
def related_question():
    """Gère les réponses aux questions liées."""
    data = request.json
    user_question = data.get('question', '').lower()
    
    for subject, content in faq.items():
        if user_question in content["related"]:
            answer = content["related"][user_question]
            return jsonify({
                "status": "success",
                "data": {
                    "question": user_question,
                    "answer": answer
                }
            })
    
    return jsonify({"status": "error", "message": "Désolé, je n'ai pas d'informations sur cette question."})

if __name__ == "__main__":
    app.run(debug=True)
