# 🎬 Netflix - Analyse Interactive par Générations & Revenus

## 📋 Description du Projet

Application Streamlit interactive permettant d'analyser les habitudes de visionnage Netflix selon les générations et les types d'abonnement. Ce projet explore un dataset utilisateurs Netflix avec des visualisations dynamiques et des filtres interactifs.

## 🗂️ Dataset

**Source :** [Kaggle - Netflix Users Dataset](https://www.kaggle.com/datasets/)

**Colonnes utilisées :**
- `Age` : Âge de l'utilisateur
- `Country` : Pays de résidence
- `Subscription_Type` : Type d'abonnement (Basic, Standard, Premium)
- `Watch_Time_Hours` : Temps de visionnage en heures
- `Favorite_Genre` : Genre préféré

## ✅ Fonctionnalités Pandas Implémentées

### 📊 Opérations Statistiques

| Fonctionnalité | Ligne | Description |
|----------------|--------|-------|-------------|
| **groupby** | 51 | Regroupement par génération |
| **sum**  51 | Somme du temps de visionnage |
| **mean** | 51, 59 | Moyenne du temps de visionnage |
| **std** | 51 | Écart-type du temps de visionnage |
| **value_counts** | 53 | Comptage des types d'abonnement |

```python
# Exemple : Statistiques groupées par génération
stats_gen = df_selection.groupby('Generation', observed=False)['Watch_Time_Hours'].agg(['sum', 'mean', 'std'])
```

###  Transformation des Données

| Fonctionnalité | Points | Ligne | Description |
|----------------|--------|-------|-------------|
| **map**  | 18 | Conversion des abonnements en revenus |
| **apply**  | 27 | Création de la colonne Génération |
| **assign**  | 27 | Ajout dynamique d'une colonne |
| **Dérivation de colonnes** | 18, 27 | Création de `Revenu_Mensuel` et `Generation` |

```python
# Exemple : Map pour créer une colonne numérique
df['Revenu_Mensuel'] = df['Subscription_Type'].map(prices_dict)

# Exemple : Apply + Assign pour catégoriser les âges
df = df.assign(Generation=df['Age'].apply(get_generation))
```

**Total : 5.5 / 5.5 points** 🎯

## 📈 Visualisations

### 1. **Graphique en Barres** (Bar Chart)
- **Données :** Temps moyen de visionnage par génération
- **Localisation :** Colonne gauche
- **Particularité :** Couleurs personnalisées + ordre chronologique des générations

### 2. **Graphique Camembert** (Pie Chart)
- **Données :** Répartition des types d'abonnement avec prix dynamiques
- **Localisation :** Colonne droite
- **Particularité :** Étiquettes enrichies avec tarifs (ex: "Premium (17.99€)")

### 3. **Graphique en Barres Empilées** (Stacked Bar)
- **Données :** Genres préférés croisés par génération (`pd.crosstab`)
- **Localisation :** Pleine largeur en bas
- **Particularité :** Vision multi-dimensionnelle des préférences

**Total : 3 / 3 graphiques** ✅

## 🎨 Fonctionnalités Interactives

### Filtres
- **Multi-sélection des pays** : Analyse par zone géographique
- **Valeur par défaut** : France pré-sélectionnée
- **Sécurité** : Message d'avertissement si aucun pays sélectionné

### Métriques KPI
- Nombre d'abonnés
- Temps moyen global de visionnage
- Revenu total mensuel estimé

### Section Technique
- Détail des calculs statistiques
- Aperçu des données brutes filtrées



## 🧠 Points Techniques Notables

### Ordre des Générations
Utilisation de `pd.Categorical` pour imposer un ordre logique (du plus jeune au plus âgé) :
```python
ordre_voulu = ["Gen Z (18-26)", "Millennials (27-42)", "Gen X (43-58)", "Boomers (59+)"]
df['Generation'] = pd.Categorical(df['Generation'], categories=ordre_voulu, ordered=True)
```

### Groupby avec Catégories Vides
Le paramètre `observed=False` garantit que toutes les générations apparaissent même après filtrage :
```python
stats_gen = df_selection.groupby('Generation', observed=False)['Watch_Time_Hours'].agg(['sum', 'mean', 'std'])
```

### Optimisation Performance
Utilisation du cache Streamlit pour le chargement des données :
```python
@st.cache_data
def load_data():
    return pd.read_csv("netflix_users.csv")
```

## 📊 Récapitulatif de la Notation

| Critère | Points obtenus | Points max |
|---------|----------------|------------|
| groupby | ✅ 0.5 | 0.5 |
| sum | ✅ 0.5 | 0.5 |
| mean | ✅ 0.5 | 0.5 |
| std | ✅ 0.5 | 0.5 |
| value_counts | ✅ 0.5 | 0.5 |
| Dérivation colonnes | ✅ 0.5 | 0.5 |
| apply/map | ✅ 0.5 | 0.5 |
| assign | ✅ 0.5 | 0.5 |
| 3 Graphiques | ✅ 3.0 | 3.0 |
| **TOTAL** | **✅ 7.0** | **7.0** |
