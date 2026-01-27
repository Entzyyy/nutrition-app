# Ishak Boukellal – Nutrition App (POC)

import streamlit as st
import requests

def fetch_product(barcode):
    url = f"https://world.openfoodfacts.org/api/v0/product/{barcode}.json"
    res = requests.get(url).json()

    if res.get("status") == 1:
        return res["product"]
    else:
        return None

st.set_page_config(page_title="Nutrition App", page_icon="🥗", layout="centered")

def scanner():
    st.header("📷 Scanner")
    st.write("Gib ein Lebensmittel oder einen Barcode ein und erhalte eine schnelle Einschätzung.")

    barcode = st.text_input("Barcode eingeben (z. B. 7613034626844)")
    
    if st.button("Scannen"):
        if barcode:
            product = fetch_product(barcode)

            if product:
                st.success(f"{product.get('product_name', 'Unbekanntes Produkt')} wurde analysiert ✅")

                nutriments = product.get("nutriments", {})

                st.write(f"• **Name:** {product.get('product_name', 'N/A')}")
                st.write(f"• **Marke:** {product.get('brands', 'N/A')}")
                st.write(f"• **Nutri-Score:** {product.get('nutriscore_grade', 'N/A').upper()}")
                st.write("---")
                st.write("### 🔍 Nährwerte (pro 100g):")
                st.write(f"- Zucker: {nutriments.get('sugars_100g', 'N/A')} g")
                st.write(f"- Salz: {nutriments.get('salt_100g', 'N/A')} g")
                st.write(f"- Kohlenhydrate: {nutriments.get('carbohydrates_100g', 'N/A')} g")
                st.write(f"- Eiweiß: {nutriments.get('proteins_100g', 'N/A')} g")
                st.write(f"- Fett: {nutriments.get('fat_100g', 'N/A')} g")
                st.write(f"- Gesättigte Fettsäuren: {nutriments.get('saturated-fat_100g', 'N/A')} g")

            else:
                st.error("❌ Produkt nicht gefunden. Bitte überprüfe den Barcode.")
        else:
            st.warning("Bitte einen Barcode eingeben.")



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
    
   
