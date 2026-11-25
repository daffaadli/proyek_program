import streamlit as st
from pypdf import PdfReader
from transformers import pipeline
# Konfigurasi halaman web
st.set_page_title("Smart Reader - AI Summarizer")

# Judul Aplikasi
st.markdown("<h1 style='text-align: center; color: #2c3e50;'>✨ Smart Reader ✨</h1>", unsafe_allow_html=True)