import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_openai import OpenAIEmbeddings
from langchain.indexes import VectorstoreIndexCreator
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import PyPDFLoader


load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

OPENAI_MODEL=os.getenv("OPENAI_MODEL")


def get_llm():
    
    llm = ChatOpenAI(
        model_name=OPENAI_MODEL,
        openai_organization="org-blnPQMoQmrYcj1cORsrpuXZz",
        max_tokens=256,         
        temperature=0,
        top_p=1,
        presence_penalty=0,
        frequency_penalty=0    
    )
    
    return llm


def get_index():
    embeddings = OpenAIEmbeddings()
    pdf_path = "data/2022-Shareholder-Letter.pdf"
    loader = PyPDFLoader(file_path=pdf_path)
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "], 
        chunk_size=1000,
        chunk_overlap=100
    )
    
    index_creator = VectorstoreIndexCreator(
        vectorstore_cls=FAISS,
        embedding=embeddings,
        text_splitter=text_splitter,
    )

    index_from_loader = index_creator.from_loaders([loader]) 
    
    return index_from_loader


def get_rag_response(index, question): #rag client function
    
    llm = get_llm()
    
    response_text = index.query(question=question, llm=llm)
    
    return response_text

