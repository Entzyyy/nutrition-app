# Ishak Boukellal – Nutrition App (POC)

import streamlit as st

# -----------------------------
# Seiten / Funktionen
# -----------------------------

def scanner():
    st.header("📷 Scanner")
    item = st.text_input("Lebensmittel eingeben (Mock-Scan)")
    if st.button("Scannen"):
        if item:
            st.success(f"{item} wurde analysiert ✅")
            st.write("• Zucker: niedrig")
            st.write("• Score: 78/100")
        else:
            st.warning("Bitte etwas eingeben")


def trends():
    st.header("🔥 Trends & Rezepte")

    st.subheader("🥑 Avocado Toast")
    st.write("Beliebt, gesund – achte auf die Portionsgröße.")

    st.subheader("🍕 Protein Pizza")
    st.write("Trend auf TikTok – besser als klassische Pizza.")


def stores():
    st.header("🛒 Stores")

    st.write("Empfohlene Produkte:")
    st.write("• Migros – Bio Haferflocken")
    st.write("• Coop – Protein Joghurt")


def community():
    st.header("💬 Community (coming soon)")
    st.info("Likes, Kommentare, Challenges – später 🔒")


def profile():
    st.header("👤 Profil")
    st.write("Name: Ishak")
