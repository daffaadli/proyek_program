import streamlit as st
from pypdf import PdfReader
from transformers import pipeline

# Konfigurasi halaman web
st.set_page_config(page_title="Smart Reader - AI Summarizer", page_icon="✨", layout="centered")

# Desain Tampilan dengan CSS (Gradasi Pink Muda ke Biru Muda)
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #ffdde1 0%, #ee9ca7 50%, #a1c4fd 100%);
        background-attachment: fixed;
    }
    .main-header {
        color: #2c3e50;
        text-align: center;
        font-weight: bold;
        margin-bottom: 20px;
    }
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Judul Aplikasi
st.markdown("<h1 class='main-header'>✨ Smart Reader ✨</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align: center; color: #34495e;'>Asisten pintar berbasis AI untuk merangkum dokumen dan materi pelajaran PDF dengan cepat.</p>", unsafe_allow_html=True)
