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

def main():
    load_dotenv()
    # Title for the application
    st.set_page_config(page_title="Chat with Conference Papers", page_icon=":newspaper:")
    
    st.header("Chat with Conference Papers :newspaper:")
    st.text_input("Ask Question about your document: ")
    
    # The sidebar with text, button and upload option
    with st.sidebar:
        st.subheader("Your documents")
        
        pdf_docs = st.file_uploader(
            "Upload your PDF", accept_multiple_files=True)
        if st.button("Process"):
            # spinner to make it user friendly
            with st.spinner("Processing"):
                # get pdf text
                raw_text = get_pdf_text(pdf_docs)
                st.write(raw_text)
                

if __name__ == '__main__':
    main()