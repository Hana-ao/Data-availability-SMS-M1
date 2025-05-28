import pandas as pd

# 🔹 1. Charger le fichier 
df = pd.read_csv("csv-format-Grille-d'extraction-finale.csv", sep=";")

# 🔹 2. Nettoyer les noms de colonnes
df.columns = [col.strip() for col in df.columns]

# 🔹 3. Générer les numéros de ligne logiques : L2 à Ln (L1 = métadonnées)
df = df.reset_index(drop=True)
df["Ligne"] = ["L" + str(i + 2) for i in range(len(df))]

# 🔹 4. Grouper par critère EN (libellé identique) + agréger les lignes associées
df_clusters = df.groupby("Terme original (EN)").agg({
    "Ligne": lambda x: ", ".join(sorted(x)),
    "Définition du critère": "first",
    "Type du critère (Métrique, Capacité ou Mixte)": "first"
}).reset_index()

# 🔹 5. Renommer les colonnes du tableau final
df_clusters.columns = [
    "Critère (EN)",
    "Lignes associées",
    "Définition",
    "Type"
]

# 🔹 6. Exporter le fichier Excel 
df_clusters.to_excel("Clusters_par_critereEN.xlsx", index=False)

print("✅ Fichier 'Clusters_par_critereEN.xlsx' généré avec succès.")
