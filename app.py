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
        st.file_uploader("Upload your PDF")
        st.button("Process")

if __name__ == '__main__':
    main()