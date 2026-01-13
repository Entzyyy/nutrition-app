# Ishak Boukellal – Nutrition App (POC)

import streamlit as st
from PIL import Image

st.set_page_config(page_title="Nutrition App", page_icon="🥗", layout="centered")

def scanner():
    st.header("📷 Scanner")
    st.write("Gib ein Lebensmittel ein und erhalte eine schnelle Einschätzung.")
    item = st.text_input("Lebensmittel eingeben (z. B. Cornflakes, Joghurt, Cola)")
    if st.button("Scannen"):
        if item:
            st.success(f"{item} wurde analysiert ✅")
            st.write("• Score: 78/100")
            st.write("Zucker: ... Salz: ... Kohlenhydrate: ... Ballaststoffe: ...  Eiweiss: ... Gesättigte Fettsäuren: ... Zusatzstoffe: ... :")
            st.write("Dieses Produkt enthält weniger ... als andere und ist für den Alltag geeignet")
            st.write("Details: Weniger.. hilft dabei, Energieausbrüche zu vermeiden und ... zu unterstützen")
            st.write("Quelle: WHO - Sugar Intake Guidelines")

        else:
            st.warning("Bitte etwas eingeben        ")
    
            with st.expander("📖 Mehr erfahren"):
                st.write(["details"])
                st.caption(f"Quelle: {['source']}")


def trends():
    st.header("🔥 Trends & Rezepte")

    st.subheader("🥑 Avocado Toast")
    st.write("Beliebt, gesund – achte auf die Portionsgröße.")

    st.subheader("🍕 Protein Pizza")
    st.write("Trend auf TikTok – besser als klassische Pizza.")
 

def stores():
    st.header("🛒 Stores")

    st.write("Empfohlene Produkte:")
    st.write("• Cactus - Bio Haferflocken")
    st.write("• Lidl   - Protein Joghurt")


    products = [
        {"name": "Migros – Bio Haferflocken", "key": "migros"},
        {"name": "Coop – Protein Joghurt", "key": "coop"},
        {"name": "Aldi – Mandelmilch", "key": "aldi"},
    ]



def community():
    st.header("💬 Community (coming soon)")
    st.info("Likes, Kommentare, Challenges – später 🔒")


def profile():
    st.header("👤 Profil")
    st.write("Name: Ishak")
    if st.button("Abmelden"):
        pass

def fridge():
    st.header("🧊 Kühlschrank (coming soon)")
    st.info("Hier kannst du demnächst deine Vorräte verwalten.")



PAGES = {
    "📷 Scanner": scanner,
    "🧊 Kühlschrank": fridge,
    "🔥 Trends & Rezepte": trends,
    "🛒 Stores": stores,
    "💬 Community": community,
    "👤 Profil": profile, }


st.sidebar.title("𝙸𝚜𝚑𝚊𝚔")

page = st.sidebar.radio("Seite auswählen", ["Scanner🔍", "Kühlschrank 🧊", "Trends & Rezepte 🍱", "Stores🏪", "Community🫂", "Profil😀"])

if page == "Scanner🔍":
    scanner()
elif page == "Trends & Rezepte 🍱":
    trends()
elif page == "Stores🏪":
    stores()
elif page == "Kühlschrank 🧊":
    fridge()
elif page == "Community🫂":
    community()
elif page == "Profil😀":
    profile()
    
   
