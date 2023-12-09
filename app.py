import streamlit as st
from dotenv import load_dotenv

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
                

if __name__ == '__main__':
    main()