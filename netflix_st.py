import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt


st.set_page_config(page_title="Analyse Netflix", layout="wide")
st.title("Netflix : Analyse par Générations & Revenus")


@st.cache_data
def load_data():
    return pd.read_csv("netflix_users.csv")

df = load_data()

# MAP : Création d'une SEULE colonne numérique pour le revenu 
prices_dict = {'Basic': 8.99, 'Standard': 13.49, 'Premium': 17.99}
df['Revenu_Mensuel'] = df['Subscription_Type'].map(prices_dict)

# ASSIGN & APPLY : Creation des Génération
def get_generation(age):
    if age >= 59: return "Boomers (59+)"
    elif age >= 43: return "Gen X (43-58)"
    elif age >= 27: return "Millennials (27-42)"
    else: return "Gen Z (18-26)"

df = df.assign(Generation=df['Age'].apply(get_generation))
ordre_voulu = ["Gen Z (18-26)", "Millennials (27-42)", "Gen X (43-58)", "Boomers (59+)"]
df['Generation'] = pd.Categorical(df['Generation'], categories=ordre_voulu, ordered=True)


st.sidebar.header("Filtres")
liste_pays = st.sidebar.multiselect(
    "Choisir les pays :",
    options=sorted(df['Country'].unique()),
    default=["France"]
)

# Filtrage
df_selection = df[df['Country'].isin(liste_pays)]

# Sécurité si l'utilisateur désélectionne tous les pays
if df_selection.empty:
    st.warning("Veuillez sélectionner au moins un pays dans le menu de gauche.")
    st.stop()

# Group by avec sum, mean et std 
stats_gen = df_selection.groupby('Generation', observed=False)['Watch_Time_Hours'].agg(['sum', 'mean', 'std']).reset_index()

# Value_counts pour le camanbert
type_counts = df_selection['Subscription_Type'].value_counts()


collone1, collone2, collone3 = st.columns(3)
collone1.metric("Nombre d'abonnés", f"{len(df_selection):,}")
collone2.metric("Temps Moyen Global", f"{df_selection['Watch_Time_Hours'].mean():.1f} h")
collone3.metric("Revenu Total Mensuel", f"{df_selection['Revenu_Mensuel'].sum():,.0f} €")

st.divider()



col_left, col_right = st.columns(2)

with col_left:
    # GRAPHIQUE 1 : Bar Chart (Moyenne de visionnage par Génération)
    st.subheader("⏱️ Temps moyen par Génération")
    fig1, ax1 = plt.subplots(figsize=(6, 4))
    
    # Couleurs personnalisées pour Matplotlib
    colors = ['#ff9999', '#66b3ff', '#99ff99', '#ffcc99']
    
    
    ax1.bar(stats_gen['Generation'].astype(str), stats_gen['mean'], color=colors, edgecolor='black')
    
    ax1.set_ylabel("Heures moyennes")
    plt.xticks(rotation=15)
    
    # Ajustement de l'axe Y pour mieux voir les différences
    ax1.set_ylim(bottom=df_selection['Watch_Time_Hours'].mean() * 0.8) 
    st.pyplot(fig1)

with col_right:
    # GRAPHIQUE 2 : Pie Chart (Abonnements avec Prix dynamique)
    st.subheader("💳 Répartition des Revenus")
    fig2, ax2 = plt.subplots(figsize=(6, 4))
    
    # Création des étiquettes dynamiques avec le prix 
    labels_avec_prix = [f"{sub} ({prices_dict[sub]}€)" for sub in type_counts.index]
    
    ax2.pie(type_counts, labels=labels_avec_prix, autopct='%1.1f%%', startangle=140, 
            colors=['#e50914', '#b20710', '#831010'], textprops={'color':"w", 'weight':'bold'})
    
    
    ax2.legend(labels_avec_prix, title="Abonnements", loc="center left", bbox_to_anchor=(1, 0, 0.5, 1))
    st.pyplot(fig2)

# GRAPHIQUE 3 : Stacked Bar (Genre préféré par Génération)
st.subheader("🎭 Quels genres les générations préfèrent-elles ?")
# On croise les données avec un crosstab de pandas
genre_gen = pd.crosstab(df_selection['Generation'], df_selection['Favorite_Genre'])

fig3, ax3 = plt.subplots(figsize=(10, 5))
genre_gen.plot(kind='bar', stacked=True, ax=ax3, colormap='tab20')
ax3.set_ylabel("Nombre d'utilisateurs")
plt.xticks(rotation=0)
plt.legend(title='Genres', bbox_to_anchor=(1.01, 1), loc='upper left')
st.pyplot(fig3)


with st.expander("Voir le détail technique des calculs"):
    st.write("Statistiques de visionnage par génération (Somme, Moyenne, Écart-type) :")
    st.dataframe(stats_gen)
    
    st.write("Aperçu des données brutes :")
    st.dataframe(df_selection)