import streamlit as st
from PIL import Image

st.markdown("""
<style>
.stApp { 
    background-color: #fff0f5; 
    color: #4a1221; 
}
div.stButton > button {
    background-color: #ff8da1; 
    color: white;
    border-radius: 12px;
    padding: 10px 24px;
    border: none;
    font-size: 16px;
    font-weight: bold;
    transition: all 0.3s ease;
    box-shadow: 0 4px 6px rgba(0,0,0,0.05);
}
div.stButton > button:hover {
    background-color: #ffb7c5; 
    color: #4a1221;
    border: none;
}
div.stButton > button:active {
    background-color: #d81b60; 
    color: white;
}
h1 { color: #880e4f !important; } 
h2 { color: #ad1457 !important; } 
h3 { color: #c2185b !important; } 
.stTextInput > div > div > input {
    background-color: #ffffff;
    border-color: #ffb7c5;
}
</style>
""", unsafe_allow_html=True)

st.title("🌸 mini app (intento numero 100)")
st.header("Desarrollo de aplicaciones interactivas")
st.write("Explora las distintas modalidades de interacción humano-computador con un toque rosa.")

try:
    image = Image.open('ImagenPrincipal.png')
    st.image(image, caption='Interfaces Multimodales', use_column_width=True)
except:
    st.info("🍥 Imagen no encontrada — asegúrate de subir el archivo para completar el diseño.")

st.subheader("📝 Entrada de texto")
texto = st.text_input('Escribe algo', 'Este es mi texto')
st.write(f'**Texto escrito:** {texto}')
st.caption(f"Caracteres: {len(texto)}")

st.subheader("🎀 Dos columnas interactivas")
col1, col2 = st.columns(2)

with col1:
    st.subheader("Opinión")
    st.write("Las interfaces multimodales son versátiles y mejoran la experiencia del usuario.")
    resp1 = st.checkbox('🌸 Estoy de acuerdo')
    resp2 = st.checkbox('🍥 No estoy de acuerdo')
    if resp1 and not resp2:
        st.success('💖 ¡Correcto! Las interfaces multimodales amplían las posibilidades.')
    if resp2 and not resp1:
        st.error('💭 ¡Interesante perspectiva! ¿Por qué no estás de acuerdo?')
    if resp1 and resp2:
        st.warning('⚠️ Solo puedes elegir una opción.')

with col2:
    st.subheader("Modalidad principal")
    modo = st.radio("¿Qué modalidad es la principal en tu interfaz?",
                    ('👁️ Visual', '🎧 Auditiva', '✋ Táctil'))
    descripciones = {
        '👁️ Visual':   ('La vista es fundamental para tu interfaz.', '🎨'),
        '🎧 Auditiva': ('La audición es fundamental para tu interfaz.', '🔊'),
        '✋ Táctil':   ('El tacto es fundamental para tu interfaz.', '📳'),
    }
    desc, emoji = descripciones[modo]
    st.info(f"{emoji} {desc}")

st.subheader("🩰 Nivel de interactividad")
nivel = st.slider("¿Qué tan interactiva quieres tu interfaz?", 0, 100, 50)
st.progress(nivel)
if nivel < 33:
    st.warning("Interfaz básica — considera agregar más elementos.")
elif nivel < 66:
    st.info("Interfaz moderada — ¡vas bien!")
else:
    st.success("¡Interfaz muy interactiva! 💖")

st.subheader("💮 Botón interactivo")
if "presionado" not in st.session_state:
    st.session_state.presionado = False
    st.session_state.veces = 0

if st.button('🦄 Presiona el botón'):
    st.session_state.presionado = True
    st.session_state.veces += 1

if st.session_state.presionado:
    st.success(f"💖 ¡Gracias por presionarlo! Lo has hecho {st.session_state.veces} vez/veces.")
    if st.session_state.veces >= 5:
        st.balloons()
        st.write("🎉 ¡Has presionado el botón 5 veces!")
else:
    st.write("🌸 No has presionado aún.")

st.subheader("🔮 Selector de modalidad")
in_mod = st.selectbox("Selecciona la modalidad", ("Audio", "Visual", "Háptico"))

acciones = {
    "Audio":   ("Reproducir audio",    "🔊", "success"),
    "Visual":   ("Reproducir video",    "🎬", "info"),
    "Háptico": ("Activar vibración",   "📳", "warning"),
}
accion, emoji, tipo = acciones[in_mod]
getattr(st, tipo)(f"{emoji} La acción es: **{accion}**")