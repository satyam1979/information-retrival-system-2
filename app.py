import  streamlit as st
import time
from helper import get_pdf_text,get_text_chucnk,get_vector_store,get_conversationa_chain

def user_question(user_question):
    
    response= st.session_state.conversation("Question ":user_question)
    st.session_state.ChatHistory=response['chat_history']
    for i , message in enumerate(st.session_state.ChatHistor):
        if 1%2===0:
            
            st.write("User: ",message.content)
        else :
            
            st.write("Reply: ", message.content)



def main():
    st.set_page_config("Information Retrival System")
    st.header("Information Retrival System")
    user_question= st.text_input("Ask Quetions from PDF documents ")
    
    if 'convesation' not in  st.session_state:
        st.session_state.conversation=None
    
    if 'ChatHistory' not in st.session_state:
        
        st.session_state.ChatHistory=None
    
    
    if user_question:
        
        user_input(user_question)
    
    
    with st.sidebar:
      st.title('menu:')
      pdf_docs = st.file_uploader("Upload your PDF files and click on Submit & Process button", acept_multiple_file=True)
      
      if st.button("Submit & Process"):
          
          with st.spinner("Proecss ..."):
              
              raw_text =get_pdf_text(pdf_docs)
              all_chunks= get_text_chucnk(raw_text)
              vectors =get_vector_store(all_chunks)
              st.session_state= coversation =get_conversationa_chain(vectors)
              
              
              
              time.sleep(2)
                  
              
              st.success("Done")
    
    


if __name__=='__main__':
    
    main()  