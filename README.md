# Données de la Revue Systématique de Littérature (SMS) - Mémoire de M1

## Critères d'évaluation d'une démarche DevOps : panorama des dimensions de qualité, performance et sécurité

Ce dépôt contient les données et les fichiers de travail utilisés pour la réalisation du mémoire de Master 1 de **Hana Ouraghene**, intitulé "Critères d'évaluation d'une démarche DevOps : panorama des dimensions de qualité, performance et sécurité". Ce mémoire a été réalisé dans le cadre du Master MIAGE (apprentissage) de l'Université Paris Nanterre.

L'objectif principal du mémoire était de réaliser une cartographie exploratoire des critères d'évaluation d'une démarche DevOps, identifiés à partir d'une revue systématique de la littérature (Systematic Mapping Study - SMS) portant sur 20 articles scientifiques récents.

---

### Objectif de ce Dépôt

*   **Transparence :** Fournir un accès aux données brutes et aux différentes étapes de traitement et de classification qui ont mené aux résultats présentés dans le mémoire.
*   **Reproductibilité :** Permettre à d'autres chercheurs de comprendre la démarche et, potentiellement, de reproduire ou d'adapter certaines parties de l'analyse.
*   **Réutilisation :** Offrir une base de données de critères et un exemple de script de clustering qui pourraient être utiles pour de futurs travaux de recherche ou des applications pratiques dans le domaine de l'évaluation DevOps.

---

### 📂 Contenu du Dépôt et Workflow du Projet

Le processus d'analyse des données s'est déroulé en plusieurs étapes, reflétées par les fichiers présents dans ce dépôt :

1.  **Étape 1 : Extraction des critères bruts**
    *   **`Grille-d'extraction-finale.xlsx`**:
        *   Contient la grille d'extraction brute des 272 critères (identifiés de L2 à L273) issus des 20 articles analysés. Chaque ligne correspond à un critère avec ses métadonnées initiales.
    *   **`csv-format-Grille-d'extraction-finale.csv`**:
        *   Version au format CSV de la grille d'extraction finale. Ce format est souvent plus adapté pour les analyses automatisées et l'import dans divers outils.

2.  **Étape 2 : Regroupement automatique initial des critères**
    *   **`generate-clusters.py`**:
        *   Script Python utilisé pour effectuer un regroupement automatique (clustering) des critères sémantiquement équivalents en se basant sur leur intitulé en anglais.
        *   *Note : Ce script peut nécessiter des bibliothèques Python spécifiques (voir section "Utilisation").*
    *   **`Clusters_par_critereEN.xlsx`**:
        *   Fichier Excel résultant de l'exécution du script `generate-clusters.py`. Il présente les critères regroupés en clusters thématiques préliminaires, avec les lignes correspondantes de la grille d'extraction.

3.  **Étape 2' (ou complément à l'Étape 2) : Classification manuelle préliminaire**
    *   **`Clusters_par_critereEN-phase-préli.xlsx`**:
        *   Représente le début de la classification manuelle des critères, effectuée en s'appuyant sur les regroupements automatiques proposés par `Clusters_par_critereEN.xlsx`. Cette étape a servi à affiner et valider les clusters.

4.  **Étape 3 : Classification finale (détaillée dans le mémoire)**
    *   La classification finale et consolidée des 272 critères en **16 catégories thématiques principales** et en sous-concepts clés est intégralement présentée en **Annexe A du mémoire de M1**. Les fichiers de ce dépôt illustrent les étapes intermédiaires y menant.

5.  **Étape 4 : Préparation pour analyses approfondies et identification des "Top Critères"**
    *   **`Grille_SMS_avec_colonnes_categorisees.xlsx`**:
        *   Fichier enrichi intégrant les catégories finales (issues de l'Annexe A) et d'autres informations structurées. Ce fichier a été crucial pour :
            *   La réalisation de nombreux graphiques présentés dans le mémoire.
            *   Les analyses des sections 3.5 ("Identification des sous-concepts clés prédominants (“Top Critères”)") et 3.6 ("Qualité et nature des contributions des sources pour les sous-concepts clés") du mémoire.

---

### 🛠️ Utilisation

1.  **Téléchargement :**
    Vous pouvez télécharger le dépôt sous forme d'archive ZIP ou le cloner en utilisant Git :
    ```bash
    git clone https://github.com/Hana-ao/Data-availability-SMS-M1.git
    cd Data-availability-SMS-M1
    ```

2.  **Exploration des données :**
    Les fichiers `.xlsx` peuvent être ouverts avec Microsoft Excel, LibreOffice Calc ou Google Sheets.
    Les fichiers `.csv` peuvent être ouverts avec n'importe quel éditeur de texte ou importés dans des tableurs ou des outils d'analyse de données.

3.  **Exécution du script de clustering (`generate-clusters.py`) :**
    *   Assurez-vous d'avoir un environnement Python 3.x installé.
    *   Ce script peut nécessiter des bibliothèques Python pour le traitement du langage naturel (NLP) et le clustering (par exemple, `pandas`, `nltk`, `scikit-learn`, `sentence-transformers` ou similaires). Veuillez vérifier les `import` au début du script pour connaître les dépendances exactes et les installer (par exemple, via `pip install -r requirements.txt` si un tel fichier est fourni, ou `pip install <nom_bibliotheque>`).
    *   Le script est conçu pour prendre en entrée un fichier CSV (probablement `csv-format-Grille-d'extraction-finale.csv` ou une version adaptée) et produire un fichier Excel avec les clusters.
    ```bash
    python generate-clusters.py
    ```
    *Veuillez adapter le nom du fichier d'entrée dans le script si nécessaire.*

---

### 📚 Références du Mémoire

Ce travail s’appuie notamment sur les méthodologies décrites par :

*   Kitchenham, B., & Charters, S. (2007). *Guidelines for performing Systematic Literature Reviews in Software Engineering*. EBSE Technical Report EBSE-2007-01.
*   Petersen, K., Feldt, R., Mujtaba, S., & Mattsson, M. (2008). *Systematic Mapping Studies in Software Engineering*. Proceedings of the 12th International Conference on Evaluation and Assessment in Software Engineering (EASE).


---

### 📧 Contact

Pour toute question, suggestion ou information complémentaire concernant ce dépôt ou le mémoire associé, veuillez contacter Hana Ouraghene à l'adresse suivante : `44013266@parisnanterre.fr`
