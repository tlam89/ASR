import os
import warnings
from typing import List, Set, Tuple, Optional, Any


class TemplateManager:
    '''
        These are the prompt templates corresponding to each phase of a conversation.
        Start, continue, change topic, recall topic or end a discusion.
    '''
    def __init__(self):
        self.template=f'''
        [INST]
            <<SYS>>
                You are a professional assistant.
                DO NOT give false information.
                Always answer as exactly and shortly as possible,           
            <</SYS>>
        [/INST]
        '''
        
                
    def get_template(self,awareness: str, query: str, context: str) -> str:
        if awareness == "start":
            self.template = self.start_discussion(query, context)
        elif awareness == "continue":
            self.template = self.continue_discussion(query, context)
        elif awareness == "change":
            self.template = self.change_discussion(query,context)
        elif awareness == "recall":
            self.template = self.recall_discussion(query, context)
        
            
        return self.template
        
    def start_discussion(self,query, context) -> None:
        template=f'''
            [INST] <<SYS>>
                      You are a professional assistant.
                      Always answer {query} as exactly and shortly as possible,
                      DO NOT give false information.                      
                   <</SYS>>
                    
            [/INST]
        '''
        return template
        
    def continue_discussion(self,query, context) -> None:
        template=f'''
        [INST]
            <<SYS>>
                You are a professional assistant.
                Analyze this {context} and {query}, answer the user's question as similar to the documents as possible.
                DO NOT give false information.
                Always answer as exactly and shortly as possible,           
            <</SYS>>
        [/INST]
        '''
        return template

    def change_discussion(self,query, context) -> str:
        template=f'''
        [INST]
            <<SYS>>
                You are a professional assistant.
                Silently analyze if this {context} is related to {query}.
                Answer {query} according to the documents as accurately as possible.
                DO NOT give false information.
                Always answer as exactly and shortly as possible,           
            <</SYS>>
            
        [/INST]
        '''
        return template
        
    def recall_discussion(self,query, context) -> str:
        template=f'''
        [INST]
            <<SYS>>
                You are a professional assistant.
                Based on this {context}, answer the user's question as similar to the documents as possible.
                DO NOT give false information.
                Always answer as exactly and shortly as possible,           
            <</SYS>>
            {query}
        [/INST]
        '''
        return template