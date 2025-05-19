import os, sys
# import Argsparse
from langchain_community.vectorstores import FAISS, Chroma
from langchain_community.document_loaders import TextLoader, DataFrameLoader, JSONLoader
from langchain.text_splitter import CharacterTextSplitter, RecursiveCharacterTextSplitter
from typing import List, Set, Tuple, Any, Optional
# from langchain.memory import ConversationKGMemory,ConversationBufferMemory
import contextlib
import numpy as np

import nltk
nltk.download('stopwords')
nltk.download('punkt')
from rake_nltk import Rake
import logging

from sklearn.metrics.pairwise import cosine_similarity

class DummyFile:
    def write(self, x): pass
    def flush(self): pass

@contextlib.contextmanager
def nostdout(verbose=False):
    if not verbose:
        save_stdout = sys.stdout
        sys.stdout = DummyFile()
        yield
        sys.stdout = save_stdout
    else:
        yield

def create_docs(filepath: str, **kwarg):
    '''
    
    '''
    loader = TextLoader(filepath)
    text_splitter = RecursiveCharacterTextSplitter(**kwarg)
    docs = text_splitter.split_documents(loader.load())
    return docs

def create_retriever(docs, embedding, db_name:str) -> Any:
    '''
    
    '''
    if db_name == "CHROMA":
        return Chroma.from_documents(docs, embedding)
    elif db_name == "FAISS":
        return FAISS.from_documents(docs, embedding)
    # elif db_name = "ELASTICSEARCH"
    #     return ElasticsearchStore.from_documents(docs, embedding)
    else:
        print("Invalid VectorStore Name!")
        return 

def get_a_list_of_filepath(filename: str) -> str:

    with open(filename, 'r') as file:
        data = file.read()
        
    return data

def get_keywords(query) -> List[str]:
    '''
        Extract keywords from the queries.
    '''
    extractor = Rake(min_length=1, max_length=2)  #change min/max length of the keywords. 
    extractor.extract_keywords_from_text(query)
    keywords = extractor.get_ranked_phrases()
    return keywords

def initialize_a_logger(logger_name:str = "ChatBot.log"):
    logger = logging.getLogger('example_logger')
    
    # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    logger.setLevel(logging.INFO)
    
    # Create a file handler which logs even debug messages
    fh = logging.FileHandler(logger_name, mode='w')
    logger.addHandler(fh)
    return logger

def create_prompt(info):
    prompt= f"""
        Your are in a role of a chest X ray radiologist. Provide the most precise summary based on the following Medical History, Technical Information and Findings.
        Medical History : {info["Medical History"]}.
        Technical Information : {info["Technical Information"]}.
        Findings : {info["Findings"]}
    """
    return prompt

