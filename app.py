import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import faiss
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI

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

# Dividing the text in different chunks (groups)
def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator='\n',
        chunk_size = 1000, # 1000 characters
        chunk_overlap = 200,
        length_function = len
    )
    chunks = text_splitter.split_text(text)
    return chunks

# converting the text chunks into embeddings and storing inside vectore database
def get_vectorestore(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings()
    vectorestore = faiss.FAISS.from_texts(texts = text_chunks, embedding = embeddings)
    return vectorestore

def get_conversation_chain(vectorestore):
    llm = ChatOpenAI()
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages='True')
    converstion_chain = ConversationalRetrievalChain.from_llm(
        llm = llm,
        retriever= vectorestore.as_retriever(),
        memory = memory
    )
    return converstion_chain

def main():
    load_dotenv()
    # Title for the application
    st.set_page_config(page_title="Chat with Conference Papers", page_icon=":newspaper:")
    
    # to make it persistent
    # since streamlit reinitializes the 
    
    # initializing session_state
    if "conversation" not in st.session_state:
        st.session_state.conversation = None  
    
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
                
                # get the text chunks
                text_chunks = get_text_chunks(raw_text)
                
                # turn it into a vectorstore
                vectorestore = get_vectorestore(text_chunks)
                
                # create converstion chain
                st.session_state.converstion = get_conversation_chain(vectorestore)

    st.session_state.converstion
    

if __name__ == '__main__':
    main()