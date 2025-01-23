from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Données FAQ
faq = [
    {
        "question": "Algorithmique",
        "answer": "L'art de concevoir des algorithmes pour résoudre des problèmes complexes.",
        "follow_up": [
            {
                "question": "C'est quoi un algorithme ?",
                "answer": "Un algorithme est une suite d'instructions définies pour résoudre un problème.",
            },
            {
                "question": "quels sont les types d'algorithmes ?",
                "answer": "Les types incluent les algorithmes de tri, de recherche, et de récursivité.",
            },
            {
                "question": "Qu'est-ce que la complexité algorithmique ?",
                "answer": "La complexité algorithmique est une mesure de la quantité de ressources (temps et espace) nécessaires à l'exécution d'un algorithme.",
            }
        ]
    },
    {
        "question": "programmation",
        "answer": "L'écriture d'instructions pour que l'ordinateur exécute des tâches.",
        "follow_up": [
            {
                "question": "Qu'est-ce qu'un langage de programmation ?",
                "answer": "C'est un langage utilisé pour écrire des programmes informatiques.",
            },
            {
                "question": "Comment débuter en programmation ?",
                "answer": "Commencez par apprendre un langage simple comme Python.",
            },
            {
                "question": "Quelle est la différence entre compilé et interprété ?",
                "answer": "Un langage compilé est transformé en code machine, alors qu'un langage interprété est exécuté ligne par ligne.",
            }
        ]
    },
    {
        "question": "Langage Go",
        "answer": "Un langage de programmation rapide et simple développé par Google.",
        "follow_up": [
            {
                "question": "Quels sont les avantages de Go ?",
                "answer": "Simplicité, performance, et concurrence native.",
            },
            {
                "question": "Où utiliser Go",
                "answer": "Pour les systèmes distribués, les serveurs web, et les outils CLI.",
            },
            {
                "question": "Quelle est la différence entre Go et Python ?",
                "answer": "Go est conçu pour la performance et la simplicité, tandis que Python est plus orienté vers la polyvalence et l'analyse de données.",
            }
        ]
    },
    {
        "question": "Langage Python",
        "answer": "Un langage généraliste très utilisé en science des données.",
        "follow_up": [
            {
                "question": "Pourquoi Python est populaire ?",
                "answer": "Python est facile à apprendre et possède une grande communauté.",
            },
            {
                "question": "Où Python est-il utilisé ?",
                "answer": "Dans le développement web, les données, et l'intelligence artificielle.",
            },
            {
                "question": "Qu'est-ce qu'une bibliothèque en Python ?",
                "answer": "Une bibliothèque est un ensemble de modules et de fonctions prêtes à l'emploi pour effectuer des tâches spécifiques.",
            }
        ]
    },
    {
        "question": "Langage Java",
        "answer": "Un langage orienté objet utilisé pour les applications d'entreprise.",
        "follow_up": [
            {
                "question": "Qu'est-ce que Java ?",
                "answer": "Java est un langage portable et robuste.",
            },
            {
                "question": "qu'est-ce que la JVM ?",
                "answer": "La JVM (Java Virtual Machine) est une machine virtuelle qui exécute le bytecode Java.",
            },
            {
                "question": "Où utilise-t-on Java ?",
                "answer": "Java est utilisé pour les applications mobiles, les logiciels d'entreprise, et les serveurs web.",
            }
        ]
    },
     {
        "question": "Infrastructure",
        "answer": "Les bases physiques et logicielles pour exécuter des applications.",
        "follow_up": [
            {
                "question": "Qu'est-ce que l'infrastructure informatique ?",
                "answer": "C'est l'ensemble des composants nécessaires pour exécuter des applications.",
            },
            {
                "question": "Quels outils pour gérer l'infrastructure ?",
                "answer": "Docker, Kubernetes, Terraform.",
            },
            {
                "question": "Qu'est-ce qu'un serveur cloud ?",
                "answer": "Un serveur cloud est une ressource de calcul virtuelle hébergée sur internet.",
            }
        ]
    },
    {
        "question": "Sécurité",
        "answer": "Protéger les systèmes et les données contre les menaces.",
        "follow_up": [
            {
                "question": "Qu'est-ce que le chiffrement ?",
                "answer": "C'est une méthode pour sécuriser les données en les rendant illisibles sans une clé spécifique.",
            },
            {
                "question": "Qu'est-ce qu'une attaque par phishing ?",
                "answer": "C'est une tentative de vol de données en se faisant passer pour une entité fiable.",
            },
            {
                "question": "Comment renforcer la sécurité d'un mot de passe ?",
                "answer": "Utilisez des mots de passe longs, complexes, et uniques pour chaque compte.",
            }
        ]
    },
    {
        "question": "Base de données",
        "answer": "Organisation et gestion des données.",
        "follow_up": [
            {
                "question": "Qu'est-ce qu'une base de données ?",
                "answer": "C'est un ensemble structuré de données accessibles via un logiciel.",
            },
            {
                "question": "Quels sont les types de bases de données ?",
                "answer": "Bases relationnelles (SQL) et non relationnelles (NoSQL).",
            },
            {
                "question": "Qu'est-ce qu'une clé primaire ?",
                "answer": "Une clé primaire est un identifiant unique pour chaque enregistrement dans une table.",
            }
        ]
    },
]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/faq', methods=['GET'])
def get_faq():
    return jsonify(faq)

if __name__ == "__main__":
    app.run(debug=True)
