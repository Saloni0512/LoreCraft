
#Libraries used in this project
import streamlit as st
import anthropic
import os
from dotenv import load_dotenv
import json
from datetime import datetime

# Load environment variables
load_dotenv()

# Get API key from environment variable
API_KEY = os.getenv("ANTHROPIC_API_KEY")

# Initialize session state
if 'favorites' not in st.session_state:
    st.session_state.favorites = []



#This function generates the poem based on user text prompts,
#different types of rhyme schemes and poem styles.
def generate_poem(style, theme, lines, rhyme_scheme=None, meter=None):
    client = anthropic.Anthropic(api_key=API_KEY)
    
    prompt = f"""Human: Write a {style} poem about {theme}. The poem should be {lines} lines long.
    Make sure the poem adheres to the typical structure and characteristics of a {style} poem.
    The poem must create a strong emotional connect with the users and it can be a little complex
    to understand based on specifc {theme}.
    """
    
    if rhyme_scheme:
        prompt += f" Use the rhyme scheme: {rhyme_scheme}."
    if meter:
        prompt += f" Use {meter} meter."

    prompt += "\n\nAssistant: Here's the poem you requested:\n\n"
    
    try:
        response = client.completions.create(
            model="claude-2.1",
            prompt=prompt,
            max_tokens_to_sample=500,
            temperature=0.8
        )
        return response.completion.strip()
    except Exception as e:
        return f"An error occurred: {str(e)}"

def save_poem(poem, style, theme):
    st.session_state.favorites.append({
        'poem': poem,
        'style': style,
        'theme': theme,
        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    })

#Functions for handling the favourite poems
def load_favorites():
    if os.path.exists('favorites.json'):
        with open('favorites.json', 'r') as f:
            return json.load(f)
    return []

def save_favorites():
    with open('favorites.json', 'w') as f:
        json.dump(st.session_state.favorites, f)



#Main UI of the app using StreamLit
def main():
    st.set_page_config(page_title="LoreCraft", page_icon=":scroll:", layout="wide")
    st.title(" LoreCraft 🖋️")
    st.write("Craft beautiful poems using AI! 🌸")

    # Load favorites
    st.session_state.favorites = load_favorites()

    # Sidebar for poem generation
    with st.sidebar:
        st.header("꠫ Poem Settings")
        style = st.selectbox("Select poem style:", ["Haiku", "Sonnet", "Free Verse", "Limerick", "Acrostic"])
        theme = st.text_input("Enter the theme or subject of the poem:")
        lines = st.slider("Number of lines:", min_value=1, max_value=200, value=50)
        
        # Advanced options
        with st.expander("⚙️ Advanced Options"):
            rhyme_scheme = st.text_input("Rhyme scheme (e.g., ABAB):", "")
            meter = st.selectbox("Meter:", ["", "Iambic Pentameter", "Trochaic Tetrameter", "Dactylic Hexameter"])

        if st.button("✨ Generate Poem ✨"):
            if theme:
                with st.spinner("Crafting your masterpiece... 🎶"):
                    poem = generate_poem(style, theme, lines, rhyme_scheme, meter)
                st.session_state.current_poem = poem
                st.session_state.current_style = style
                st.session_state.current_theme = theme
            else:
                st.warning("Please enter a theme for your poem.")

    # Main area for displaying the generated poem
    if 'current_poem' in st.session_state:
        st.header("📜 Your Generated Poem")
        st.write(st.session_state.current_poem)
        if st.button("💾 Save to Favorites"):
            save_poem(st.session_state.current_poem, st.session_state.current_style, st.session_state.current_theme)
            save_favorites()
            st.success("Poem saved to favorites!")

    # Gallery of previously generated poems
    st.header("📚 Poetry Gallery")
    for i, fav in enumerate(st.session_state.favorites):
        with st.expander(f"{fav['style']} about {fav['theme']} - {fav['timestamp']}"):
            st.write(fav['poem'])
            if st.button("🗑️ Remove from Favorites", key=f"remove_{i}"):
                st.session_state.favorites.pop(i)
                save_favorites()
                st.rerun()         

if __name__ == "__main__":
    main()