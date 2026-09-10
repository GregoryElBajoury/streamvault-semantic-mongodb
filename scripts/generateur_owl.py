import os

SCHEMA_OWL_COMPLET = """<?xml version="1.0"?>
<rdf:RDF xmlns="http://www.example.org/cinema#"
     xml:base="http://www.example.org/cinema"
     xmlns:owl="http://www.w3.org/2002/07/owl#"
     xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
     xmlns:xml="http://www.w3.org/XML/1998/namespace"
     xmlns:xsd="http://www.w3.org/2001/XMLSchema#"
     xmlns:rdfs="http://www.w3.org/2000/01/rdf-schema#">
    <owl:Ontology rdf:about="http://www.example.org/cinema"/>

    <!-- CLASSES -->
    <owl:Class rdf:about="#Personne"/>
    <owl:Class rdf:about="#Acteur">
        <rdfs:subClassOf rdf:resource="#Personne"/>
    </owl:Class>
    <owl:Class rdf:about="#Realisateur">
        <rdfs:subClassOf rdf:resource="#Personne"/>
    </owl:Class>
    <owl:Class rdf:about="#Film"/>
    <owl:Class rdf:about="#Genre"/>
    <owl:Class rdf:about="#Studio"/>

    <!-- OBJECT PROPERTIES -->
    <owl:ObjectProperty rdf:about="#aJoueDans">
        <rdfs:domain rdf:resource="#Acteur"/>
        <rdfs:range rdf:resource="#Film"/>
        <owl:inverseOf rdf:resource="#aPourActeur"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#aPourActeur">
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Acteur"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#aRealise">
        <rdfs:domain rdf:resource="#Realisateur"/>
        <rdfs:range rdf:resource="#Film"/>
        <owl:inverseOf rdf:resource="#estRealisePar"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#estRealisePar">
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Realisateur"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#aPourGenre">
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Genre"/>
        <owl:inverseOf rdf:resource="#estDuGenre"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#estDuGenre">
        <rdfs:domain rdf:resource="#Genre"/>
        <rdfs:range rdf:resource="#Film"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#estProduitPar">
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Studio"/>
        <owl:inverseOf rdf:resource="#aProduit"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#aProduit">
        <rdfs:domain rdf:resource="#Studio"/>
        <rdfs:range rdf:resource="#Film"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#estSuiteDe">
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Film"/>
        <owl:inverseOf rdf:resource="#aPourSuite"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#aPourSuite">
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="#Film"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#estFilialeDe">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#TransitiveProperty"/>
        <rdfs:domain rdf:resource="#Studio"/>
        <rdfs:range rdf:resource="#Studio"/>
        <owl:inverseOf rdf:resource="#aPourFiliale"/>
    </owl:ObjectProperty>
    <owl:ObjectProperty rdf:about="#aPourFiliale">
        <rdfs:domain rdf:resource="#Studio"/>
        <rdfs:range rdf:resource="#Studio"/>
    </owl:ObjectProperty>

    <!-- DATATYPE PROPERTIES -->
    <owl:DatatypeProperty rdf:about="#aPourTitre">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#FunctionalProperty"/>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>
    <owl:DatatypeProperty rdf:about="#aPourAnnee">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#FunctionalProperty"/>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#integer"/>
    </owl:DatatypeProperty>
    <owl:DatatypeProperty rdf:about="#aPourNoteIMDB">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#FunctionalProperty"/>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#float"/>
    </owl:DatatypeProperty>
    <owl:DatatypeProperty rdf:about="#aPourIdentifiantIMDB">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#FunctionalProperty"/>
        <rdfs:domain rdf:resource="#Film"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>
    <owl:DatatypeProperty rdf:about="#aPourNom">
        <rdf:type rdf:resource="http://www.w3.org/2002/07/owl#FunctionalProperty"/>
        <rdfs:domain rdf:resource="#Personne"/>
        <rdfs:range rdf:resource="http://www.w3.org/2001/XMLSchema#string"/>
    </owl:DatatypeProperty>

    <!-- INDIVIDUALS DU BRIEF -->
    <Realisateur rdf:about="#ChristopherNolan">
        <aPourNom>Christopher Nolan</aPourNom>
        <aRealise rdf:resource="#Inception"/>
    </Realisateur>
    <Acteur rdf:about="#LeonardoDiCaprio">
        <aPourNom>Leonardo DiCaprio</aPourNom>
        <aJoueDans rdf:resource="#Inception"/>
    </Acteur>
    <Film rdf:about="#Inception">
        <aPourTitre>Inception</aPourTitre>
        <aPourAnnee rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">2010</aPourAnnee>
        <aPourNoteIMDB rdf:datatype="http://www.w3.org/2001/XMLSchema#float">8.8</aPourNoteIMDB>
        <aPourIdentifiantIMDB>tt1375666</aPourIdentifiantIMDB>
        <aPourGenre rdf:resource="#ActionGenre"/>
        <estProduitPar rdf:resource="#WarnerBros"/>
    </Film>
    <Film rdf:about="#Casablanca">
        <aPourTitre>Casablanca</aPourTitre>
        <aPourAnnee rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">1942</aPourAnnee>
    </Film>
    <Genre rdf:about="#ActionGenre"/>
    <Genre rdf:about="#DrameGenre"/>
    <Studio rdf:about="#WarnerBros">
        <estFilialeDe rdf:resource="#WarnerBrosGroup"/>
    </Studio>
    <Studio rdf:about="#WarnerAnimation">
        <estFilialeDe rdf:resource="#WarnerBros"/>
    </Studio>
    <Studio rdf:about="#WarnerBrosGroup"/>
</rdf:RDF>
"""

def afficher_guide_manuel():
    print("\n" + "="*50)
    print(" GUIDE MANUEL - ÉTAPES DU BRIEF (WebProtégé)")
    print("="*50)
    print("1. Classes : Créer Personne, Acteur (sous-classe), Realisateur (sous-classe), Film, Genre, Studio.")
    print("2. Object Properties : Créer les 6 relations avec Domain, Range, et Inverse property (ex: aJoueDans <-> aPourActeur). Marquer 'estFilialeDe' comme Transitive !")
    print("3. Data Properties : Créer aPourTitre, aPourAnnee, aPourNoteIMDB, aPourIdentifiantIMDB, aPourNom (toutes Functional).")
    print("4. Individus : Créer les 9 individus (Christopher Nolan, Leonardo DiCaprio, Inception, Casablanca, ActionGenre, DrameGenre, WarnerBros, Warner Animation, WarnerBrosGroup)[cite: 2].")
    print("5. Property assertions : Relier Christopher Nolan -> aRealise -> Inception, etc.[cite: 2]")
    print("="*50)
    input("\nAppuie sur Entrée pour revenir au menu principal...")

def generer_individu_interactif():
    while True:
        print("\n" + "="*50)
        print(" GÉNÉRATEUR DE BLOCS INDIVIDUS (OWL/XML)")
        print("="*50)
        print("1. Créer un Film")
        print("2. Créer un Réalisateur / Acteur")
        print("3. Créer un Studio")
        print("4. Créer un Genre")
        print("0. ⬅ Retour au menu principal")
        
        choix = input("\nChoisis une option : ").strip()
        
        if choix == "0":
            break
        elif choix == "1":
            nom_id = input("Identifiant du film (ex: Inception) : ").strip()
            titre = input("Titre : ").strip()
            annee = input("Année (ex: 2010) : ").strip()
            note = input("Note IMDB (ex: 8.8) : ").strip()
            id_imdb = input("Identifiant IMDB (ex: tt1375666) : ").strip()
            
            xml = f"""    <Film rdf:about="#{nom_id}">
        <aPourTitre>{titre}</aPourTitre>"""
            if annee:
                xml += f'\n        <aPourAnnee rdf:datatype="http://www.w3.org/2001/XMLSchema#integer">{annee}</aPourAnnee>'
            if note:
                xml += f'\n        <aPourNoteIMDB rdf:datatype="http://www.w3.org/2001/XMLSchema#float">{note}</aPourNoteIMDB>'
            if id_imdb:
                xml += f'\n        <aPourIdentifiantIMDB>{id_imdb}</aPourIdentifiantIMDB>'
            xml += "\n    </Film>"
            print("\n--- Bloc OWL/XML généré ---\n" + xml)
            input("\nAppuie sur Entrée pour continuer...")
            
        elif choix == "2":
            type_pers = input("S'agit-il d'un Acteur ou d'un Realisateur ? ").strip()
            nom_id = input("Identifiant (ex: ChristopherNolan) : ").strip()
            nom_complet = input("Nom et Prénom : ").strip()
            
            xml = f"""    <{type_pers} rdf:about="#{nom_id}">
        <aPourNom>{nom_complet}</aPourNom>
    </{type_pers}>"""
            print("\n--- Bloc OWL/XML généré ---\n" + xml)
            input("\nAppuie sur Entrée pour continuer...")

        elif choix == "3":
            nom_id = input("Identifiant du studio (ex: WarnerBros) : ").strip()
            filiale_de = input("Est filiale de (laisser vide si aucun) : ").strip()
            
            xml = f"""    <Studio rdf:about="#{nom_id}">"""
            if filiale_de:
                xml += f'\n        <estFilialeDe rdf:resource="#{filiale_de}"/>'
            xml += "\n    </Studio>"
            print("\n--- Bloc OWL/XML généré ---\n" + xml)
            input("\nAppuie sur Entrée pour continuer...")

        elif choix == "4":
            nom_id = input("Identifiant du genre (ex: ActionGenre) : ").strip()
            xml = f'    <Genre rdf:about="#{nom_id}"/>'
            print("\n--- Bloc OWL/XML généré ---\n" + xml)
            input("\nAppuie sur Entrée pour continuer...")

        else:
            print("Option invalide, réessaie.")

def main():
    while True:
        print("\n" + "="*50)
        print(" COMPAGNON PÉDAGOGIQUE - BRIEF CINÉMA (OWL/RDF)")
        print("="*50)
        print("1. Afficher le guide pour tout construire à la main (WebProtégé)")
        print("2. Utiliser le générateur interactif d'individus (OWL/XML)")
        print("3. Exporter le fichier OWL complet pré-rempli (avec tout le brief)")
        print("4. Quitter")
        
        mode = input("\nQue veux-tu faire ? (1-4) : ").strip()
        
        if mode == "1":
            afficher_guide_manuel()
        elif mode == "2":
            generer_individu_interactif()
        elif mode == "3":
            nom_fichier = "cinema_complet.owl"
            with open(nom_fichier, "w", encoding="utf-8") as f:
                f.write(SCHEMA_OWL_COMPLET)
            print(f"\n✅ Fichier '{nom_fichier}' généré avec succès dans le dossier !")
            print("Tu peux directement l'importer dans WebProtégé ou le tester sur WebVOWL[cite: 2].")
            input("\nAppuie sur Entrée pour continuer...")
        elif mode == "4":
            print("\nÀ bientôt et bon courage pour le brief !")
            break
        else:
            print("Choix non reconnu, réessaie.")

if __name__ == "__main__":
    main()