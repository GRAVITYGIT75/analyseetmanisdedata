# 🎬 Netflix - Analyse Interactive



---

## 🚀 Lancement Rapide

### 1️⃣ Prérequis
- Python 3.8 ou supérieur
- pip installé

### 2️⃣ Installation

```bash
# Activer l'environnement virtuel
.\venv\Scripts\Activate.ps1

# Installer les dépendances
pip install -r requirements.txt
```

### 3️⃣ Lancer l'application

```bash
streamlit run netflix_st.py
```

### 4️⃣ Accéder à l'interface

L'application s'ouvre automatiquement dans votre navigateur à l'adresse :
```
http://localhost:8501
```

---

## 📁 Fichiers Nécessaires

| Fichier | Description |
|---------|-------------|
| `netflix_st.py` | Application Streamlit principale |
| `netflix_users.csv` | Dataset des utilisateurs Netflix |
| `requirements.txt` | Dépendances Python |

---

## 🎮 Utilisation

1. **Filtrer par pays** : Utilisez le menu latéral gauche pour sélectionner un ou plusieurs pays
2. **Consulter les KPI** : Nombre d'abonnés, temps moyen, revenus
3. **Analyser les graphiques** :
   - Temps moyen par génération (bar chart)
   - Répartition des abonnements (pie chart)
   - Genres préférés par génération (stacked bar)
4. **Voir les détails** : Cliquez sur "Voir le détail technique des calculs"

---

## 🛠️ Technologies

- **Streamlit** : Interface web interactive
- **Pandas** : Manipulation et analyse de données
- **Matplotlib** : Visualisations graphiques

---

## 📦 Dépendances

```
streamlit
pandas
matplotlib
```

---

## 🐛 Dépannage

**Problème : L'application ne démarre pas**
```bash
# Vérifier que l'environnement virtuel est activé
.\venv\Scripts\Activate.ps1

# Réinstaller les dépendances
pip install -r requirements.txt --force-reinstall
```

**Problème : Erreur FileNotFoundError**
- Vérifiez que `netflix_users.csv` est dans le même dossier que `netflix_st.py`

**Problème : Port déjà utilisé**
```bash
# Lancer sur un autre port
streamlit run netflix_st.py --server.port 8502
```

---

## 📊 Fonctionnalités Pandas

✅ groupby, sum, mean, std  
✅ value_counts  
✅ map, apply, assign  
✅ Dérivation de colonnes (Generation, Revenu_Mensuel)  
✅ Categorical ordering

---