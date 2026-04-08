import os
from PyPDF2 import PdfReader 
from Langchain.text_splitter import RecursiveCharacterTextSplitter
from Langchain.embeddings import GooglePalmEmbeddings
from Langchain.llms import GooglePalm
from Langchain.vectorstores import FAISS
from Langchain.chains import ConversationalRetrivalChain
from Langchain.memory import  ConversationalBufferMemory
from dotenv import  load_dotenv

load_dotenv()
GOOGLE_API_KEY= os.getenv("GOOGLE_API_KEY")

os.environment["GOOGLE_API_KEY"] =GOOGLE_API_KEY

def get_pdf_text(pdf_docs):
    
    text=''
    for pdf in  pdf_docs:
        
        pdf_reader=PdfReader(pdf)
        for page in pdf_reader.pages:
            
            text+=page.extract_text()
    
    return text

def get_text_chucnk(text):

    text_spliter=RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=20)
    
    chunk =text_spliter.split_text(text)
    
    return chunck
    
    
def get_vector_store(text_chunks):
    
    embeddings =GooglePalmEmbeddings()
    store_vector=FAISS.from_texts(text_chunks, embedding =embeddings) 
    
    return store_vector


def get_conversationa_chain(store_vector):

    llm =GooglePalm()
    memory =ConversationalBufferMemory(memory_key='chat_history', return_message=True )
    conversation_chain=ConversationRetrivalChain.form_llm(llm=llm, retriever=store_vector.as_retriever(),memory=memory)
    
    return conversation_chain
    
    


