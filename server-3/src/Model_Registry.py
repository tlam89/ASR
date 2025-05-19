import os

import warnings
warnings.filterwarnings("ignore")

from langchain.llms import LlamaCpp

# from langchain_community.llms import LlamaCpp
from langchain.callbacks.manager import CallbackManager
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

from utils import nostdout


