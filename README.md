Markdown
# StreamVault - NoSQL & Sémantique Cinéma

Ce dépôt regroupe les travaux pratiques et le code associés au brief **StreamVault**, combinant l'interrogation de bases de données NoSQL et la modélisation d'ontologies OWL/RDF.

##  Arborescence du Projet

```
streamvault-semantic-mongodb/
├── assets/
│   ├── Anatomie_d_une_commande_Mongosh_CLI.pdf
│   ├── Brief_mongodb_1_partie1.pdf
│   ├── brief1_partie2_ontologie_owl_rdf.pdf
│   ├── MongoDB_Ontologies_OWLRDF.pdf
├── ontology/
│   ├── cinema.owl
│   ├── cinema_inferred.owl
├── scripts/
│   └── generateur_owl.py
├── .gitignore
├── livres.json
└── README.md
```

## Documentation et Travail Global


* **Rapport Complet** : Le document [MongoDB_Ontologies_OWLRDF.pdf](./assets/MongoDB_Ontologies_OWLRDF.pdf) regroupe l'ensemble du travail de réalisation pour la Partie 1 (NoSQL) et la Partie 2 (Sémantique).

* **Énoncés Officiels** : Les sujets des deux parties sont disponibles dans [Brief_mongodb_1_partie1.pdf](./assets/Brief_mongoDB_1_partie1.pdf) et [brief1_partie2_ontologie_owl_rdf.pdf](./assets/brief1_partie2_ontologie_owl_rdf.pdf).

* **Mémo Technique** : Les notes personnelles sur les commandes `mongosh` se trouvent dans [Anatomie_d_une_commande_Mongosh_CLI.pdf](./assets/Anatomie_d_une_commande_Mongosh_CLI.pdf).


## Partie 1 : Requêtes NoSQL & MongoDB

* Les jeux de données de test ([livres.json](./livres.json)) et les archives associées servent de support, tandis que la mise en œuvre et les solutions des requêtes NoSQL sont détaillées dans [MongoDB_Ontologies_OWLRDF.pdf](./assets/MongoDB_Ontologies_OWLRDF.pdf).


## Partie 2 : Ontologie et Sémantique (OWL / RDF)

* Implémentation de l'ontologie du cinéma (classes, propriétés d'objet et de données, et gestion de la transitivité sur `estFilialeDe`) réalisée sur l'interface puis via script `.owl` stocké dans le dossier [ontology/](./ontology/) ([cinema.owl](./ontology/cinema.owl), [cinema_inferred.owl](./ontology/cinema_inferred.owl)). La démarche et les étapes de modélisation sont documentées dans [MongoDB_Ontologies_OWLRDF.pdf](./assets/MongoDB_Ontologies_OWLRDF.pdf).


## Visualisation et Validation

* Les graphes d'ontologie associés aux différents modèles ont été entièrement vérifiés et validés via **WebVOWL** pour l'inspection visuelle des taxonomies et relations, ainsi que via **WebProtégé** pour l'exécution des raisonneurs sémantiques. L'ensemble des captures, des rapports de validation et des détails méthodologiques de cette phase est documenté dans le fichier [MongoDB_Ontologies_OWLRDF.pdf](./assets/MongoDB_Ontologies_OWLRDF.pdf).


## Outil Personnel en béta (Compagnon Pédagogique)

* **Rôle et fonctionnement** : Développé dans le script `scripts/generateur_owl.py`, cet outil interactif en ligne de commande sert de compagnon d'apprentissage pour structurer et manipuler les ontologies OWL/RDF[cite: 1]. Il s'articule autour d'un menu principal proposant trois fonctionnalités clés : l'affichage d'un guide méthodologique pas à pas, un générateur dynamique de fragments de code OWL/XML pour les individus (films, réalisateurs, acteurs, studios, genres), et l'export direct d'un fichier complet pré-rempli (`cinema_complet.owl`) intégrant l'ensemble des données du brief[cite: 1].
Etant encore en phase de développement il pourrait ne pas être 100% fonctionnel.

* **Comment l'exécuter** : Place-toi à la racine du dépôt dans ton terminal, puis lance la commande suivante :
  ```bash
```python
python3 scripts/generateur_owl.py

```
