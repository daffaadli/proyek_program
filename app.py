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
<<<<<<< HEAD
# Membuat wadah (Card) untuk unggah file PDF
=======

# Membuat wadah untuk unggah file PDF
>>>>>>> temp-branch
st.markdown("<div class='card'>", unsafe_allow_html=True)
st.subheader("📂 Unggah Dokumen PDF")
uploaded_file = st.file_uploader("Pilih file PDF yang ingin dirangkum", type=["pdf"])
st.markdown("</div>", unsafe_allow_html=True)

# Jika file PDF sudah diunggah oleh pengguna
if uploaded_file is not None:
    # Membaca isi file PDF menggunakan pypdf
    reader = PdfReader(uploaded_file)
    extracted_text = ""
    
    # Menggabungkan teks dari setiap halaman PDF
    for page in reader.pages:
        text = page.extract_text()
        if text:
            extracted_text += text + "\n"
            
    st.success(f"Berhasil membaca dokumen! Total karakter teks: {len(extracted_text)}")
    
    # Menampilkan pratinjau teks (opsional)
    with st.expander("Lihat Pratinjau Teks Ekstraksi"):
        st.write(extracted_text[:1000] + "...") # Menampilkan 1000 karakter pertama
        
st.markdown("</div>", unsafe_allow_html=True)
