import streamlit as st
from api_handler import get_cheapest_fruit  # Mock or real API

# Page Configs
st.set_page_config(
    page_title="GOA App Demo",
    layout="centered",
    page_icon="🏝️"
)

# Header for the platform
st.title("🏝️ Grocery Optimisation Assistant")
st.subheader("Find the cheapest grocery from Blinkit, Zepto & more")

st.markdown("Type in your grocery item and I'll find you the best deal!")


fruit = st.chat_input("Grocery Shopping? Tell me   ")

if fruit:
    with st.spinner("Searching... 🔍"):
        result = get_cheapest_fruit(fruit)

    # Check if result is a dict (valid search result with image)
    if isinstance(result, dict) and "message" in result:
        st.success(result["message"])
        if "image" in result:
            st.image(result["image"], width=250, caption=f"{fruit.capitalize()} preview")
    else:
        # Fallback in case of error or no item found
        st.warning(result if isinstance(result, str) else "No result found.")


