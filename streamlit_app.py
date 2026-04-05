import streamlit as st
import urllib.parse

st.set_page_config(page_title="Aura Beats", layout="wide")

st.markdown("""
<style>
*{font-family:Poppins,sans-serif!important;}
.stApp{background:linear-gradient(135deg,#FF6B6B 0%,#4ECDC4 100%)!important;}
h1{font-size:3em!important;background:linear-gradient(45deg,#FFD700,#FFFFFF);-webkit-background-clip:text;-webkit-text-fill-color:transparent;text-align:center!important;}
.btn{display:inline-block;background:rgba(255,255,255,0.2)!important;backdrop-filter:blur(20px)!important;border:2px solid white!important;border-radius:25px!important;color:white!important;font-weight:700!important;font-size:1.1em!important;padding:15px 30px!important;margin:10px!important;text-decoration:none!important;}
.btn:hover{background:rgba(255,255,255,0.4)!important;}
.card{background:rgba(255,255,255,0.15)!important;backdrop-filter:blur(20px)!important;border-radius:20px!important;padding:25px!important;margin:15px 0!important;text-align:center!important;border:2px solid rgba(255,255,255,0.3)!important;}
</style>
<meta name='viewport' content='width=device-width, initial-scale=1.0'>
<link rel='manifest' href='data:application/json;base64,eyJuYW1lIjoiQXVyYSBCZWF0cyIsInNob3J0X25hbWUiOiJBdXJhIiwic3RhcnRfdXJsIjoiLyIsImRpc3BsYXkiOiJzdGFuZGFsb25lIiwidGhlbWVfY29sb3IiOiIjRkY2QjZCIiwiYmFja2dyb3VuZF9jb2xvciI6IiNGRjZCNkIifQ=='>
""", unsafe_allow_html=True)

st.markdown("<h1>🔥 Aura Beats</h1>", unsafe_allow_html=True)
st.markdown("<h2 style='text-align:center;color:white;'>🎵 Mood → Perfect Playlist</h2>", unsafe_allow_html=True)

# MOOD SELECTOR
st.markdown("---")
col1,col2,col3=st.columns(3)
if col1.button("🎉 PARTY"):st.session_state.vibe="party"
if col2.button("🌙 CHILL"):st.session_state.vibe="chill"
if col3.button("⚡ HYPE"):st.session_state.vibe="hype"

col4,col5,col6=st.columns(3)
if col4.button("💙 SAD"):st.session_state.vibe="sad"
if col5.button("🔥 RAGE"):st.session_state.vibe="rage"
if col6.button("💖 LOVE"):st.session_state.vibe="love"

vibe=st.session_state.get('vibe','party')

# SMART TEXT
if st.text_input("Type mood...","party gym chill"):
    if 'party' in st.session_state.input.lower():vibe='party'
    elif 'chill' in st.session_state.input.lower():vibe='chill'
    elif 'gym' in st.session_state.input.lower():vibe='hype'

# UNIVERSAL MUSIC LINKS
st.markdown("---")
query=urllib.parse.quote(f"{vibe} music playlist 2024")

st.markdown(f"""
<div class='card'>
<h3 style='color:#1DB954;'>🎵 SPOTIFY</h3>
<a href='https://open.spotify.com/search/{query}' target='_blank' class='btn'>▶️ OPEN SPOTIFY</a>
</div>
<div class='card'>
<h3 style='color:#FF0000;'>📱 YOUTUBE MUSIC</h3>
<a href='https://music.youtube.com/search?q={query}' target='_blank' class='btn'>▶️ YOUTUBE MUSIC</a>
</div>
<div class='card'>
<h3 style='color:#A6A6A6;'>🍎 APPLE MUSIC</h3>
<a href='https://music.apple.com/search?term={query}' target='_blank' class='btn'>▶️ APPLE MUSIC</a>
</div>
<div class='card'>
<h3 style='color:#FF0000;'>📺 YOUTUBE</h3>
<a href='https://youtube.com/results?search_query={query}' target='_blank' class='btn'>▶️ YOUTUBE</a>
</div>
<div class='card'>
<h3 style='color:#4285F4;'>🔍 GOOGLE</h3>
<a href='https://google.com/search?q={query}' target='_blank' class='btn'>🔍 GOOGLE MUSIC</a>
</div>
""", unsafe_allow_html=True)

st.markdown("""
<div style='text-align:center;padding:40px;color:white;background:rgba(0,0,0,0.5);border-radius:25px;margin-top:40px;'>
<h3>📱 Install App</h3>
<p>Chrome: ☰ → "Install Aura Beats"<br>Safari: Share → "Add to Home Screen"</p>
</div>
""", unsafe_allow_html=True)
