import glob
from langchain_community.document_loaders import DirectoryLoader,TextLoader
import os
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma



chroma_db="vector_db"

repo="jawahar_estate_rag_data"
# Load all the data from the Directory to list .

def load_data(repo):
    documents=[]
    folder_name=glob.glob(pathname=repo+"/*")
    for doc in folder_name:
        #file_name=os.path.basename(doc)
        documents=DirectoryLoader(path=doc,glob="**/*.md", loader_cls=TextLoader)
        folder_doc=documents.load()
    return folder_doc

# Convert document into chunks with over lap 200 and chunk size 1000
def data_splitter(folder_doc):
    split=RecursiveCharacterTextSplitter(chunk_size=2000,chunk_overlap=200)
    chunks=split.split_documents(documents=folder_doc)
    return chunks

# convet chunk to embeding and save vector to chroma

def vectors(chunks):
    embedding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
    if os.path.exists(chroma_db):
        Chroma(persist_directory=chroma_db,embedding_function=embedding).delete_collection()
    vectors_data=Chroma.from_documents(documents=chunks,embedding=embedding,persist_directory=chroma_db)

if __name__=="__main__":
    data=load_data(repo=repo)
    chunks=data_splitter(data)
    vectors(chunks=chunks)



