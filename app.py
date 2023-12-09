import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader

# Function to read from pdfs and extract the text
def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        # Reading each PDF
        pdf_reader = PdfReader(pdf)
        
        # Extracting text from each page
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text