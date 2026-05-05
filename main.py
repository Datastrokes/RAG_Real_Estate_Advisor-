from langchain_chroma import Chroma
from data_vector import chroma_db
from langchain_huggingface import HuggingFaceEmbeddings

from langchain_core.messages import SystemMessage, HumanMessage 
from langchain_ollama import ChatOllama
import gradio as gr

embidding=HuggingFaceEmbeddings(model="sentence-transformers/all-MiniLM-L6-v2")
vectors=Chroma(persist_directory=chroma_db,embedding_function=embidding)
retrive=vectors.as_retriever()
system_prompt="""
Youry name is J. You are a knowledgeable, friendly assistant representing the company Jawahar Estate is a professional real 
estate advisory and property services company focused on delivering transparent, data-informed real estate solutions.
You are chatting with a user about real estate .
If relevant, use the given context to answer any question.
If you don't know the answer, say so.
Context:
{context}

aslo use previuse chat from the user_history.
user_history:{user_history}
"""
llm=ChatOllama(model="llama3.1")
user_history=[]
def user_vector(prompt,history):

    docs=retrive.invoke(prompt)
    context="\n\n".join(doc.page_content for doc in docs)
    
    system_message=system_prompt.format(context=context,user_history=history)
    chat=llm.invoke([SystemMessage(content=system_message),HumanMessage(content=prompt)])
    user_history.append([{"role":"user","content":prompt},{"role":"system","content":chat.content}])
    return chat.content


if __name__=="__main__":
    interface=gr.ChatInterface(fn=user_vector)
    interface.launch()
    






