import streamlit as st
import random

st.set_page_config(page_title="Game Tebak Buah PAUD", page_icon="🍎")

st.title("🎮 Game Tebak Buah")
st.write("Pilih jawaban yang benar ya! 😊")

# Data buah
fruits = [
    {"name": "Apel", "emoji": "🍎"},
    {"name": "Pisang", "emoji": "🍌"},
    {"name": "Jeruk", "emoji": "🍊"},
    {"name": "Anggur", "emoji": "🍇"},
]

# Simpan state
if "question" not in st.session_state:
    st.session_state.question = random.choice(fruits)

if "options" not in st.session_state:
    options = [f["name"] for f in fruits]
    random.shuffle(options)
    st.session_state.options = options

# Tampilkan soal
st.subheader(f"Buah apakah ini? {st.session_state.question['emoji']}")

# Pilihan jawaban
answer = st.radio("Pilih jawaban:", st.session_state.options)

# Tombol cek
if st.button("Cek Jawaban"):
    if answer == st.session_state.question["name"]:
        st.success("Benar! Hebat! 🎉")
    else:
        st.error(f"Salah 😢 Jawaban yang benar: {st.session_state.question['name']}")

# Tombol soal baru
if st.button("Soal Baru"):
    st.session_state.question = random.choice(fruits)
    options = [f["name"] for f in fruits]
    random.shuffle(options)
    st.session_state.options = options
    st.rerun()