import os, glob
import sys 
import logging
import asyncio

import time
from datetime import datetime
import warnings
warnings.filterwarnings("ignore")

import numpy as np
import json 

from typing import List, Set, Optional, Dict, Tuple, Any, AsyncIterable
from langchain_community.document_loaders import TextLoader
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings

from sklearn.metrics.pairwise import cosine_similarity

from utils import nostdout, create_retriever, create_docs, get_keywords




class AwarenessManager:
    def __init__(self, cmd_intent_file: str, embeddings):
        self.INTENTION_PARAMS = {
            "separators" : ["\n\n", "\n"],
            "chunk_size" :20,
            "chunk_overlap" : 0
        }
        if os.path.exists(cmd_intent_file):
            self.cmd_intent_file = cmd_intent_file
        else:
            self.cmd_intent_file = "Users/tlam/Documents/mistral/cmd_all.txt"
            
        self.DOCS = create_docs(self.cmd_intent_file, **self.INTENTION_PARAMS)
        
        if embeddings == None:
            embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    
        self.INTENT_DB = create_retriever(self.DOCS, embeddings, "FAISS")

    async def analyze_intent(self, query):
        result = await self.INTENT_DB.asimilarity_search(query, search_kwargs={"k": 1} )
    
        return result[0].page_content.split("***INTENT***")[-1]

    def update_intent(self, query, intent):
        line = f"{query}***INTENT***{intent}"
        try:
            
            with open(self.cmd_intent_file, 'a') as file:
                file.writeline(line)
        except Exception as e:
            raise "Could not add the command due to {e}!"

    def remove_intent(self, query, intent):
        pass
        