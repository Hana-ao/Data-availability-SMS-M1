# Données de la Revue Systématique de Littérature (SMS) - Mémoire de M1
## Critères d'évaluation d'une démarche DevOps : panorama des dimensions de qualité, performance et sécurité

Ce dépôt contient les données et les fichiers de travail utilisés pour la réalisation du mémoire de Master 1, intitulé "Critères d'évaluation d'une démarche DevOps : panorama des dimensions de qualité, performance et sécurité". Ce mémoire a été réalisé dans le cadre du Master MIAGE (apprentissage) de l'Université Paris Nanterre.

L'objectif principal du mémoire était de réaliser une cartographie exploratoire des critères d'évaluation d'une démarche DevOps, identifiés à partir d'une revue systématique de la littérature (Systematic Mapping Study - SMS) portant sur 20 articles scientifiques récents.

📂 Contenu du dépôt

- **Grille-d'extraction-finale.xlsx** : Grille d'extraction brute (272 critères, L2 à L273) issus des articles analysés.
- **csv-format-Grille-d'extraction-finale.csv** : Version CSV de la grille d'extraction finale, pour analyses automatisées.
- **generate-clusters.py** : Script Python utilisé pour regrouper automatiquement les critères sémantiquement équivalents en clusters thématiques (étape 2).
- **Clusters_par_critereEN.xlsx** : Résultat du script : critères regroupés selon leur intitulé EN, avec les lignes correspondantes.
- **Clusters_par_critereEN-phase-préli.xlsx** : Début de classification manuelle des critères, à l'aide du fichier Clusters_par_critereEN.xlsx.
- **Grille_SMS_avec_colonnes_categorisees.xlsx** : Fichier aidant à la réalisation de nombreux graphiques, ainsi qu'aux sections 3.5, 3.6.

- Workflow du projet

Étape 1 : Extraction des critères bruts (Grille-d'extraction-finale.xlsx)

↓

Étape 2 : Regroupement automatique des critères (generate-clusters.py → Clusters_par_critereEN.xlsx)

↓

Étape 2' : Tentative manuelle de classification (Clusters_par_critereEN-phase-préli.xlsx)

↓

Étape 3 : Classification finale 

↓

La classification finale des 16 catégories est disponible dans l'annexe A du mémoire. 


Étape 4 : Identification des "top-critères", les plus mentionnés (à l'aide de : Grille_SMS_avec_colonnes_categorisees.xlsx + Annexe A)

↓

Analyse des top-critères et des contributions (Sections 3.5 et 3.6 du mémoire : 3.5 Identification des sous-concepts clés prédominants (“Top Critères”), 3.6 Qualité et nature des contributions des sources pour les sous-concepts clés)


- Références

Ce travail s’appuie notamment sur :
	•	Kitchenham et Charters (2007) – Guidelines for performing Systematic Literature Reviews in Software Engineering
	•	Petersen et al. (2008) – Systematic Mapping Studies in Software Engineering

- Utilisation
Téléchargez le dépôt ou clonez-le :

      git clone https://github.com/Hana-ao/Data-availability-SMS-M1.git

Exécutez le script de regroupement dans un environnement Python 3 :

    python generate-clusters.py

- Contact

Pour toute question ou suggestion :
44013266@parisnanterre.fr


